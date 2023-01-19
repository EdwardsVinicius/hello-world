from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

url = 'https://selenium.dunossauro.live/keyboard'

browser = Firefox()

browser.get(url)

html = browser.find_element(By.TAG_NAME, 'html')

html.send_keys('Selenium')
