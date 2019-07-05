#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
import ast
    
def get_id_mus(url):
    code = requests.get(url)
    plain = code.text
    res = BeautifulSoup(plain, "html.parser")

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

# def check_has_subtitle(id_mus):
#     url_subtitle = 'https://m.letras.mus.br/subtitle/'
#     code = requests.get(url_subtitle + id_mus)
#     plain = code.text
#     res = BeautifulSoup(plain, "html.parser")
    
#     arr = res.text
#     if arr.split()[0] == 'null':
#         return None
#     else:
#         arr1 = arr[2:].split('","')
#         arr1[len(arr1)-1] = arr1[len(arr1)-1][0:arr1[len(arr1)-1].find('"]')]
#         return arr1

# def get_cync_lyric_arr(id_mus, arr_sib):
#     if arr_sib is None:
#         return None
#     else:
#         url = 'https://m.letras.mus.br/subtitle/' + id_mus + '/' + arr_sib
#         lyric = get_cync_lyric(url)
#         if lyric is not None:
#             return lyric
#         return None

def get_cync_lyric(id_mus,id_vid):

    url = 'https://m.letras.mus.br/subtitle/' + id_mus + '/' + id_vid

    code = requests.get(url)
    
    json_code = code.json()
    json_code = json_code['Original']

    json_code['Subtitle'] = change_subtitle_json(json_code['Subtitle'])
    # print json_code['SongID']

    # plain = code.text
    # res = BeautifulSoup(plain, "html.parser")

    # res_text = res.text
    # res_text_subtitle_ini = res_text.find('"Subtitle":"')
    # res_text_subtitle_ini += 12
    # res_text_subtitle_fim = res_text.find('","VideoID"')
    # res_text_subtitle = res_text[res_text_subtitle_ini:res_text_subtitle_fim]
    
    # res_text_subtitle_stretch = res_text_subtitle[2:].split('],[')
    # res_text_subtitle_stretch[len(res_text_subtitle_stretch)-1] = res_text_subtitle_stretch[len(res_text_subtitle_stretch)-1][0:(res_text_subtitle_stretch[len(res_text_subtitle_stretch)-1].find(']]'))]

    # lyric_struct = []

    # for res_stretch in res_text_subtitle_stretch:
    #     temp = res_stretch.split('\\"')
    #     temp1 = [temp[1],temp[3],temp[5]]
    #     lyric_struct.append(temp1)
        
    return json_code

#funcao que a entrada e o nome da musica e do artista digitado, e, 
#a saida e o link do video para o download e array da letra com o timestamp
def get_lyric_videoLink(text_music_name,text_artist_name):
    id_mus_vid = get_id_mus('https://www.letras.mus.br/'+ text_artist_name.replace(" ", "-") + '/' + text_music_name.replace(" ", "-") + '/')
    # id_lyric_arr = check_has_subtitle(id_mus_vid[0])
    # if id_lyric_arr is None:
    #     return None
    json_mus = get_cync_lyric(id_mus_vid[0], id_mus_vid[1])
    # youtube_link = "https://www.youtube.com/watch?v=" + id_mus_vid[1]
    return json_mus

def change_subtitle_json(sub):
    subt = ast.literal_eval(sub)
    
    subtitle = []

    index = 0
    for line in subt:
        subtitle_line = {
            "Index": index,
            "Lyric": line[0],
            "Begin": float(line[1]),
            "End": float(line[2]),
            "Image": None,
            "ImageDeepDream": None
        }
        subtitle.append(subtitle_line)
        index+=1

    return subtitle