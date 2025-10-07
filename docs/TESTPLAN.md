
# Маппинг тестов к требованиям задания

## Регистрация
- **Успешная регистрация** — `tests/test_auth.py::test_register_success`
- **Ошибка при коротком пароле (<6)** — `tests/test_auth.py::test_register_short_password_error`

## Вход (4 способа)
- **С главной кнопкой «Войти в аккаунт»** — `tests/test_auth.py::test_login_from_main_button`
- **Через «Личный Кабинет» в хедере** — `tests/test_auth.py::test_login_from_profile_header`
- **Из формы регистрации по ссылке «Войти»** — `tests/test_auth.py::test_login_from_register_form_link`
- **Из формы восстановления пароля по ссылке «Войти»** — `tests/test_auth.py::test_login_from_forgot_password_form_link`

## Переходы и выход
- **Переход в профиль** — `tests/test_profile_and_nav.py::test_go_to_profile`
- **Возврат в конструктор кнопкой «Конструктор»** — `tests/test_profile_and_nav.py::test_back_to_constructor_by_button`
- **Возврат по клику на логотип** — `tests/test_profile_and_nav.py::test_back_to_constructor_by_logo`
- **Выход из аккаунта** — `tests/test_profile_and_nav.py::test_logout`

## Конструктор
- **Переключение вкладок «Булки/Соусы/Начинки»** — `tests/test_constructor_tabs.py::test_tabs_switching`
