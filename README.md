
# UI‑тесты Stellar Burgers (Selenium + pytest)

Готовый минимально‑жизнеспособный набор автотестов под учебный стенд **stellarburgers.nomoreparties.site**.
Покрывает регистрацию, вход (4 способа), переходы в профиль/конструктор, выход и переключение вкладок «Булки/Соусы/Начинки».

## ⚙️ Требования
- Python 3.10+
- Браузер: **Chrome** (по заданию) или **Edge**
- Пакеты: `selenium`, `webdriver-manager`, `pytest`

## 🚀 Установка
```powershell
# в корне проекта
pip install -U -r requirements.txt
```

## ▶️ Запуск
Chrome (по умолчанию):
```powershell
pytest -q
```

Edge:
```powershell
$env:SB_BROWSER="edge"; pytest -q
```
> Браузер и URL задаются переменными окружения:
- `SB_BROWSER`: `chrome` (дефолт) или `edge`
- `SB_URL`: по умолчанию `https://stellarburgers.nomoreparties.site`

Примеры:
```powershell
# запустить только авторизационные тесты
pytest -q tests/test_auth.py

# запустить по ключевому слову
pytest -q -k login

# подробный вывод
pytest -vv
```

## 🧭 Структура
```
stellarburgers_ui_tests/
  conftest.py          # фикстура driver (Chrome/Edge), BASE_URL и выбор браузера
  locators.py          # локаторы элементов UI
  utils/
    generators.py      # генераторы email/паролей (уникальные учётки для регистр.)
  tests/
    test_auth.py               # регистрация + 4 способа входа
    test_profile_and_nav.py    # профиль, конструктор, логотип, выход
    test_constructor_tabs.py   # вкладки «Булки/Соусы/Начинки»
  docs/
    TESTPLAN.md        # соответствие кейсам из задания
    LOCATORS.md        # справочник локаторов с пояснениями
  scripts/
    run_chrome.ps1     # запуск в Chrome
    run_edge.ps1       # запуск в Edge
  requirements.txt
  pytest.ini
  .gitignore
  README.md
```

## ❗️ Заметки по стабильности
- Локаторы привязаны к **видимому тексту** и лейблам форм (менее хрупко, чем к классам).  
- В тестах используются **явные ожидания** `WebDriverWait` + `EC.*`, чтобы избежать гонок.  
- Если билд стенда отличается (другой текст на кнопке и т.п.) — правим `locators.py` точечно.

## 🤝 Как обновить локаторы
Правьте только `locators.py`. Тесты ничего не знают о конкретных XPath — зависят от констант.

## 🧪 Что покрыто (коротко)
- Регистрация (успех) и ошибка для короткого пароля (<6)
- Вход: главная, «Личный кабинет», из регистрации, из восстановления
- Переход в профиль; возврат в конструктор кнопкой и по логотипу
- Выход из аккаунта
- Вкладки «Булки/Соусы/Начинки»
Подробно см. `docs/TESTPLAN.md`.

Техно-примечание: стартовый PR для ревью.
