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

    FILLINGS = ".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'][2]" # Переход к разделу Начинки
    SAUCES = ".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'][1]" # Переход к разделу Соусы
    ROLLS = ".//div/span[text()='Булки']" # Переход к разделу Булки

    # Восстановление пароля
    RECOVER_PASS = "Восстановить пароль" # Восстановить пароль
    TEXT_INPUT = "Войти" # Текст войти

    # Регистрация нового пользователя
    REG = "Зарегистрироваться" # Нжаать на текст Зарегистрироваться
    NAME_REG = ".//fieldset[1]/div/div/input[@name='name']" # Поле ввода имени
    EMAIL_REG = ".//fieldset[2]/div/div/input[@name='name']" # Поле ввода email
    PASS_REG =  ".//fieldset[3]/div/div/input[@name='Пароль']" # Поле ввода пароля
    BUT_REG = ".//button[text()='Зарегистрироваться']" # Кнопка Зарегистрироваться

    # Заголовки
    HEAD_ROLLS = ".//h2[text() = 'Булки']" # Булки
    HEAD_SAUCES = ".//h2[text() = 'Соусы']" # Соусы
    HEAD_FILLINGS = ".//h2[text() = 'Начинки']" # Начинки