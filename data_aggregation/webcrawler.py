from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    driver = Firefox()
    driver.get("https://www.bi.id.ethz.ch/personensuche/personenFormular.view")

    elm = WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='icon']")))
    elm.click()

    elm = WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='icon']")))

