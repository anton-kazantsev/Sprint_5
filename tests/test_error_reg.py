from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarLocators
from conftest import driver
from email_gen import EmailGeniration
class TestErrorPass:
    def test_error_pass(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, StellarLocators.INPUT_ACCOUNT).click() # Войти в аккаунт на главной странице
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.AUTH_LOGIN))) # Ожидание открытия личного кабинета

        # Регистрация нового пользователя
        driver.find_element(By.LINK_TEXT, StellarLocators.REG).click()
        driver.find_element(By.XPATH, StellarLocators.NAME_REG).send_keys('Антон')
        driver.find_element(By.XPATH, StellarLocators.EMAIL_REG).send_keys(EmailGeniration.email_generation())
        driver.find_element(By.XPATH, StellarLocators.PASS_REG).send_keys('12345')
        driver.find_element(By.XPATH, StellarLocators.BUT_REG).click()
        error_pass = driver.find_element(By.XPATH, StellarLocators.ERROR_PASS)
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/register" and error_pass.text == "Некорректный пароль"