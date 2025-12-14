from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import Locators


class TestNavigateToPersonalAccount:
    # Проверка перехода из конструктора бургеров в личный кабинет
    def test_navigate_from_constructor_to_personal_account(self, driver, login):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.profile))
        assert driver.find_element(*Locators.order_history).is_displayed()