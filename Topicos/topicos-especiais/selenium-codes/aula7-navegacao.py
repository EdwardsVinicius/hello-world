from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com")

campo_login = driver.find_element(By.ID, 'user-name')
campo_password = driver.find_element(By.ID, 'password')
login = driver.find_element(By.ID, 'login-button')

campo_login.send_keys('standard_user')
campo_password.send_keys('secret_sauce')
login.click()


# lista_opcoes = driver.find_element(By.CLASS_NAME, 'product_sort_container')
select = Select(driver.find_element(
    By.CLASS_NAME, 'product_sort_container'))
# select.select_by_value('lohi')
# select.select_by_visible_text('Price (low to high)')
# select.select_by_index(2)
# mais_barato = driver.find_element(
#     By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button')
# mais_barato.click()

# # select.select_by_index(2)
# # sleep(5)
# # select.select_by_visible_text("Name (A to Z)")
# # sleep(5)
# # select.select_by_value('lohi')
# # sleep(5)


# # driver.quit()
