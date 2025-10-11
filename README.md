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

Закрыл замечания ревью: заменил `sleep` на `WebDriverWait`, централизовал локаторы, вынес фикстуры в `conftest.py`, добавил явный `assert` для переключения вкладок (устойчиво к aria-selected/классу), вынес вспомогательные сценарии в `helpers/`, добавил `config.py` с переменными окружения.

---

## Что изменилось
- `tests/test_constructor_tabs.py`: добавлен **явный assert** после ожидания; проверяется активность **контейнера** таба (ancestor с `role="tab"` или класс `...current...`), а не `span`.
- `locators.py`: локаторы централизованы; тесты больше не хранят селекторы внутри.
- `conftest.py`: только фикстуры и инициализация драйвера (без хардкода URL).
- `helpers/driver_factory.py`, `helpers/auth.py`, `helpers/ui.py`: вынесены хелперы (логин/навигация/ожидания/фабрика драйвера).
- `config.py`: BASE_URL/BROWSER и таймауты, поддержка переменных окружения (`SB_BROWSER`, `SB_URL`, `SB_CHROMEDRIVER_PATH`, `SB_EDGEDRIVER_PATH`).
- `tests/test_auth.py`, `tests/test_profile_and_nav.py`: убраны `sleep`, добавлены явные ожидания/ассерты, лёгкая чистка нейминга.

---

## Как запустить проверку локально (Windows/PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt

$env:SB_BROWSER = "edge"            # или "chrome"
$env:SB_URL = "https://stellarburgers.nomoreparties.site"

.\.venv\Scripts\pytest -q
# точечно:
.\.venv\Scripts\pytest tests/test_constructor_tabs.py::TestConstructorTabs::test_tab_switch -vv -s
