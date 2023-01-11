from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://google.com/')
driver.find_element(By.ID, 'id')
