from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
url = 'file:///home/balbino/git/pysite/frontend/pyladiesday.html'
browser.get(url)


ul = browser.find_element_by_css_selector('[type="disc"]')
sobre = ul.find_element_by_tag_name('[href="sobre.html"]')
sobre.click()

browser.quit()

"""
Código de teste do botão Sobre
"""
