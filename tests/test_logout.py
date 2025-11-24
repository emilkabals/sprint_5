from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import Locators


class TestLogout:
    # вход по кнопке «Войти в аккаунт»
    def test_logout_of_personal_account_success(self, driver, login):
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            Locators.button_make_the_order))
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.profile))
        driver.find_element(*Locators.button_logout).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.button_login))
        assert driver.find_element(*Locators.button_login).is_displayed()