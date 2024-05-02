from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarLocators
from conftest import driver

class TestReg:
    def test_reg(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, StellarLocators.INPUT_ACCOUNT).click() # Войти в аккаунт на главной странице
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.AUTH_LOGIN))) # Ожидание открытия личного кабинета

        # Регистрация нового пользователя
        driver.find_element(By.LINK_TEXT, StellarLocators.REG).click()
        driver.find_element(By.XPATH, StellarLocators.NAME_REG).send_keys('Антон')
        driver.find_element(By.XPATH, StellarLocators.EMAIL_REG).send_keys('antonkazantsev05@yandex.ru')
        driver.find_element(By.XPATH, StellarLocators.PASS_REG).send_keys('123456')
        driver.find_element(By.XPATH, StellarLocators.BUT_REG).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.AUTH_LOGIN)))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/register"