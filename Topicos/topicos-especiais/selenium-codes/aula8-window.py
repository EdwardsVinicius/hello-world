from os import link
from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/abtest")


link = driver.find_element(By.LINK_TEXT, 'Elemental Selenium')
link.click()

# for handle in driver.window_handles:
#     driver.switch_to.window(handle)
#     print('Mudei de janela')
