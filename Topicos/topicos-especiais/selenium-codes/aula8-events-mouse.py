from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


url = 'https://selenium.dunossauro.live/caixinha'
browser = Firefox()
browser.get(url)
ac = ActionChains(browser)

# BUSCANDO OS ELEMENTOS
caixinha = browser.find_element(By.ID, 'caixa')
span = browser.find_element(By.ID, 'area')


ac.key_down(Keys.CONTROL)
ac.move_to_element(caixinha)
ac.click()
ac.key_up(Keys.CONTROL)
ac.move_to_element(span)
ac.pause(1)


ac.key_down(Keys.CONTROL)
ac.key_down(Keys.SHIFT)
ac.move_to_element(caixinha)
ac.click()
ac.key_up(Keys.CONTROL)
ac.key_up(Keys.SHIFT)
ac.move_to_element(span)
ac.pause(1)


ac.move_to_element(caixinha)
ac.double_click()
ac.context_click()
ac.pause(1)

ac.perform()
