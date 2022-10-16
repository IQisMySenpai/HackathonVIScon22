import warnings

from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from api.mongo_api import MongoAPI
import time
import requests as rq


class NoMatchingLecturer(Warning):
    def __init__(self, message):
        self.message=message

    def __str__(self):
        return repr(self.message)


class MultipleMatchingLecturer(Warning):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


def load_file():
    with open("missing.txt", "r") as f:
        content = f.read()

    lines = content.split("\n")
    lecturer_ids = []

    for l in lines:
        vid = l.split(" ")[-1]
        if vid not in lecturer_ids:
            lecturer_ids.append(vid)

    return lecturer_ids


def search_person(driver: Firefox, f_name: str, l_name: str):
    driver.get("http://vvz.ethz.ch/Vorlesungsverzeichnis/sucheDozierendePre.view")

    last_name = WebDriverWait(driver, timeout=10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='famname']")))
    first_name = WebDriverWait(driver, timeout=10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='rufname']")))

    ActionChains(driver) \
        .send_keys_to_element(first_name, "SAMPLE")\
        .key_down(Keys.LEFT_CONTROL)\
        .send_keys(Keys.BACKSPACE)\
        .send_keys(Keys.BACKSPACE)\
        .send_keys(Keys.BACKSPACE)\
        .key_up(Keys.LEFT_CONTROL) \
        .send_keys(Keys.BACKSPACE) \
        .send_keys(Keys.BACKSPACE) \
        .send_keys(Keys.BACKSPACE) \
        .key_up(Keys.LEFT_CONTROL) \
        .send_keys_to_element(first_name, f_name).perform()

    ActionChains(driver)\
        .send_keys_to_element(last_name, "SAMPLE")\
        .key_down(Keys.LEFT_CONTROL)\
        .send_keys(Keys.BACKSPACE)\
        .send_keys(Keys.BACKSPACE)\
        .send_keys(Keys.BACKSPACE)\
        .key_up(Keys.LEFT_CONTROL) \
        .send_keys(Keys.BACKSPACE) \
        .send_keys(Keys.BACKSPACE) \
        .send_keys(Keys.BACKSPACE) \
        .key_up(Keys.LEFT_CONTROL) \
        .send_keys_to_element(last_name, l_name).perform()

    confirm = WebDriverWait(driver, timeout=10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='search']")))
    confirm.click()


def process_search_results(driver: Firefox, pers_id: int, lecturer: str):
    last_name = WebDriverWait(driver, timeout=10).until(
        EC.presence_of_element_located((By.XPATH, "//table/tbody/tr/td/b/a")))

    elms = driver.find_elements(By.XPATH, "//table/tbody/tr/td/b/a")

    matching_urls = []

    for e in elms:
        url = e.get_attribute("href")

        if pers_id.__str__() in url:
            matching_urls.append(url)

    if len(matching_urls) == 0:
        warnings.warn(NoMatchingLecturer(f"Lecturer: '{lecturer}' has no matching url"))
    elif len(matching_urls) > 1:
        warnings.warn(MultipleMatchingLecturer(f"Lecturer: '{lecturer}' has no matching url"))

    return matching_urls


def get_lecturer_person_url(driver: Firefox, start_url: str, lecturer: str):
    driver.get(start_url)

    URL_row = driver.find_elements(By.XPATH, "//table/tbody/tr/td[text()='URL']")
    assert len(URL_row) <= 1, f"More Table Rows found that are URL {lecturer}"
    if len(URL_row) == 0:
        return None

    link = URL_row[0].find_elements(By.XPATH, "../td/a")
    assert len(URL_row) <= 1, f"More Table Columns found that are expected for a single url {lecturer}"
    return link[0].get_attribute("href")


def find_image(driver: Firefox, url: str, lecturer: str, vvz_id: int):
    driver.get(url)

    # image version 1
    imgs = driver.find_elements(By.XPATH, "//figure/img")

    if len(imgs) > 1:
        if "bsse.ethz.ch" in driver.current_url:
            return None
        print(f"WARNING: {lecturer} has multiple images matching: //figure/img")

    if len(imgs) == 0:
        if "researchgate" in driver.current_url:
            return None
        print("NO image found")
        with open("missing.txt", "a") as f:
            f.write(lecturer + " " + str(vvz_id))
            f.write("\n")
        return None

    return imgs[0].get_attribute("src")


def download_image(url: str, vvz_id: int):
    if url is None:
        return None
    resp = rq.get(url=url, headers={"user-agent": "Ima"})

    if resp.ok:
        if "?" in url:
            url = url.split("?")[0]
        ext = url.split(".")[-1]
    else:
        print(f"Failed to Download {url}")
        return None

    with open(f"/home/alisot2000/Desktop/lecturer/{vvz_id}.{ext}", "wb") as f:
        f.write(resp.content)


if __name__ == "__main__":
    driver = Firefox()

    ids = load_file()

    mongo = MongoAPI('vvzpp.5byhvi1.mongodb.net', 'VVZpp', 'admin', 'LR3I3ChKSA59lVmC')

    find_many = mongo.find(collection="professors")

    for i in range(0, len(find_many)):
        entry = find_many[i]
        # print(f"{i + 1} of {len(find_many)}")

        if str(entry["vvz_id"]) not in ids:
            continue

        print(entry["vvz_id"])

        try:
            search_person(driver, f_name=entry["first_name"], l_name=entry["last_name"])

            lecturer_full_name = entry["first_name"] + " " + entry["last_name"]
            lecturer_urls = process_search_results(driver, entry["vvz_id"], lecturer=f"{lecturer_full_name}")

            for url in lecturer_urls:
                prs_url = get_lecturer_person_url(driver, url, lecturer_full_name)

                if prs_url is not None:
                    img_url = find_image(driver, prs_url, lecturer_full_name, entry["vvz_id"])

                    download_image(img_url, entry["vvz_id"])
        except Exception as e:
            print(entry["vvz_id"])
            print(e)

        input("Press enter to continue")


