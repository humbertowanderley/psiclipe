from selenium import webdriver
from bs4 import BeautifulSoup

def search_link_music(browser, music_name):
    letras_url = 'https://www.letras.mus.br/'
    search_part = '?q=' + music_name
    browser.get(letras_url + search_part)
    search_html = browser.page_source
    res = BeautifulSoup(search_html,"html.parser")
    link = res.find('a',{'class': 'gs-title'})
    return link.get('data-ctorig')
    
def get_id_mus(browser,url):
    browser.get(url)
    search_html = browser.page_source
    res = BeautifulSoup(search_html,"html.parser")
    link = res.find(id="js-scripts")
    scrpt = link.script.text
    pos_ini = scrpt.find('{"ID":')
    pos_ini += 6
    pos_fim = scrpt.find(',"URL"')
    mus_id = scrpt[pos_ini:pos_fim]
    youtube_id_ini = scrpt.find('YoutubeID":"')
    youtube_id_ini += 12
    youtube_id_fim = scrpt.find('","StartSeconds')
    youtube_id = scrpt[youtube_id_ini:youtube_id_fim]

    return [mus_id,youtube_id]

def check_has_subtitle(browser, id_mus):
    url_subtitle = 'https://m.letras.mus.br/subtitle/'
    browser.get(url_subtitle + id_mus)
    search_html = browser.page_source
    res = BeautifulSoup(search_html,"html.parser")
    arr = res.body.pre.text
    if arr.split()[0] == 'null':
        return None
    else:
        arr1 = arr[2:].split('","')
        arr1[len(arr1)-1] = arr1[len(arr1)-1][0:arr1[len(arr1)-1].find('"]')]
        return arr1

def get_cync_lyric_arr(browser, id_mus, arr_sib):
    if arr_sib is None:
        return None
    else:
        for ar in arr_sib:
            url = 'https://m.letras.mus.br/subtitle/' + id_mus + '/' + ar
            lyric = get_cync_lyric(browser, url)
            if lyric is not None:
                return lyric
        return None

def get_cync_lyric(browser, url):
    browser.get(url)
    search_html = browser.page_source
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

#funcao que a entrada e o nome da musica digitado, e, 
#a saida e o link do video para o download e array da letra com o timestamp
def get_lyric_videoLink(text_music_name):
    browser = webdriver.Chrome()

    link_music_letras = search_link_music(browser, text_music_name)
    id_mus_vid = get_id_mus(browser, link_music_letras)
    id_lyric_arr = check_has_subtitle(browser, id_mus_vid[0])
    if id_lyric_arr is None:
        return None
    lyric_sync = get_cync_lyric_arr(browser, id_mus_vid[0], id_lyric_arr)
    youtube_link = "https://www.youtube.com/watch?v=" + id_mus_vid[1]

    browser.quit()

    return [youtube_link,lyric_sync]
