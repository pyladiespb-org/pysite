from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
url = 'file:///home/balbino/git/pysite/frontend/perfis.html'
browser.get(url)

def habilidades(browser):
    select = browser.find_element_by_xpath('//*[@id="interface"]/div[1]/div[1]/table/tbody/tr/td[1]/select')
    select.click()
    habilidade = select.find_element_by_css_selector('[value="14"]').click()
    lupa = browser.find_element_by_xpath('//*[@id="interface"]/div[1]/div[1]/table/tbody/tr/td[2]/a/i')
    sleep(0.5)
    lupa.click()



def main():
    habilidades(browser)


if __name__ == '__main__':
    main()


#browser.quit()
