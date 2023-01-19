
from selenium.webdriver.common.by import By


class SwagLabsLocators():
    login_field = (By.ID, 'user-name')
    password_field = (By.ID, 'password')
    button_login = (By.ID, 'login-button')
    error_message = (By.CSS_SELECTOR, 'h3[data-test=error]')



