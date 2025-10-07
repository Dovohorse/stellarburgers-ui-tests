Stellar Burgers — UI tests (Selenium + pytest)

Мини-набор автотестов для учебного стенда stellarburgers.nomoreparties.site.

Требования

Python 3.10+

Браузер: Chrome (по заданию) или Edge

Библиотеки: selenium, webdriver-manager, pytest

Установка
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

Запуск

Chrome (по умолчанию):

pytest -q


Edge:

$env:SB_BROWSER="edge"; pytest -q


Переменные окружения:

SB_BROWSER: chrome | edge (по умолчанию chrome)

SB_URL: базовый URL стенда (по умолчанию https://stellarburgers.nomoreparties.site)

Примеры:

pytest -q tests/test_auth.py
pytest -q -k login
pytest -vv

Структура проекта
conftest.py           # фикстура driver, выбор браузера, BASE_URL
locators.py           # локаторы элементов
utils/
  generators.py       # генераторы email/паролей
tests/
  test_auth.py                # регистрация + 4 способа входа
  test_profile_and_nav.py     # профиль, конструктор, логотип, выход
  test_constructor_tabs.py    # вкладки «Булки/Соусы/Начинки»
docs/
  TESTPLAN.md         # соответствие кейсам из задания
  LOCATORS.md         # справочник локаторов

Покрытие

Регистрация: успешная и ошибка при коротком пароле (<6)

Вход: с главной, через «Личный кабинет», из регистрации, из восстановления пароля

Переход в личный кабинет; возврат в конструктор (кнопкой и по логотипу)

Выход из аккаунта

Переключение вкладок «Булки/Соусы/Начинки»

Заметки

Локаторы привязаны к текстам/лейблам, используются явные ожидания WebDriverWait.

Каждый тест автономен и завершает сессию браузера.

Техно-примечание: стартовый PR для ревью.