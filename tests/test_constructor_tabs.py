
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from conftest import BASE_URL

def _active(d): 
    return len(d.find_elements(*ACTIVE_TAB)) > 0

def test_tabs_switching(driver):
    driver.get(BASE_URL + "/")
    w = WebDriverWait(driver, 10)

    w.until(EC.element_to_be_clickable(TAB_SAUCES)).click()
    w.until(lambda d: _active(d))

    w.until(EC.element_to_be_clickable(TAB_FILLINGS)).click()
    w.until(lambda d: _active(d))

    w.until(EC.element_to_be_clickable(TAB_BUNS)).click()
    w.until(lambda d: _active(d))
