from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import Locators


class TestNavigationToConstructor:
    # Проверка перехода из ЛК по клику на «Конструктор»
    def test_navigate_from_personal_account_to_constructor_by_header_success(self, driver, login):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.profile))
        driver.find_element(*Locators.header_of_page_constructor).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            Locators.button_make_the_order))
        assert driver.find_element(*Locators.button_make_the_order).is_displayed()

    # Проверка перехода из ЛК по клику на лого
    def test_navigate_from_personal_account_to_constructor_by_logo_success(self, driver, login):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.profile))
        driver.find_element(*Locators.logo).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            Locators.button_make_the_order))
        assert driver.find_element(*Locators.button_make_the_order).is_displayed()