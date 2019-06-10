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
    
def get_id_mus(url):
    browser = webdriver.Chrome()
    browser.get(url)
    search_html = browser.page_source
    browser.quit()
    res = BeautifulSoup(search_html,"html.parser")
    link = res.find(id="js-scripts")
    scrpt = link.script.text
    pos_ini = scrpt.find('{"ID":')
    pos_ini += 6
    pos_fim = scrpt.find(',"URL"')
    mus_id = scrpt[pos_ini:pos_fim]
    return mus_id

def check_has_subtitle(id_mus):
    url_subtitle = 'https://m.letras.mus.br/subtitle/'
    browser = webdriver.Chrome()
    browser.get(url_subtitle + id_mus)
    search_html = browser.page_source
    browser.quit()
    res = BeautifulSoup(search_html,"html.parser")
    arr = res.body.pre.text
    if arr.split()[0] == 'null':
        return None
    else:
        arr1 = arr[2:].split('","')
        arr1[len(arr1)-1] = arr1[len(arr1)-1][0:arr1[len(arr1)-1].find('"]')]
        return arr1

def get_cync_lyric_arr(id_mus, arr_sib):
    if arr_sib is None:
        return None
    else:
        for ar in arr_sib:
            url = 'https://m.letras.mus.br/subtitle/' + id_mus + '/' + ar
            lyric = get_cync_lyric(url)
            if lyric is not None:
                return lyric

def get_cync_lyric(url):
    browser = webdriver.Chrome()
    browser.get(url)
    search_html = browser.page_source
    browser.quit()
    res = BeautifulSoup(search_html,"html.parser")
    res_text = res.body.pre.text
    res_text_subtitle_ini = res_text.find('"Subtitle":"')
    res_text_subtitle_ini += 12
    res_text_subtitle_fim = res_text.find('","VideoID"')
    res_text_subtitle = res_text[res_text_subtitle_ini:res_text_subtitle_fim]
    
    res_text_subtitle_stretch = res_text_subtitle[2:].split('],[')
    res_text_subtitle_stretch[len(res_text_subtitle_stretch)-1] = res_text_subtitle_stretch[len(res_text_subtitle_stretch)-1][0:(res_text_subtitle_stretch[len(res_text_subtitle_stretch)-1].find(']]'))]

    lyric_struct = []

    for res_stretch in res_text_subtitle_stretch:
        temp = res_stretch.split('\\"')
        temp1 = [temp[1],temp[3],temp[5]]
        lyric_struct.append(temp1)
        
    return lyric_struct

# print get_cync_lyric_arr(get_id_mus(search_link_music('envolvimento')),check_has_subtitle(get_id_mus(search_link_music('envolvimento'))))