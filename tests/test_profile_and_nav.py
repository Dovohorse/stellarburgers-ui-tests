
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import *
from utils.generators import gen_email, gen_password
from conftest import BASE_URL

def login_ready(d):
    email, pwd = gen_email(), gen_password()
    # reg
    d.get(BASE_URL + "/register")
    w = WebDriverWait(d, 12)
    w.until(EC.visibility_of_element_located(INPUT_NAME_BY_LABEL)).send_keys("Егор")
    d.find_element(*INPUT_EMAIL_BY_LABEL).send_keys(email)
    d.find_element(*INPUT_PASSWORD_BY_LABEL).send_keys(pwd)
    d.find_element(*BTN_REGISTER_SUBMIT).click()
    # login
    w.until(EC.visibility_of_element_located(BTN_LOGIN_SUBMIT))
    d.find_element(*INPUT_EMAIL_BY_LABEL).send_keys(email)
    d.find_element(*INPUT_PASSWORD_BY_LABEL).send_keys(pwd)
    d.find_element(*BTN_LOGIN_SUBMIT).click()
    w.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Оформить заказ']")))
    return email, pwd

def test_go_to_profile(driver):
    login_ready(driver)
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(BTN_PROFILE)).click()
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located(BTN_LOGOUT))

def test_back_to_constructor_by_button(driver):
    login_ready(driver)
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(BTN_PROFILE)).click()
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located(BTN_LOGOUT))
    driver.find_element(*BTN_CONSTRUCTOR).click()
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space()='Соберите бургер']")))

def test_back_to_constructor_by_logo(driver):
    login_ready(driver)
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(BTN_PROFILE)).click()
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located(BTN_LOGOUT))
    driver.find_element(*LOGO_HOME).click()
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space()='Соберите бургер']")))

def test_logout(driver):
    login_ready(driver)
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(BTN_PROFILE)).click()
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(BTN_LOGOUT)).click()
    WebDriverWait(driver, 8).until(
        EC.any_of(
            EC.visibility_of_element_located(BTN_LOGIN_SUBMIT),
            EC.visibility_of_element_located(BTN_LOGIN_FROM_MAIN)
        )
    )
