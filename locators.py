class StellarLocators:

    PA_BUTTON = "Личный Кабинет" # Переход в личный кабинет
    INPUT_ACCOUNT = ".//button[text()='Войти в аккаунт']" # Войти в аккаунт на главной странице

    # Ожидания
    AUTH_LOGIN = "Auth_login__3hAey" # Ожидание открытия личного кабинета
    MAIN_PAGE = "BurgerIngredients_ingredients__1N8v2" # Ожидание перехода на главную страницу
    ACCOUNT_LIST = "Account_listItem__35dAP" # Ожидание открытия личного кабинета
    INPUT_MAIN = "App_componentContainer__2JC2W" # Ожидание открытия главной страницы
    ACCOUNT_LOGIN = "Account_nav__Lgali" # Ожидание открытия личного кабинета после регистрации

    # Вход в аккаунт
    INPUT_EMAIL = ".//input[@type='text']" # Ввод email для входа
    INPUT_PASSWORD = ".//input[@type='password']" # Ввод пароля для входа
    ENTER_BUTTON = ".//button[text()='Войти']" # Кнопка Войти

    OUT = ".//button[text()='Выход']" # Выход из личного кабинета

    CONSTRUCT_BUTTON = ".//a[@class='AppHeader_header__link__3D_hX']" # Кнопка Конструктор
    LOGO = ".//div[@class='AppHeader_header__logo__2D0X2']" # Нажатие на кнопку Stellar Burgers

    ERROR_PASS = ".//p[text()='Некорректный пароль']" # Ввод некорректного пароля

    FILLINGS = ".//div/span[text()='Начинки']" # Переход к разделу Начинки
    SAUCES = ".//div/span[text()='Соусы']" # Переход к разделу Соусы
    ROLLS = ".//div/span[text()='Булки']" # Переход к разделу Булки

    # Восстановление пароля
    RECOVER_PASS = "Восстановить пароль" # Восстановить пароль
    TEXT_INPUT = "Войти" # Текст войти

    # Регистрация нового пользователя
    REG = "Зарегистрироваться" # Нажать на текст Зарегистрироваться
    NAME_REG = ".//label[text()='Имя']/../input" # Поле ввода имени
    EMAIL_REG = ".//label[text()='Email']/../input" # Поле ввода email
    PASS_REG = ".//label[text()='Пароль']/../input" # Поле ввода пароля
    BUT_REG = ".//button[text()='Зарегистрироваться']" # Кнопка Зарегистрироваться

    # Заголовки
    HEAD_ROLLS = ".//h2[text() = 'Булки']" # Булки
    HEAD_SAUCES = ".//h2[text() = 'Соусы']" # Соусы
    HEAD_FILLINGS = ".//h2[text() = 'Начинки']" # Начинки