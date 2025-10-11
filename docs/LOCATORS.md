
# LOCATORS — справочник
Ключевые локаторы, сгруппированные по зонам. Тексты/лейблы выбраны намеренно — это устойчивее, чем классы.

## Header
- `BTN_CONSTRUCTOR` — ссылка «Конструктор» (By.LINK_TEXT)
- `BTN_PROFILE` — ссылка «Личный Кабинет» (By.LINK_TEXT)
- `LOGO_HOME` — логотип, ссылка на корень (CSS `a[href='/']`)

## Главная (неавторизован)
- `BTN_LOGIN_FROM_MAIN` — кнопка «Войти в аккаунт» (XPath по нормализованному тексту)
- `TAB_BUNS` / `TAB_SAUCES` / `TAB_FILLINGS` — вкладки конструктора по тексту
- `ACTIVE_TAB` — любая вкладка, у которой класс содержит `current`

## Формы (логин/регистрация/восстановление)
- `INPUT_EMAIL_BY_LABEL` — инпут почты: берём **первый input после лейбла** `Email`
- `INPUT_PASSWORD_BY_LABEL` — инпут пароля (type='password'), после лейбла `Пароль`
- `INPUT_NAME_BY_LABEL` — инпут имени после лейбла `Имя`
- `BTN_LOGIN_SUBMIT` — кнопка «Войти»
- `BTN_REGISTER_SUBMIT` — кнопка «Зарегистрироваться»
- `LINK_LOGIN` — ссылка «Войти» (на /register и /forgot-password)

## Профиль
- `BTN_LOGOUT` — кнопка «Выход» (или «Выйти» — учтены оба текста)
