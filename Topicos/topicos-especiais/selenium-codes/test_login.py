import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class ProcedimentoTesteLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.saucedemo.com/")

    def test_login_invalido(self):
        campo_login = self.driver.find_element(By.ID, 'user-name')
        campo_password = self.driver.find_element(By.ID, 'password')
        login = self.driver.find_element(By.ID, 'login-button')

        # ENTRADA
        campo_login.send_keys('user')
        campo_password.send_keys('secret_sauce')
        login.click()
        # SAIDA ESPERADA
        # texto_erro = 'Epic sadface: Username and password do not match any user in this service'
        elemento_erro = self.driver.find_element(
            By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        self.assertTrue(elemento_erro.is_displayed())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
