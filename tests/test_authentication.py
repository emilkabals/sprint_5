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
        driver.find_element(*Locators.input_email_auth).send_keys(UsersTestData.email)
        driver.find_element(*Locators.input_password_auth).send_keys(UsersTestData.password)
        driver.find_element(*Locators.button_login).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            Locators.button_make_the_order))
        assert driver.find_element(*Locators.button_make_the_order).is_displayed()

    # Вход через кнопку «Личный кабинет»
    def test_authentication_by_button_personal_account_in_main_page_success(self, driver):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.button_register))
        driver.find_element(*Locators.input_email_auth).send_keys(UsersTestData.email)
        driver.find_element(*Locators.input_password_auth).send_keys(UsersTestData.password)
        driver.find_element(*Locators.button_login).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            Locators.button_make_the_order))
        assert driver.find_element(*Locators.button_make_the_order).is_displayed()

    # Вход через кнопку в форме регистрации
    def test_authentication_by_button_login_in_registration_form_success(self, driver):
        driver.find_element(*Locators.button_login_in_main).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.button_register))
        driver.find_element(*Locators.button_register).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.button_submit))
        driver.find_element(*Locators.button_login_in_registration_form).click()
        driver.find_element(*Locators.input_email_auth).send_keys(UsersTestData.email)
        driver.find_element(*Locators.input_password_auth).send_keys(UsersTestData.password)
        driver.find_element(*Locators.button_login).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            Locators.button_make_the_order))
        assert driver.find_element(*Locators.button_make_the_order).is_displayed()

    # Вход через кнопку в форме восстановления пароля
    def test_authentication_by_button_forgot_password_in_auth_form_success(self, driver):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.button_register))
        driver.find_element(*Locators.button_forgot_password).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            Locators.button_login_passwd_recovery_form))
        driver.find_element(*Locators.button_login_passwd_recovery_form).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.button_register))
        driver.find_element(*Locators.input_email_auth).send_keys(UsersTestData.email)
        driver.find_element(*Locators.input_password_auth).send_keys(UsersTestData.password)
        driver.find_element(*Locators.button_login).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            Locators.button_make_the_order))
        assert driver.find_element(*Locators.button_make_the_order).is_displayed()