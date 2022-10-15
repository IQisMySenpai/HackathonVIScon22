from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from api.mongo_api import MongoAPI
import time


def search_person(driver: Firefox, f_name: str, l_name: str):
    driver.get("http://vvz.ethz.ch/Vorlesungsverzeichnis/sucheLehrangebotPre.view")

    first_name = WebDriverWait(driver, timeout=10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='famname']")))
    last_name = WebDriverWait(driver, timeout=10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='rufname']']")))

    ActionChains(driver).send_keys_to_element(first_name, f_name).perform()
    ActionChains(driver).send_keys_to_element(last_name, l_name).perform()


if __name__ == "__main__":
    driver = Firefox()

    mongo = MongoAPI('vvzpp.5byhvi1.mongodb.net', 'VVZpp', 'admin', 'LR3I3ChKSA59lVmC')

    find_many = mongo.find(collection="professors")

    for entry in find_many:
        search_person(driver, f_name=entry["first_name"], l_name=entry["last_name"])

        time.sleep(10)
