from selenium import webdriver
from bs4 import BeautifulSoup

def search_link_music(music_name):
    letras_url = 'https://www.letras.mus.br/'
    search_part = '?q=' + music_name
    browser = webdriver.Chrome()
    browser.get(letras_url + search_part)
    search_html = browser.page_source
    browser.quit()
    res = BeautifulSoup(search_html,"html.parser")
    link = res.find('a',{'class': 'gs-title'})
    return link.get('data-ctorig')
    
print search_link_music('envolvimento')