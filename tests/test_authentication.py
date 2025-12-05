from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import Locators
from data.data import UsersTestData


class TestAuthentication:
    # Вход по кнопке «Войти в аккаунт» на главной
    def test_authentication_by_button_login_in_main_page_success(self, driver):
        driver.find_element(*Locators.button_login_in_main).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            Locators.button_register))
        
        email_element = driver.find_element(*Locators.input_email_auth)
        password_element = driver.find_element(*Locators.input_password_auth)
        login_button = driver.find_element(*Locators.button_login)
        make_order_button = Locators.button_make_the_order

        email_element.send_keys(UsersTestData.email)
        password_element.send_keys(UsersTestData.password)
        login_button_element = driver.find_element(*Locators.button_login)
        login_button_element.click()

        # Ожидание появления кнопки "Сделать заказ"
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(make_order_button))
        
        # Ассерты с поиском элемента внутри
        assert driver.find_element(*make_order_button).is_displayed()

class TestAuthentication:
    # Вход через кнопку в форме регистрации
    def test_authentication_by_button_login_in_registration_form_success(self, driver):
        driver.find_element(*Locators.button_login_in_main).click()
        driver.find_element(*Locators.button_register).click()
        driver.find_element(*Locators.button_login_in_registration_form).click()
        driver.find_element(*Locators.input_email_auth).send_keys(UsersTestData.email)
        driver.find_element(*Locators.input_password_auth).send_keys(UsersTestData.password)
        driver.find_element(*Locators.button_login).click()
        
        assert WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located(Locators.button_make_the_order)
        ).is_displayed()
        
    # Вход через кнопку «Личный кабинет»
    def test_authentication_by_button_personal_account_in_main_page_success(self, driver):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.button_register))
        driver.find_element(*Locators.input_email_auth).send_keys(UsersTestData.email)
        driver.find_element(*Locators.input_password_auth).send_keys(UsersTestData.password)
        driver.find_element(*Locators.button_login).click()
        # Переносим ожидание и поиск внутрь ассерта
        assert WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located(Locators.button_make_the_order)
        ) and driver.find_element(*Locators.button_make_the_order).is_displayed()

    # Вход через кнопку в форме регистрации
    def test_authentication_by_button_login_in_registration_form_success(self, driver):
        driver.find_element(*Locators.button_login_in_main).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.button_register))
        driver.find_element(*Locators.button_register).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.button_submit))
        driver.find_element(*Locators.button_login_in_registration_form).click()
        driver.find_element