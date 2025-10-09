import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import BASE_URL
from helpers.auth import do_register, do_login, open_register, open_forgot
from utils.generators import gen_email, gen_password
from locators import (
    BTN_LOGIN_FROM_MAIN, BTN_PROFILE, LINK_LOGIN,
    BTN_LOGIN_SUBMIT, ERR_SHORT_PASSWORD, ORDER_BUTTON
)

@pytest.mark.usefixtures("driver")
class TestAuth:

    def test_register_success(self, driver):
        email, password = gen_email(), gen_password()
        do_register(driver, email, password)
        # Явная проверка — форма логина видна (и/или редирект на /login)
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BTN_LOGIN_SUBMIT))

    def test_register_short_password_error(self, driver):
        email, bad = gen_email(), "12345"
        open_register(driver)
        do_register(driver, email, bad)  # дождётся формы логина только при успехе
        # Проверяем, что видна ошибка некорректного пароля
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ERR_SHORT_PASSWORD))

    def test_login_from_main_button(self, driver):
        # подготовим валидного пользователя
        email, password = gen_email(), gen_password()
        do_register(driver, email, password)

        driver.get(BASE_URL + "/")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(BTN_LOGIN_FROM_MAIN)).click()
        do_login(driver, email, password)
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ORDER_BUTTON))

    def test_login_from_profile_header(self, driver):
        email, password = gen_email(), gen_password()
        do_register(driver, email, password)

        driver.get(BASE_URL + "/")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(BTN_PROFILE)).click()
        do_login(driver, email, password)
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ORDER_BUTTON))

    def test_login_from_register_form_link(self, driver):
        email, password = gen_email(), gen_password()
        do_register(driver, email, password)

        open_register(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LINK_LOGIN)).click()
        do_login(driver, email, password)
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ORDER_BUTTON))

    def test_login_from_forgot_password_form_link(self, driver):
        email, password = gen_email(), gen_password()
        do_register(driver, email, password)

        open_forgot(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LINK_LOGIN)).click()
        do_login(driver, email, password)
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ORDER_BUTTON))
