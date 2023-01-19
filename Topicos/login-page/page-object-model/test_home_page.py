import unittest

from selenium.webdriver import Firefox

from pages.swag_home_page import HomePage


class TestSwagLabsHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = Firefox()
        self.home_page = HomePage(self.driver)

    # def test_search_info(self):
    #     self.home_page.search_info("zona franca de manaus")
    #     resultado_obtido = self.home_page.get_title()
    #     self.assertIn('zona', resultado_obtido)

    def test_valid_login(self):
        self.home_page.login_info('standard_user', 'secret_sauce')
        url = self.home_page.get_url()
        self.assertIn('inventory', url)

    def test_locked_out_user(self):
        self.home_page.login_info('locked_out_user', 'secret_sauce')
        message = self.home_page.get_error_message()
        self.assertEqual('Epic sadface: Sorry, this user has been locked out.', message)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
