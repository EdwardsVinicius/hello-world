from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
browser.get('https://curso-python-selenium.netlify.app/aula_03.html')
sleep(2)
# elemento = browser.find_element_by_tag_name('a')
elemento = browser.find_element('tag name', 'a')

for click in range(1, 11):
    elemento.click()
    paragrafo = browser.find_elements('tag name', 'p')
    print('Valor do paragrafo', paragrafo[-1].text)

browser.quit()
