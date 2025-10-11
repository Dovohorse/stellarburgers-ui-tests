from selenium.webdriver.common.by import By

# ===== Header / Навигация =====
BTN_CONSTRUCTOR = (By.LINK_TEXT, "Конструктор")
BTN_PROFILE     = (By.LINK_TEXT, "Личный Кабинет")
LOGO_HOME       = (By.CSS_SELECTOR, "a[href='/']")
BTN_LOGOUT      = (By.XPATH, "//button[normalize-space()='Выход' or normalize-space()='Выйти']")

# ===== Главная =====
BTN_LOGIN_FROM_MAIN = (By.XPATH, "//button[normalize-space()='Войти в аккаунт']")

# ===== Формы: ПЕРВИЧНЫЕ (placeholder — стабильно) =====
INPUT_NAME     = (By.CSS_SELECTOR, "input[placeholder='Имя']")
INPUT_EMAIL    = (By.CSS_SELECTOR, "input[placeholder='Email']")
INPUT_PASSWORD = (By.CSS_SELECTOR, "input[placeholder='Пароль']")

# ===== Формы: РЕЗЕРВНЫЕ (label → input) =====
INPUT_NAME_BY_LABEL     = (By.XPATH, "//label[normalize-space()='Имя']/following::input[1]")
INPUT_EMAIL_BY_LABEL    = (By.XPATH, "//label[normalize-space()='Email']/following::input[1]")
INPUT_PASSWORD_BY_LABEL = (By.XPATH, "//label[normalize-space()='Пароль']/following::input[1]")

# ===== Кнопки/ссылки форм =====
BTN_LOGIN_SUBMIT     = (By.XPATH, "//button[normalize-space()='Войти']")
BTN_REGISTER_SUBMIT  = (By.XPATH, "//button[normalize-space()='Зарегистрироваться']")
LINK_LOGIN           = (By.LINK_TEXT, "Войти")

# ===== Конструктор =====
TAB_BUNS     = (By.XPATH, "//span[text()='Булки']")
TAB_SAUCES   = (By.XPATH, "//span[text()='Соусы']")
TAB_FILLINGS = (By.XPATH, "//span[text()='Начинки']")
ACTIVE_TAB   = (By.XPATH, "//*[@aria-selected='true' or contains(@class,'tab_tab_type_current') or contains(@class,'current')]")

# ===== Прочее =====
ORDER_BUTTON       = (By.XPATH, "//button[normalize-space()='Оформить заказ']")
ERR_SHORT_PASSWORD = (By.XPATH, "//*[contains(text(),'Некоррект') and contains(text(),'парол')]")
ERR_USER_EXISTS    = (By.XPATH, "//*[contains(text(),'уже существует')]")  # «Такой пользователь уже существует»
