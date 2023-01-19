
from pages.base_page import BasePage
from resources.locators import SwagLabsLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://saucedemo.com/')

    def login_info(self, user, pwd):
        self.enter_text(SwagLabsLocators.login_field, user)
        self.enter_text(SwagLabsLocators.password_field, pwd)
        
        self.click(SwagLabsLocators.button_login)
