from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class ProcedimentoTesteLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.saucedemo.com/')

    def test_valid_login(self):
        campo_login = self.driver.find_element(By.ID, 'user-name')
        campo_pass = self.driver.find_element(By.ID, 'password')
        login_button = self.driver.find_element(By.ID, 'login-button')

        # ENTRADA
        campo_login.send_keys('standard_user')
        campo_pass.send_keys('secret_sauce')
        login_button.click()

        label_product = self.driver.find_element(By.CLASS_NAME, 'title')

        self.assertEqual('PRODUCTS', label_product.text)

    def test_problem_user(self):

        campo_login = self.driver.find_element(By.ID, 'user-name')
        campo_pass = self.driver.find_element(By.ID, 'password')
        login_button = self.driver.find_element(By.ID, 'login-button')

        # ENTRADA
        campo_login.send_keys('problem_user')
        campo_pass.send_keys('secret_sauce')
        login_button.click()

        label_product = self.driver.find_element(By.CLASS_NAME, 'title')

        self.assertEqual('PRODUCTS', label_product.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
