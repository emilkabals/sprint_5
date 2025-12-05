from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import Locators
from conftest import driver, login
from data.data import UsersTestData  # Импортируем тестовые данные


class TestLogout:
    # вход по кнопке «Войти в аккаунт»
    def test_logout_of_personal_account_success(self, driver, login):
        # Проверяем что авторизация прошла успешно
        assert WebDriverWait(driver, 6).until(
            EC.visibility_of_element_located(Locators.button_make_the_order)
        ).is_displayed()
        
        # Переходим в личный кабинет
        driver.find_element(*Locators.button_personal_account).click()
        
        # Проверяем что перешли в ЛК
        assert WebDriverWait(driver, 6).until(
            EC.visibility_of_element_located(Locators.profile)
        ).is_displayed()
        
        # Выходим из аккаунта
        driver.find_element(*Locators.button_logout).click()
        
        # Проверяем что вернулись на страницу авторизации
        login_button = WebDriverWait(driver, 6).until(
            EC.visibility_of_element_located(Locators.button_login)
        )
        assert login_button.is_displayed()
        # Можно также проверять текст кнопки из тестовых данных
        assert login_button.text == UsersTestData.login_button_text