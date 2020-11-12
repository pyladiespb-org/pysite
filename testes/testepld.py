from selenium.webdriver import Firefox

browser = Firefox()
url = 'file:///home/balbino/git/pysite/frontend/pyladiesday.html'
browser.get(url)

ul = browser.find_element_by_css_selector('[type="disc"]')
pdl = ul.find_element_by_tag_name('[href="pyladiesday.html"]')
pdl.click()

browser.quit()

"""
Código de teste do botão Pyladies Day
"""
