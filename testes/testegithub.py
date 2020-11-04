from selenium.webdriver import Firefox

browser = Firefox()
url = 'file:///home/balbino/git/pysite/frontend/index.html'
browser.get(url)

a = browser.find_element_by_css_selector('[class="rede-social"]')
github = a.find_element_by_css_selector('[href="https://github.com/pyladiespb-org"]')
github.click()

browser.quit()


"""
Código de teste do botão Github
"""
