
from selenium.webdriver.common.by import By

# ==== Header ====
BTN_CONSTRUCTOR = (By.LINK_TEXT, "Конструктор")
BTN_PROFILE = (By.LINK_TEXT, "Личный Кабинет")  # в некоторых билдах пишут с заглавной К
LOGO_HOME = (By.CSS_SELECTOR, "a[href='/']")

# ==== Main (unauthorized) ====
BTN_LOGIN_FROM_MAIN = (By.XPATH, "//button[normalize-space()='Войти в аккаунт']")
TAB_BUNS = (By.XPATH, "//*[self::div or self::button][contains(@class,'tab')][.//span[normalize-space()='Булки'] or normalize-space()='Булки']")
TAB_SAUCES = (By.XPATH, "//*[self::div or self::button][contains(@class,'tab')][.//span[normalize-space()='Соусы'] or normalize-space()='Соусы']")
TAB_FILLINGS = (By.XPATH, "//*[self::div or self::button][contains(@class,'tab')][.//span[normalize-space()='Начинки'] or normalize-space()='Начинки']")
ACTIVE_TAB = (By.XPATH, "//*[contains(@class,'tab') and contains(@class,'current')]")

# ==== Login / Register / Forgot ====
INPUT_EMAIL_BY_LABEL = (By.XPATH, "//label[normalize-space()='Email']/following::input[1]")
INPUT_PASSWORD_BY_LABEL = (By.XPATH, "//label[normalize-space()='Пароль']/following::input[@type='password'][1]")
INPUT_NAME_BY_LABEL = (By.XPATH, "//label[normalize-space()='Имя']/following::input[1]")

BTN_LOGIN_SUBMIT = (By.XPATH, "//button[normalize-space()='Войти']")
BTN_REGISTER_SUBMIT = (By.XPATH, "//button[normalize-space()='Зарегистрироваться']")
LINK_LOGIN = (By.LINK_TEXT, "Войти")  # ссылка из /register и /forgot-password

# ==== Profile ====
BTN_LOGOUT = (By.XPATH, "//button[normalize-space()='Выход' or normalize-space()='Выйти']")
