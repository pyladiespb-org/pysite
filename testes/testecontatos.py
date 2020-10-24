from selenium.webdriver import Firefox

browser = Firefox()
url = 'file:///home/balbino/git/pysite/frontend/pyladiesday.html'
browser.get(url)

ul = browser.find_element_by_css_selector('[type="disc"]')
contatos = ul.find_element_by_tag_name('[href="contatos.html"]')
contatos.click()

browser.quit()

"""
Código de teste do botão Contatos
"""
