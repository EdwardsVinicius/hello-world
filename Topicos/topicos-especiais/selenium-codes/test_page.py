import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class ProcedimentoBuscaProduto(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://automationpractice.com/")

    def test_search_no_find_product(self):
        campo_busca = self.driver.find_element(By.ID, 'search_query_top')
        # ENTRADA
        campo_busca.send_keys('Blusa')
        # SAIDA ESPERADA
        mensagem_esperada = 'No results were found for your search "Blusa"'
        pesquisar = self.driver.find_element(By.NAME, 'submit_search')
        pesquisar.click()

        elemento = self.driver.find_element(
            By.XPATH, '//*[@id="center_column"]/p')
        mensagem_obtida = elemento.text
        self.assertEqual(mensagem_esperada, mensagem_obtida)

    def test_search_find_product(self):
        campo_busca = self.driver.find_element(By.ID, 'search_query_top')
        # ENTRADA
        campo_busca.send_keys('Blouse')

        # SAIDA ESPERADA
        mensagem_esperada = 'Blouse'
        pesquisar = self.driver.find_element(By.NAME, 'submit_search')
        pesquisar.click()
        elemento = self.driver.find_element(
            By.XPATH, '/html/body/div/div[2]/div/div[3]/div[2]/ul/li/div/div[2]/h5/a')
        mensagem_obtida = elemento.text
        self.assertEqual(mensagem_esperada, mensagem_obtida)

    def tearDown(self):
        self.driver.quit()


class ProcedimentoBuscaProduto(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://automationpractice.com/")

    def test_search_no_find_product(self):
        campo_busca = self.driver.find_element(By.ID, 'search_query_top')
        # ENTRADA
        campo_busca.send_keys('Blusa')
        # SAIDA ESPERADA
        mensagem_esperada = 'No results were found for your search "Blusa"'
        pesquisar = self.driver.find_element(By.NAME, 'submit_search')
        pesquisar.click()

        elemento = self.driver.find_element(
            By.XPATH, '//*[@id="center_column"]/p')
        mensagem_obtida = elemento.text
        self.assertEqual(mensagem_esperada, mensagem_obtida)

    def test_search_find_product(self):
        campo_busca = self.driver.find_element(By.ID, 'search_query_top')
        # ENTRADA
        campo_busca.send_keys('Blouse')

        # SAIDA ESPERADA
        mensagem_esperada = 'Blouse'
        pesquisar = self.driver.find_element(By.NAME, 'submit_search')
        pesquisar.click()
        elemento = self.driver.find_element(
            By.XPATH, '/html/body/div/div[2]/div/div[3]/div[2]/ul/li/div/div[2]/h5/a')
        mensagem_obtida = elemento.text
        self.assertEqual(mensagem_esperada, mensagem_obtida)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
