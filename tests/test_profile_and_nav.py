import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import BASE_URL
from helpers.auth import login_ready
from locators import BTN_PROFILE, BTN_CONSTRUCTOR, LOGO_HOME, BTN_LOGOUT, BTN_LOGIN_SUBMIT, ORDER_BUTTON

@pytest.mark.usefixtures("driver")
class TestProfileAndNav:

    def test_go_to_profile(self, driver):
        login_ready(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(BTN_PROFILE)).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BTN_LOGOUT))

    def test_back_to_constructor_by_button(self, driver):
        login_ready(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(BTN_PROFILE)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(BTN_CONSTRUCTOR)).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ORDER_BUTTON))

    def test_back_to_constructor_by_logo(self, driver):
        login_ready(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(BTN_PROFILE)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LOGO_HOME)).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ORDER_BUTTON))

    def test_logout(self, driver):
        login_ready(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(BTN_PROFILE)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(BTN_LOGOUT)).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BTN_LOGIN_SUBMIT))
