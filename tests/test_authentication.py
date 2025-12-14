from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import Locators
from data.data import UsersTestData


class TestAuthentication:
    def test_authentication_by_button_login_in_main_page_success(self, driver):
        # ARRANGE: Подготовка (минимальная)
        email = UsersTestData.VALID_USER['email']
        password = UsersTestData.VALID_USER['password']
        
        # исправления в коде: Действия (прямые и лаконичные)
        driver.find_element(*Locators.button_login_in_main).click()
        driver.find_element(*Locators.input_email_auth).send_keys(email)
        driver.find_element(*Locators.input_password_auth).send_keys(password)
        driver.find_element(*Locators.button_login).click()
        
        # перенос в ASSERT: Проверка (с ожиданием ВНУТРИ assert)
        assert WebDriverWait(driver, 6).until(
            EC.visibility_of_element_located(Locators.button_make_the_order)
        ).is_displayed()

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
        
class TestAuthentication:
    # Вход через кнопку «Личный кабинет»
    def test_authentication_by_button_personal_account_in_main_page_success(self, driver):
        # измененный код
        driver.find_element(*Locators.button_personal_account).click()
        driver.find_element(*Locators.input_email_auth).send_keys(UsersTestData.VALID_USER['email'])
        driver.find_element(*Locators.input_password_auth).send_keys(UsersTestData.VALID_USER['password'])
        driver.find_element(*Locators.button_login).click()
        
        # ASSERT (исправлено)
        assert WebDriverWait(driver, UsersTestData.TIMEOUTS['medium']).until(
            EC.visibility_of_element_located(Locators.button_make_the_order)
        )  # WebDriverWait.until() уже возвращает элемент или бросает исключение

    # Вход через кнопку в форме регистрации  
    def test_authentication_by_button_login_in_registration_form_success(self, driver):
        # измененный код
        driver.find_element(*Locators.button_login_in_main).click()
        driver.find_element(*Locators.button_register).click()
        driver.find_element(*Locators.button_login_in_registration_form).click()
        driver.find_element(*Locators.input_email_auth).send_keys(UsersTestData.VALID_USER['email'])
        driver.find_element(*Locators.input_password_auth).send_keys(UsersTestData.VALID_USER['password'])
        driver.find_element(*Locators.button_login).click()
        
        # ASSERT
        assert WebDriverWait(driver, UsersTestData.TIMEOUTS['medium']).until(
            EC.visibility_of_element_located(Locators.button_make_the_order)
        )