from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class ProcedimentoTesteCompra(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.saucedemo.com/')
        self.valid_login()

    def valid_login(self):
        campo_login = self.driver.find_element(By.ID, 'user-name')
        campo_pass = self.driver.find_element(By.ID, 'password')
        login_button = self.driver.find_element(By.ID, 'login-button')
        # ENTRADA
        campo_login.send_keys('standard_user')
        campo_pass.send_keys('secret_sauce')
        login_button.click()

    def test_buy_product(self):
        produto = self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-backpack')

        produto.click()

        carrinho = self.driver.find_element(
            By.ID, 'shopping_cart_container')
        carrinho.click()
        sleep(3)

        carrinho = self.driver.find_element(
            By.ID, 'shopping_cart_container')
        carrinho.click()
        sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
