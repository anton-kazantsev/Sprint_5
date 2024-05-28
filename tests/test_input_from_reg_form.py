from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarLocators
from conftest import driver

class TestInputFromRegForm:
    def test_input_from_reg_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, StellarLocators.INPUT_ACCOUNT).click() # Войти в аккаунт на главной странице
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.AUTH_LOGIN))) # Ожидание открытия личного кабинета

        # Войти в аккаунт через форрму регистрации
        driver.find_element(By.LINK_TEXT, StellarLocators.REG).click()
        driver.find_element(By.LINK_TEXT, StellarLocators.TEXT_INPUT).click()

        # Ввод данных для входа
        driver.find_element(By.XPATH, StellarLocators.INPUT_EMAIL).send_keys("antonkazantsev05@yandex.ru")
        driver.find_element(By.XPATH, StellarLocators.INPUT_PASSWORD).send_keys("123456")
        driver.find_element(By.XPATH, StellarLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, StellarLocators.MAIN_PAGE)))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"