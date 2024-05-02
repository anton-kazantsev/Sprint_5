from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarLocators
from conftest import driver

class TestOutForm:
    def test_out_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.LINK_TEXT, StellarLocators.PA_BUTTON).click() # Переход в личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.AUTH_LOGIN))) # Ожидание открытия личного кабинета

        # Ввод данных для входа
        driver.find_element(By.XPATH, StellarLocators.INPUT_EMAIL).send_keys("antonkazantsev05@yandex.ru")
        driver.find_element(By.XPATH, StellarLocators.INPUT_PASSWORD).send_keys("123456")
        driver.find_element(By.XPATH, StellarLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.INPUT_MAIN))) # Ожидание открытия главной страницы

        driver.find_element(By.LINK_TEXT, StellarLocators.PA_BUTTON).click() # Переход в личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.ACCOUNT_LOGIN))) # Ожидание открытия личного кабинета

        driver.find_element(By.XPATH, StellarLocators.OUT).click() # Выход из личного кабинета
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.AUTH_LOGIN)))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"