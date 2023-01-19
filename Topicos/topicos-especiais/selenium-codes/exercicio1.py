from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.google.com.br")
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("iron maiden")
elem.send_keys(Keys.RETURN)
sleep(8)
driver.close()
