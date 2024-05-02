from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import StellarLocators
from conftest import driver

class TestTransition:
    def test_to_rolls(self, driver):
        # Переход на сайт
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, StellarLocators.SAUCES).click()
        driver.find_element(By.XPATH, StellarLocators.ROLLS).click()
        element = driver.find_element(By.XPATH, StellarLocators.HEAD_ROLLS)
        assert element.text == "Булки"

    def test_to_sauces(self, driver):
        # Переход на сайт
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, StellarLocators.SAUCES).click()
        element = driver.find_element(By.XPATH, StellarLocators.HEAD_SAUCES)
        assert element.text == "Соусы"

    def test_to_fillings(self, driver):
        # Переход на сайт
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, StellarLocators.FILLINGS).click()
        element = driver.find_element(By.XPATH, StellarLocators.HEAD_FILLINGS)
        assert  element.text == "Начинки"