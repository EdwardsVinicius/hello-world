
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'https://selenium.dunossauro.live/aula_09_a.html'
firefox = Firefox()
firefox.get(url)
wait = WebDriverWait(firefox, 10)
element = wait.until(EC.element_to_be_clickable(
    firefox.find_elements(By.ID, 'request')))
element.click()

# suecsso = firefox.find_element(By.CSS_SELECTOR, '#finished')
# assert suecsso.text == 'Carregamento concluído'
# suecsso = firefox.find_element(By.CSS_SELECTOR, 'corinthians')
