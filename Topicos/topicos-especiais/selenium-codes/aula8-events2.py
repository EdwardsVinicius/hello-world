from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import (
    ActionChains
)
from selenium.webdriver.common.keys import Keys

url = 'https://selenium.dunossauro.live/aula_08_a'
texto = 'Flexpeak'

browser = Firefox()
browser.get(url)

# hi-level
elemento = browser.find_element(By.NAME, 'texto')
# elemento.send_keys()

# low-level
ac = ActionChains(browser)
ac.move_to_element(elemento)
ac.click(elemento)


for letra in texto:
    ac.key_down(Keys.SHIFT)
    ac.key_down(letra)
    ac.key_up(letra)
    ac.key_up(Keys.SHIFT)

ac.perform()


# digita_com(Keys.SHIFT)
# digita_com(Keys.CAPS)


# ac.perform()
