import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from data.data import UsersTestData

class Locators:
    button_login_in_main = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    input_email_auth = (By.XPATH, "//input[@name='name']")
    input_password_auth = (By.XPATH, "//input[@name='Пароль']")
    button_login = (By.XPATH, "//button[contains(text(),'Войти')]")

@pytest.fixture(scope="function")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*Locators.button_login_in_main).click()
    driver.find_element(*Locators.input_email_auth).send_keys(UsersTestData.email)
    driver.find_element(*Locators.input_password_auth).send_keys(UsersTestData.password)
    driver.find_element(*Locators.button_login).click()

