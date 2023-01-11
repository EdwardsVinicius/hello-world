import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.saucedemo.com/')

        self.loginField = self.driver.find_element(By.ID, 'user-name')
        self.passwdField = self.driver.find_element(By.ID, 'password')
        self.loginButton = self.driver.find_element(By.ID, 'login-button')
        return super().setUp()

    # def test_valid_login(self):
    #     self.loginField.send_keys('standard_user')
    #     self.passwdField.send_keys('secret_sauce')

    #     self.loginButton.click()

    #     label_product = self.driver.find_element(By.CLASS_NAME, 'title')
    #     self.assertEqual('PRODUCTS', label_product.text)

    #     self.driver.quit()

    def test_locked_out_user(self):
        self.loginField.send_keys('locked_out_user')
        self.passwdField.send_keys('secret_sauce')

        self.loginButton.click()

        message = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3')
        self.assertEqual('Epic sadface: Sorry, this user has been locked out.', message.text)

        self.driver.quit()

    def test_problem_user(self):
        self.loginField.send_keys('problem_user')
        self.passwdField.send_keys('secret_sauce')

        self.loginButton.click()

        label_product = self.driver.find_element(By.CLASS_NAME, 'title')
        self.assertEqual('PRODUCTS', label_product.text)

        self.driver.quit()

    def test_performance_glitch_user(self):
        self.loginField.send_keys('performance_glitch_user')
        self.passwdField.send_keys('secret_sauce')

        self.loginButton.click()

        label_product = self.driver.find_element(By.CLASS_NAME, 'title')
        self.assertEqual('PRODUCTS', label_product.text)

        self.driver.quit()

    # def test_empty_passwd(self):
    #     self.loginField.send_keys('problem_user')
    #     self.passwdField.send_keys('')

    #     self.loginButton.click()

    #     message = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3')
    #     self.assertEqual('Epic sadface: Password is required', message.text)

    #     self.driver.quit()

    # def test_error_passwd(self):
    #     self.loginField.send_keys('problem_user')
    #     self.passwdField.send_keys('not_so_secret_sauce')

    #     self.loginButton.click()

    #     message = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3')
    #     self.assertEqual('Epic sadface: Username and password do not match any user in this service', message.text)

    #     self.driver.quit()

    # def test_empty_login(self):
    #     self.loginField.send_keys('')
    #     self.passwdField.send_keys('secret_sauce')

    #     self.loginButton.click()

    #     message = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3')
    #     self.assertEqual('Epic sadface: Username is required', message.text)

    #     self.driver.quit()

    # def test_error_login(self):
    #     self.loginField.send_keys('wrong_user')
    #     self.passwdField.send_keys('secret_sauce')

    #     self.loginButton.click()

    #     message = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3')
    #     self.assertEqual('Epic sadface: Username and password do not match any user in this service', message.text)

    #     self.driver.quit()


    def tearDown(self) -> None:
        # self.driver.quit()
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
