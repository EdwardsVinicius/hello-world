
from selenium.webdriver.common.by import By


class GooglePageLocators():
    search_field = (By.NAME, 'q')
    search_button = (By.NAME, 'btnK')


class DuckGoPageLocators():
    search_field = (By.ID, 'search_form_input_homepage')
    search_button = (By.ID, 'search_button_homepage')
