from selenium.webdriver import Firefox

browser = Firefox()
url = 'file:///home/balbino/git/pysite/frontend/index.html'
browser.get(url)

a = browser.find_element_by_css_selector('[class="rede-social"]')
instagram = a.find_element_by_css_selector('[href="https://www.instagram.com/pyladiespb/?hl=pt-br"]')
instagram.click()

browser.quit()


"""
Código de teste do botão Instagram
"""
