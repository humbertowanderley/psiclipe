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

def get_cync_lyric(id_mus,id_vid):

    url = 'https://m.letras.mus.br/subtitle/' + id_mus + '/' + id_vid

    code = requests.get(url)
    
    json_code = code.json()
    json_code = json_code['Original']

    json_code['Subtitle'] = change_subtitle_json(json_code['Subtitle'])
        
    return json_code

#funcao que a entrada e o nome da musica e do artista digitado, e, 
#a saida e o link do video para o download e array da letra com o timestamp
def get_lyric_videoLink(text_music_name,text_artist_name):
    id_mus_vid = get_id_mus('https://www.letras.mus.br/'+ text_artist_name.replace(" ", "-") + '/' + text_music_name.replace(" ", "-") + '/')
    json_mus = get_cync_lyric(id_mus_vid[0], id_mus_vid[1])
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