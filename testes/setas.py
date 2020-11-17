from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
url = 'file:///home/balbino/git/pysite/frontend/eventos.html'
browser.get(url)

lista_slides = ['[for="slide2"]', '[for="slide3"]',
'[for="slide4"]', '[for="slide5"]', '[for="slide6"]', '[for="slide7"]',
'[for="slide8"]', '[for="slide9"]', '[for="slide10"]', '[for="slide11"]',
'[for="slide12"]', '[for="slide1"]']


def clica_setas(browser):
    id = browser.find_element_by_id('controls')
    for slide in lista_slides:
        sleep(0.5)
        label = id.find_element_by_css_selector(slide)
        sleep(0.5)
        label.click()


def main():
    clica_setas(browser)

if __name__ == '__main__':
    main()
