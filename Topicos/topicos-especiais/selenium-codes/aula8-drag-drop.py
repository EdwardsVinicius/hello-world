from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get('http://the-internet.herokuapp.com/drag_and_drop')

element = driver.find_element(By.ID, 'column-a')
target = driver.find_element(By.ID, 'column-b')

action_chains = webdriver.ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()
