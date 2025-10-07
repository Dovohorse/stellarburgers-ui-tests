
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import *
from utils.generators import gen_email, gen_password
from conftest import BASE_URL

def open_login(d): d.get(BASE_URL + "/login")
def open_register(d): d.get(BASE_URL + "/register")
def open_forgot(d): d.get(BASE_URL + "/forgot-password")

def do_login(d, email, password):
    open_login(d)
    w = WebDriverWait(d, 12)
    w.until(EC.visibility_of_element_located(INPUT_EMAIL_BY_LABEL)).send_keys(email)
    d.find_element(*INPUT_PASSWORD_BY_LABEL).send_keys(password)
    d.find_element(*BTN_LOGIN_SUBMIT).click()
    # успех → видим «Оформить заказ»
    w.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Оформить заказ']")))

def do_register(d, email, password, name="Егор"):
    open_register(d)
    w = WebDriverWait(d, 12)
    w.until(EC.visibility_of_element_located(INPUT_NAME_BY_LABEL)).send_keys(name)
    d.find_element(*INPUT_EMAIL_BY_LABEL).send_keys(email)
    d.find_element(*INPUT_PASSWORD_BY_LABEL).send_keys(password)
    d.find_element(*BTN_REGISTER_SUBMIT).click()

def test_register_success(driver):
    email, pwd = gen_email(), gen_password(8)
    do_register(driver, email, pwd)
    # обычно редирект на /login
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(BTN_LOGIN_SUBMIT))

def test_register_short_password_error(driver):
    email, short_pwd = gen_email(), "12345"  # < 6
    do_register(driver, email, short_pwd)
    # ждём ошибку «Некорректный пароль» ИЛИ остаёмся на форме регистрации
    WebDriverWait(driver, 6).until(
        EC.any_of(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Некоррект') and contains(text(),'парол')]")),
            EC.visibility_of_element_located(BTN_REGISTER_SUBMIT)
        )
    )

def test_login_from_main_button(driver):
    email, pwd = gen_email(), gen_password()
    do_register(driver, email, pwd)
    driver.get(BASE_URL + "/")
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(BTN_LOGIN_FROM_MAIN)).click()
    do_login(driver, email, pwd)

def test_login_from_profile_header(driver):
    email, pwd = gen_email(), gen_password()
    do_register(driver, email, pwd)
    driver.get(BASE_URL + "/")
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(BTN_PROFILE)).click()
    do_login(driver, email, pwd)

def test_login_from_register_form_link(driver):
    email, pwd = gen_email(), gen_password()
    do_register(driver, email, pwd)       # после регы попадаем на /login
    open_register(driver)                 # открываем /register снова
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(LINK_LOGIN)).click()
    do_login(driver, email, pwd)

def test_login_from_forgot_password_form_link(driver):
    email, pwd = gen_email(), gen_password()
    do_register(driver, email, pwd)
    open_forgot(driver)
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(LINK_LOGIN)).click()
    do_login(driver, email, pwd)
