#!/usr/bin/env python
# -*- coding: utf-8 -*-
from search_lyric import get_lyric_videoLink
from download_music import download_song
from get_images import get_lyric_images
from make_video import make_video
from dream import dreamVideo


current_job = "Aguarde..."
done_job = False

def project_structure(text_music_name,text_artist_name,op_deepDream,image_type):
    global current_job

    # current_job = "Buscando link da musica..."
    # temp = get_lyric_videoLink(text_music_name,text_artist_name)
    
    # if temp is None:
    #     return 'Nao foi possivel concluir, escolha outra musica.'
    
    # youtube_link = temp[0]

    # current_job = "Baixando letra da musica"
    # lyric = temp[1] 


    # current_job = "Baixando musica"
    # download_song(youtube_link)

    # current_job = "Baixando imagens"
    # image_timestamp = get_lyric_images(lyric,image_type)

    image_timestamp = [
        ['/code/flask/imagens/0 1.d4ythn1-748ba582-9f92-4a64-abb6-461f08723e13.jpg', 16.3, 18.8],
        ['/code/flask/imagens/1 1.17.jpg', 21.3, 25.1],
        ['/code/flask/imagens/2 1.NFS-PAYBACK.jpg', 26.2, 28.8],
        ['/code/flask/imagens/3 1.Youre-Pretty-Special-Just-Saying-tbw265.jpg', 31.3, 35.0],
        ['/code/flask/imagens/4 1.b3e4c636216499.5714b50b95c7e.jpg', 35.7, 38.9],
        ['/code/flask/imagens/5 1.ESCUDOS001.jpg', 41.0, 42.7],
        ['/code/flask/imagens/6 1.c-s-lewis-quote.jpg', 42.7, 49.3],
        ['/code/flask/imagens/7 1.69465630.jpg', 50.9, 55.1],
        ['/code/flask/imagens/8 1.105_1430.jpg', 66.3, 69.4],
        ['/code/flask/imagens/9 1.dark_music_2x.jpg', 71.2, 75.3],
        ['/code/flask/imagens/10 1.NFS-PAYBACK.jpg', 76.2, 79.2],
        ['/code/flask/imagens/11 1.22-BL14-117.jpg', 81.3, 85.2],
        ['/code/flask/imagens/12 1.processador-im-intel-usado-com-menor-preco-hnd-D_NQ_NP_666256-MLB28805713069_112018-F.jpg', 85.7, 89.0],
        ['/code/flask/imagens/13 1.ESCUDOS001.jpg', 90.9, 92.7],
        ['/code/flask/imagens/14 1.c-s-lewis-quote.jpg', 92.7, 99.1],
        ['/code/flask/imagens/15 1.69465630.jpg', 100.8, 105.2],
        ['/code/flask/imagens/16 1.Bombfrog-3.jpg', 105.7, 110.5],
        ['/code/flask/imagens/17 1.golf-bunker-shots.jpg', 110.6, 114.7],
        ['/code/flask/imagens/18 1.IMG-20170518-WA0003.width-800.jpg', 115.6, 118.0],
        ['/code/flask/imagens/19 1.3-things-cant-do-sleep_800x600.jpg', 118.1, 120.3],
        ['/code/flask/imagens/20 1.t1ondddeuod21.jpg', 120.3, 124.6],
        ['/code/flask/imagens/21 1.marietteshallowidolsweden.jpg', 126.1, 130.5],
        ['/code/flask/imagens/22 1.marietteshallowidolsweden.jpg', 131.1, 135.3],
        ['/code/flask/imagens/23 1.marietteshallowidolsweden.jpg', 136.2, 140.2],
        ['/code/flask/imagens/24 1.t1ondddeuod21.jpg', 140.2, 144.3],
        ['/code/flask/imagens/25 1.jun2019_f02_submarine_copy-edit.jpg', 165.7, 170.3],
        ['/code/flask/imagens/26 1.golf-bunker-shots.jpg', 170.4, 174.9],
        ['/code/flask/imagens/27 1.IMG-20170518-WA0003.width-800.jpg', 175.6, 178.1],
        ['/code/flask/imagens/28 1.3-things-cant-do-sleep_800x600.jpg', 178.1, 180.2],
        ['/code/flask/imagens/29 1.t1ondddeuod21.jpg', 180.3, 184.2],
        ['/code/flask/imagens/30 1.marietteshallowidolsweden.jpg', 186.3, 190.2],
        ['/code/flask/imagens/31 1.marietteshallowidolsweden.jpg', 191.2, 195.1],
        ['/code/flask/imagens/32 1.marietteshallowidolsweden.jpg', 196.1, 200.1],
        ['/code/flask/imagens/33 1.t1ondddeuod21.jpg', 200.2, 204.4]
    ]

    if op_deepDream:
        dream_image_timestamp = dreamVideo(image_timestamp)
        # dream_image_timestamp = aux_dream(image_timestamp)
        make_video(dream_image_timestamp)
    else:
        make_video(image_timestamp)

    done_job = True
    return 'tudo certo ate agora.'

# print project_structure('envolvimento', 'mc loma')







