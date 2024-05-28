В данном проекте реализуется UI-тестирование сайта https://stellarburgers.nomoreparties.site/

В проекте используется директория tests, которая включет в себя все проведенные автотесты, файл .gitignore, файл
локаторов locators.py, файл с фикстурой conftest.py.

Файлы директории tests:
1. test_error_reg - тестирование отсутствие возможности регистрации с некорректным паролем
2. test_in_personal_account - переход по клику в личный кабинет
3. test_input_from_main_page - вход в аккаунт через главную страницу
4. test_input_from_pass_rec - вход в аккаунт через форму восстановления пароля
5. test_input_from_personal_account - вход через личный кабинет
6. test_input_from_reg_form - вход через форму регистрации
7. test_out_from_personal_account - выход через личный кабинет
8. test_reg - регистрация нового пользователя
9. test_transition - переключение между разделами: соусы, булки, начинки
10. test_transition_designer - переход по клику на Конструктор
11. test_transition_stellarburgers - переход по клику на логотип Stellar Burgers