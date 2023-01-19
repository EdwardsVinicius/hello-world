import unittest

from selenium.webdriver import Firefox

from pages.duck_home_page import HomePage


class TestDuckHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = Firefox()
        self.home_page = HomePage(self.driver)

    def test_search_info(self):
        self.home_page.search_info("instituto flexpeak")
        resultado_obtido = self.home_page.get_title()
        self.assertIn('flexpeak', resultado_obtido)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
