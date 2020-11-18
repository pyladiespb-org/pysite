from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
url = 'file:///home/balbino/git/pysite/frontend/perfis.html'
browser.get(url)


def cidade(browser):
    select = browser.find_element_by_xpath('//*[@id="interface"]/div[1]/div[2]/table/tbody/tr/td[1]/select')
    select.click()
    cidade = select.find_element_by_css_selector('[value="João Pessoa"]').click()
    sleep(0.5)
    lupa = browser.find_element_by_xpath('//*[@id="interface"]/div[1]/div[2]/table/tbody/tr/td[2]/a/i').click()


def main():
    cidade(browser)


if __name__ == '__main__':
    main()

#browser.quit()
