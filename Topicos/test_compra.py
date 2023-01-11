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
        self.loginField.send_keys('standard_user')
        self.passwdField.send_keys('secret_sauce')
        self.loginButton.click()


        self.addToCartButton = self.driver.find_element(By.CLASS_NAME, 'btn btn_primary btn_small btn_inventory')
        self.addToCartButton.click()

        self.goToCartButton = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
        self.goToCartButton.click()
        
        self.checkoutButton = self.driver.find_element(By.ID, 'checkout')
        self.checkoutButton.click()

        self.firstNameField = self.driver.find_element(By.ID, 'first-name')
        self.lastNameField = self.driver.find_element(By.ID, 'last-name')
        self.postalCodeField = self.driver.find_element(By.ID, 'postal-code')
        self.continueButton = self.driver.find_element(By.ID, 'continue')
        self.firstNameField.send_keys('Your')
        self.lastNameField.send_keys('Mom')
        self.postalCodeField.send_keys('Your')
        self.continueButton.click()



        return super().setUp()

    def test_checkout_success(self):


        label_product = self.driver.find_element(By.CLASS_NAME, 'title')
        self.assertEqual('PRODUCTS', label_product.text)

        self.driver.quit()


    def tearDown(self) -> None:
        # self.driver.quit()
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
