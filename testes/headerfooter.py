from selenium.webdriver import Firefox

browser = Firefox()
url = 'file:///home/balbino/git/pysite/frontend/index.html'
browser.get(url)

# dicionários a serem acessados:

selector_dicionario = {'header': '[type="disc"]',
'footer': '[class="rede-social"]'}

links_header = {'sobre': '[href="sobre.html"]', 'pyladiesday': '[href="pyladiesday.html"]',
'eventos': '[href="eventos.html"]', 'perfis': '[href="perfis.html"]', 'contatos': '[href="#footer"]'}

links_footer = {'linkedin': '[href="https://www.linkedin.com/company/pyladiespb"]',
'github': '[href="https://github.com/pyladiespb-org"]',
'instagram': '[href="https://www.instagram.com/pyladiespb/?hl=pt-br"]'}

# fim dos dicionários

def clica_links(browser, selector, link):
    """
    - browser = a instância do navegador
    - selector = nome do seletor que contem os links que você quer acessar(basta
    acessar pelo 'selector_dicionario')
    - link = link que você quer testar (basta acessar pelo dicionário de links escolhido de acordo
    com o seletor)
    """

    seletor = browser.find_element_by_css_selector(selector)
    link_especifico = seletor.find_element_by_tag_name(link)
    link_especifico.click()

"""
Exemplo (acesssar o link do github no rodape):

clica_links(browser, selector_dicionario['footer'], links_footer['github'])
"""

#browser.quit()
