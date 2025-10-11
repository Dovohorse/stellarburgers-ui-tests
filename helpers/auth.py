# helpers/auth.py — навигация и сценарии регистрации/логина (быстрее)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from config import BASE_URL
from locators import (
    INPUT_NAME_BY_LABEL, INPUT_EMAIL_BY_LABEL, INPUT_PASSWORD_BY_LABEL,
    BTN_REGISTER_SUBMIT, BTN_LOGIN_SUBMIT, ORDER_BUTTON,
    ERR_SHORT_PASSWORD, ERR_USER_EXISTS
)
from utils.generators import gen_email, gen_password

DEFAULT_TIMEOUT = 6         # было 10–12 -> уменьшаем
FAST_TIMEOUT     = 3        # для полей формы

# --- Навигация ---
def open_login(d):    d.get(BASE_URL + "/login")
def open_register(d): d.get(BASE_URL + "/register")
def open_forgot(d):   d.get(BASE_URL + "/forgot-password")

# --- Хелперы ожиданий ---
def _wait(d, timeout=DEFAULT_TIMEOUT):  # короче запись
    return WebDriverWait(d, timeout)

def _type(d, locator, text):
    el = _wait(d, FAST_TIMEOUT).until(EC.presence_of_element_located(locator))
    el.clear(); el.send_keys(text)
    return el

# --- Регистрация ---
def do_register(d, email, password, name="Egor"):
    open_register(d)

    # поля (без избыточных двойных ожиданий)
    _type(d, INPUT_NAME_BY_LABEL, name)
    _type(d, INPUT_EMAIL_BY_LABEL, email)
    _type(d, INPUT_PASSWORD_BY_LABEL, password)

    d.find_element(*BTN_REGISTER_SUBMIT).click()

    # Успех: появилась форма логина
    # Ошибки: короткий пароль / «пользователь уже существует»
    _wait(d, DEFAULT_TIMEOUT).until(EC.any_of(
        EC.visibility_of_element_located(BTN_LOGIN_SUBMIT),
        EC.visibility_of_element_located(ERR_SHORT_PASSWORD),
        EC.visibility_of_element_located(ERR_USER_EXISTS),
    ))

# --- Логин ---
def do_login(d, email, password):
    open_login(d)
    _type(d, INPUT_EMAIL_BY_LABEL, email)
    _type(d, INPUT_PASSWORD_BY_LABEL, password)
    d.find_element(*BTN_LOGIN_SUBMIT).click()

    # Быстрее, но устойчиво: ждём либо кнопку заказа, либо редирект на /
    WebDriverWait(d, 12).until(EC.any_of(
        EC.visibility_of_element_located(ORDER_BUTTON),
        EC.url_contains(BASE_URL + "/"),
    ))
# --- Быстрый доступ к «готовой» сессии (кэш на время ранa pytest) ---
_CACHED = {"email": None, "pwd": None}

def login_ready(d):
    """
    Создаёт пользователя один раз за прогон и переиспользует его.
    Это сильно ускоряет все тесты, где нужна авторизация.
    """
    if _CACHED["email"] and _CACHED["pwd"]:
        # пробуем сразу войти
        try:
            do_login(d, _CACHED["email"], _CACHED["pwd"])
            return _CACHED["email"], _CACHED["pwd"]
        except Exception:
            # если сессия/аккаунт сломались — пересоздадим ниже
            pass

    email, pwd = gen_email(), gen_password()
    do_register(d, email, pwd)   # если уже существует — условие выше отловит это
    do_login(d, email, pwd)

    _CACHED["email"], _CACHED["pwd"] = email, pwd
    return email, pwd
