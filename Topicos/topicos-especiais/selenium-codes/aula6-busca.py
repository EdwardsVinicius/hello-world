from functools import partial
from gettext import find
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


from time import sleep


driver = webdriver.Firefox()
driver.get("http://automationpractice.com/")
campo_busca = driver.find_element(By.ID, 'search_query_top')
campo_busca.send_keys('Blouse')
pesquisar = driver.find_element(By.NAME, 'submit_search')
pesquisar.click()


sleep(2)
mensagem = driver.find_element(
    By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/h5/a')
if (mensagem.text == 'Blouse'):
    print('Sucesso')
else:
    print('Falha')

driver.quit()
