from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarLocators
from conftest import driver

class TestTransitionDesigner:
    def test_transition_designer(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, StellarLocators.INPUT_ACCOUNT).click() # Войти в аккаунт на главной странице
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.AUTH_LOGIN))) # Ожидание открытия личного кабинета

        # Ввод данных для входа
        driver.find_element(By.XPATH, StellarLocators.INPUT_EMAIL).send_keys("antonkazantsev05@yandex.ru")
        driver.find_element(By.XPATH, StellarLocators.INPUT_PASSWORD).send_keys("123456")
        driver.find_element(By.XPATH, StellarLocators.ENTER_BUTTON).click() # Нажатие на кнопку Войти
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.MAIN_PAGE))) # Ожидание перехода на главную страницу

        driver.find_element(By.LINK_TEXT, StellarLocators.PA_BUTTON).click() # Переход в личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.ACCOUNT_LIST))) # Ожидание открытия личного кабинета

        driver.find_element(By.XPATH, StellarLocators.CONSTRUCT_BUTTON).click() # Кнопка Конструктор
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.MAIN_PAGE))) # Ожидание перехода на главную страницу

        assert expected_conditions.visibility_of_element_located((By.XPATH, StellarLocators.INPUT_ACCOUNT))
