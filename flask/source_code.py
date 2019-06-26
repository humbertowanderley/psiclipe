#!/usr/bin/env python
# -*- coding: utf-8 -*-
from search_lyric import get_lyric_videoLink
from download_music import download_song
from get_images import get_lyric_images
from make_video import make_video
#from dream import aux_dream


current_job = "Aguarde..."
done_job = False

def project_structure(text_music_name,text_artist_name):
    global current_job

    current_job = "Buscando link da musica..."
    temp = get_lyric_videoLink(text_music_name,text_artist_name)
    
    if temp is None:
        return 'Nao foi possivel concluir, escolha outra musica.'
    
    youtube_link = temp[0]

    current_job = "Baixando letra da musica"
    lyric = temp[1] 


    current_job = "Baixando musica"
    download_song(youtube_link)

    current_job = "Baixando imagens"
    image_timestamp = get_lyric_images(lyric)

    #image_timestamp = [['/code/flask/imagens/34 1.0_2.jpg', 167.9, 169.8],['/code/flask/imagens/35 1.reunion-800.jpg', 169.9, 174.1],['/code/flask/imagens/36 1.single-life-quotes.jpg', 174.2, 177.5]]

    #dream_image_timestamp = aux_dream(image_timestamp)
    
    make_video(image_timestamp)

    done_job = True
    return 'tudo certo ate agora.'

# print project_structure('envolvimento', 'mc loma')







