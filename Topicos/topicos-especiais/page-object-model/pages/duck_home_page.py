
from pages.base_page import BasePage
from resources.locators import DuckGoPageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://duckduckgo.com/')

    def search_info(self, info):
        self.enter_text(DuckGoPageLocators.search_field, info)
        self.click(DuckGoPageLocators.search_button)
