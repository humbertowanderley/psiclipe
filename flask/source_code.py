#!/usr/bin/env python
# -*- coding: utf-8 -*-
from search_lyric import get_lyric_videoLink
from download_music import download_song
from get_images import get_lyric_images
from get_images import get_images
from make_video import make_video
from make_video import make_videoDeep
from make_video import improve_subtitle
import json
# from make_video import improve_timestamp
from dream import dreamImage
from dream import dreamImage_5
from dream import dreamImage_10
import shutil


current_job = "Aguarde..."
done_job = False

def project_structure(text_music_name,text_artist_name,image_type,op_deepDream,deepDream_format):
    global current_job
    shutil.rmtree('/code/flask/music', ignore_errors=True)
    shutil.rmtree('/code/flask/imagens', ignore_errors=True)
    current_job = "Buscando link da musica..."
    json_code = get_lyric_videoLink(text_music_name,text_artist_name)
    
    # print json_code['Lang']
    # print json_code['UserName']
    # print json_code['SongID']
    # print json_code['TranslationID']
    # print json_code['UserID']
    # print json_code['VideoID']
    # print json_code['ID']
    # print json_code['SentAt']
    # print json_code['Subtitle']

    # if temp is None:
    #     return 'Nao foi possivel concluir, escolha outra musica.'
    
    # print '\n\nlink de musica e letra buscada\n\n'

    # youtube_link = temp[0]

    # current_job = "Baixando letra da musica"
    # lyric = temp[1] 
    # print '\n\nletra pegada\n\n'

    # current_job = "Baixando musica"
    json_code['MusicPath'] = download_song(json_code['VideoID'])
    # print json_code.keys()
    # print json_code
    # print json_code['musicPath']
    print '\n\nmusica baixada\n\n'

    # current_job = "Baixando imagens"
    # image_timestamp = get_lyric_images(lyric,image_type)
    # print image_timestamp
    # print json_code['Subtitle']
    json_code['Subtitle'] = get_images(json_code['Subtitle'],image_type)
    print '\n\nimagens pegadas\n\n'
    # print json_code['Subtitle']
    # # image_timestamp = improve_timestamp(image_timestamp)
    # # print image_timestamp
    # # image_timestamp = [['/code/flask/imagens/0 1.how-to-tell-a-girl-you-like-her.jpg', 16.3, 18.8], ['/code/flask/imagens/1 1.4994003443_20bafa8c17_b.jpg', 21.3, 25.1], ['/code/flask/imagens/2 1.NFS-PAYBACK.jpg', 26.2, 28.8], ['/code/flask/imagens/3 1.coldplay-chainsmokers.jpg', 31.3, 35.0], ['/code/flask/imagens/4 1.b3e4c636216499.5714b50b95c7e.jpg', 35.7, 38.9], ['/code/flask/imagens/5 1.ESCUDOS001.jpg', 41.0, 42.7], ['/code/flask/imagens/6 1.c-s-lewis-quote.jpg', 42.7, 49.3], ['/code/flask/imagens/7 1.fear-the-walking-dead-season-3-troy-sharman-800x600-cast.jpg', 50.9, 55.1], ['/code/flask/imagens/8 1.105_1430.jpg', 66.3, 69.4], ['/code/flask/imagens/9 1.dark_music_2x.jpg', 71.2, 75.3], ['/code/flask/imagens/10 1.NFS-PAYBACK.jpg', 76.2, 79.2], ['/code/flask/imagens/11 1.22-BL14-117.jpg', 81.3, 85.2], ['/code/flask/imagens/12 1.processador-im-intel-usado-com-menor-preco-hnd-D_NQ_NP_666256-MLB28805713069_112018-F.jpg', 85.7, 89.0], ['/code/flask/imagens/13 1.ESCUDOS001.jpg', 90.9, 92.7], ['/code/flask/imagens/14 1.c-s-lewis-quote.jpg', 92.7, 99.1], ['/code/flask/imagens/15 1.fear-the-walking-dead-season-3-troy-sharman-800x600-cast.jpg', 100.8, 105.2], ['/code/flask/imagens/16 1.DSCN0375.jpg', 105.7, 110.5], ['/code/flask/imagens/17 1.golf-bunker-shots.jpg', 110.6, 114.7], ['/code/flask/imagens/18 1.surface-go-hero.jpg', 115.6, 118.0], ['/code/flask/imagens/19 1.hopearmsraisedskycreditshutterstockcom.jpg', 118.1, 120.3], ['/code/flask/imagens/20 1.t1ondddeuod21.jpg', 120.3, 124.6], ['/code/flask/imagens/21 1.marietteshallowidolsweden.jpg', 126.1, 130.5], ['/code/flask/imagens/22 1.marietteshallowidolsweden.jpg', 131.1, 135.3], ['/code/flask/imagens/23 1.marietteshallowidolsweden.jpg', 136.2, 140.2], ['/code/flask/imagens/24 1.t1ondddeuod21.jpg', 140.2, 144.3], ['/code/flask/imagens/25 1.DSCN0375.jpg', 165.7, 170.3], ['/code/flask/imagens/26 1.42-18102572.jpg', 170.4, 174.9], ['/code/flask/imagens/27 1.surface-go-hero.jpg', 175.6, 178.1], ['/code/flask/imagens/28 1.img_9262.jpg', 178.1, 180.2], ['/code/flask/imagens/29 1.t1ondddeuod21.jpg', 180.3, 184.2], ['/code/flask/imagens/30 1.marietteshallowidolsweden.jpg', 186.3, 190.2], ['/code/flask/imagens/31 1.marietteshallowidolsweden.jpg', 191.2, 195.1], ['/code/flask/imagens/32 1.marietteshallowidolsweden.jpg', 196.1, 200.1], ['/code/flask/imagens/33 1.t1ondddeuod21.jpg', 200.2, 204.4]]
    # # image_timestamp = [['/code/flask/dream_frames/0 1.how-to-tell-a-girl-you-like-her.jpg0.jpg', 16.3, 16.8], ['/code/flask/dream_frames/0 1.how-to-tell-a-girl-you-like-her.jpg1.jpg', 16.8, 17.3], ['/code/flask/dream_frames/0 1.how-to-tell-a-girl-you-like-her.jpg2.jpg', 17.3, 17.8], ['/code/flask/dream_frames/0 1.how-to-tell-a-girl-you-like-her.jpg3.jpg', 17.8, 18.3], ['/code/flask/dream_frames/0 1.how-to-tell-a-girl-you-like-her.jpg4.jpg', 18.3, 18.8], ['/code/flask/dream_frames/1 1.4994003443_20bafa8c17_b.jpg0.jpg', 21.3, 22.060000000000002], ['/code/flask/dream_frames/1 1.4994003443_20bafa8c17_b.jpg1.jpg', 22.060000000000002, 22.82], ['/code/flask/dream_frames/1 1.4994003443_20bafa8c17_b.jpg2.jpg', 22.82, 23.580000000000002], ['/code/flask/dream_frames/1 1.4994003443_20bafa8c17_b.jpg3.jpg', 23.580000000000002, 24.34], ['/code/flask/dream_frames/1 1.4994003443_20bafa8c17_b.jpg4.jpg', 24.34, 25.1], ['/code/flask/imagens/2 1.NFS-PAYBACK.jpg', 26.2, 28.8], ['/code/flask/imagens/3 1.coldplay-chainsmokers.jpg', 31.3, 35.0], ['/code/flask/imagens/4 1.b3e4c636216499.5714b50b95c7e.jpg', 35.7, 38.9], ['/code/flask/imagens/5 1.ESCUDOS001.jpg', 41.0, 42.7], ['/code/flask/imagens/6 1.c-s-lewis-quote.jpg', 42.7, 49.3], ['/code/flask/imagens/7 1.fear-the-walking-dead-season-3-troy-sharman-800x600-cast.jpg', 50.9, 55.1], ['/code/flask/imagens/8 1.105_1430.jpg', 66.3, 69.4], ['/code/flask/imagens/9 1.dark_music_2x.jpg', 71.2, 75.3], ['/code/flask/imagens/10 1.NFS-PAYBACK.jpg', 76.2, 79.2], ['/code/flask/imagens/11 1.22-BL14-117.jpg', 81.3, 85.2], ['/code/flask/imagens/12 1.processador-im-intel-usado-com-menor-preco-hnd-D_NQ_NP_666256-MLB28805713069_112018-F.jpg', 85.7, 89.0], ['/code/flask/imagens/13 1.ESCUDOS001.jpg', 90.9, 92.7], ['/code/flask/imagens/14 1.c-s-lewis-quote.jpg', 92.7, 99.1], ['/code/flask/imagens/15 1.fear-the-walking-dead-season-3-troy-sharman-800x600-cast.jpg', 100.8, 105.2], ['/code/flask/imagens/16 1.DSCN0375.jpg', 105.7, 110.5], ['/code/flask/imagens/17 1.golf-bunker-shots.jpg', 110.6, 114.7], ['/code/flask/imagens/18 1.surface-go-hero.jpg', 115.6, 118.0], ['/code/flask/imagens/19 1.hopearmsraisedskycreditshutterstockcom.jpg', 118.1, 120.3], ['/code/flask/imagens/20 1.t1ondddeuod21.jpg', 120.3, 124.6], ['/code/flask/imagens/21 1.marietteshallowidolsweden.jpg', 126.1, 130.5], ['/code/flask/imagens/22 1.marietteshallowidolsweden.jpg', 131.1, 135.3], ['/code/flask/imagens/23 1.marietteshallowidolsweden.jpg', 136.2, 140.2], ['/code/flask/imagens/24 1.t1ondddeuod21.jpg', 140.2, 144.3], ['/code/flask/imagens/25 1.DSCN0375.jpg', 165.7, 170.3], ['/code/flask/imagens/26 1.42-18102572.jpg', 170.4, 174.9], ['/code/flask/imagens/27 1.surface-go-hero.jpg', 175.6, 178.1], ['/code/flask/imagens/28 1.img_9262.jpg', 178.1, 180.2], ['/code/flask/imagens/29 1.t1ondddeuod21.jpg', 180.3, 184.2], ['/code/flask/imagens/30 1.marietteshallowidolsweden.jpg', 186.3, 190.2], ['/code/flask/imagens/31 1.marietteshallowidolsweden.jpg', 191.2, 195.1], ['/code/flask/imagens/32 1.marietteshallowidolsweden.jpg', 196.1, 200.1], ['/code/flask/imagens/33 1.t1ondddeuod21.jpg', 200.2, 204.4]]
    # # image_timestamp = [['/code/flask/imagens/0 1.how-to-tell-a-girl-you-like-her.jpg', 16.3, 18.8], ['/code/flask/imagens/1 1.4994003443_20bafa8c17_b.jpg', 21.3, 25.1], ['/code/flask/dream_frames/2 1.NFS-PAYBACK.jpg0.jpg', 26.2, 26.72], ['/code/flask/dream_frames/2 1.NFS-PAYBACK.jpg1.jpg', 26.72, 27.24], ['/code/flask/dream_frames/2 1.NFS-PAYBACK.jpg2.jpg', 27.24, 27.76], ['/code/flask/dream_frames/2 1.NFS-PAYBACK.jpg3.jpg', 27.76, 28.28], ['/code/flask/dream_frames/2 1.NFS-PAYBACK.jpg4.jpg', 28.28, 28.8], ['/code/flask/dream_frames/3 1.coldplay-chainsmokers.jpg0.jpg', 31.3, 32.04], ['/code/flask/dream_frames/3 1.coldplay-chainsmokers.jpg1.jpg', 32.04, 32.78], ['/code/flask/dream_frames/3 1.coldplay-chainsmokers.jpg2.jpg', 32.78, 33.52], ['/code/flask/dream_frames/3 1.coldplay-chainsmokers.jpg3.jpg', 33.52, 34.26], ['/code/flask/dream_frames/3 1.coldplay-chainsmokers.jpg4.jpg', 34.26, 35.0], ['/code/flask/imagens/4 1.b3e4c636216499.5714b50b95c7e.jpg', 35.7, 38.9], ['/code/flask/imagens/5 1.ESCUDOS001.jpg', 41.0, 42.7], ['/code/flask/imagens/6 1.c-s-lewis-quote.jpg', 42.7, 49.3], ['/code/flask/imagens/7 1.fear-the-walking-dead-season-3-troy-sharman-800x600-cast.jpg', 50.9, 55.1], ['/code/flask/imagens/8 1.105_1430.jpg', 66.3, 69.4], ['/code/flask/imagens/9 1.dark_music_2x.jpg', 71.2, 75.3], ['/code/flask/imagens/10 1.NFS-PAYBACK.jpg', 76.2, 79.2], ['/code/flask/imagens/11 1.22-BL14-117.jpg', 81.3, 85.2], ['/code/flask/imagens/12 1.processador-im-intel-usado-com-menor-preco-hnd-D_NQ_NP_666256-MLB28805713069_112018-F.jpg', 85.7, 89.0], ['/code/flask/imagens/13 1.ESCUDOS001.jpg', 90.9, 92.7], ['/code/flask/imagens/14 1.c-s-lewis-quote.jpg', 92.7, 99.1], ['/code/flask/imagens/15 1.fear-the-walking-dead-season-3-troy-sharman-800x600-cast.jpg', 100.8, 105.2], ['/code/flask/imagens/16 1.DSCN0375.jpg', 105.7, 110.5], ['/code/flask/imagens/17 1.golf-bunker-shots.jpg', 110.6, 114.7], ['/code/flask/imagens/18 1.surface-go-hero.jpg', 115.6, 118.0], ['/code/flask/imagens/19 1.hopearmsraisedskycreditshutterstockcom.jpg', 118.1, 120.3], ['/code/flask/imagens/20 1.t1ondddeuod21.jpg', 120.3, 124.6], ['/code/flask/imagens/21 1.marietteshallowidolsweden.jpg', 126.1, 130.5], ['/code/flask/imagens/22 1.marietteshallowidolsweden.jpg', 131.1, 135.3], ['/code/flask/imagens/23 1.marietteshallowidolsweden.jpg', 136.2, 140.2], ['/code/flask/imagens/24 1.t1ondddeuod21.jpg', 140.2, 144.3], ['/code/flask/imagens/25 1.DSCN0375.jpg', 165.7, 170.3], ['/code/flask/imagens/26 1.42-18102572.jpg', 170.4, 174.9], ['/code/flask/imagens/27 1.surface-go-hero.jpg', 175.6, 178.1], ['/code/flask/imagens/28 1.img_9262.jpg', 178.1, 180.2], ['/code/flask/imagens/29 1.t1ondddeuod21.jpg', 180.3, 184.2], ['/code/flask/imagens/30 1.marietteshallowidolsweden.jpg', 186.3, 190.2], ['/code/flask/imagens/31 1.marietteshallowidolsweden.jpg', 191.2, 195.1], ['/code/flask/imagens/32 1.marietteshallowidolsweden.jpg', 196.1, 200.1], ['/code/flask/imagens/33 1.t1ondddeuod21.jpg', 200.2, 204.4]]
    # # image_timestamp = [['/code/flask/dream_frames/0 1.how-to-tell-a-girl-you-like-her.jpg0.jpg', 16.3, 16.8], ['/code/flask/dream_frames/0 1.how-to-tell-a-girl-you-like-her.jpg1.jpg', 16.8, 17.3], ['/code/flask/dream_frames/0 1.how-to-tell-a-girl-you-like-her.jpg2.jpg', 17.3, 17.8], ['/code/flask/dream_frames/0 1.how-to-tell-a-girl-you-like-her.jpg3.jpg', 17.8, 18.3], ['/code/flask/dream_frames/0 1.how-to-tell-a-girl-you-like-her.jpg4.jpg', 18.3, 18.8], ['/code/flask/dream_frames/1 1.4994003443_20bafa8c17_b.jpg0.jpg', 21.3, 22.060000000000002], ['/code/flask/dream_frames/1 1.4994003443_20bafa8c17_b.jpg1.jpg', 22.060000000000002, 22.82], ['/code/flask/dream_frames/1 1.4994003443_20bafa8c17_b.jpg2.jpg', 22.82, 23.580000000000002], ['/code/flask/dream_frames/1 1.4994003443_20bafa8c17_b.jpg3.jpg', 23.580000000000002, 24.34], ['/code/flask/dream_frames/1 1.4994003443_20bafa8c17_b.jpg4.jpg', 24.34, 25.1], ['/code/flask/dream_frames/2 1.NFS-PAYBACK.jpg0.jpg', 26.2, 26.72], ['/code/flask/dream_frames/2 1.NFS-PAYBACK.jpg1.jpg', 26.72, 27.24], ['/code/flask/dream_frames/2 1.NFS-PAYBACK.jpg2.jpg', 27.24, 27.76], ['/code/flask/dream_frames/2 1.NFS-PAYBACK.jpg3.jpg', 27.76, 28.28], ['/code/flask/dream_frames/2 1.NFS-PAYBACK.jpg4.jpg', 28.28, 28.8], ['/code/flask/dream_frames/3 1.coldplay-chainsmokers.jpg0.jpg', 31.3, 32.04], ['/code/flask/dream_frames/3 1.coldplay-chainsmokers.jpg1.jpg', 32.04, 32.78], ['/code/flask/dream_frames/3 1.coldplay-chainsmokers.jpg2.jpg', 32.78, 33.52], ['/code/flask/dream_frames/3 1.coldplay-chainsmokers.jpg3.jpg', 33.52, 34.26], ['/code/flask/dream_frames/3 1.coldplay-chainsmokers.jpg4.jpg', 34.26, 35.0], ['/code/flask/imagens/4 1.b3e4c636216499.5714b50b95c7e.jpg', 35.7, 38.9], ['/code/flask/imagens/5 1.ESCUDOS001.jpg', 41.0, 42.7], ['/code/flask/imagens/6 1.c-s-lewis-quote.jpg', 42.7, 49.3], ['/code/flask/imagens/7 1.fear-the-walking-dead-season-3-troy-sharman-800x600-cast.jpg', 50.9, 55.1], ['/code/flask/imagens/8 1.105_1430.jpg', 66.3, 69.4], ['/code/flask/imagens/9 1.dark_music_2x.jpg', 71.2, 75.3], ['/code/flask/imagens/10 1.NFS-PAYBACK.jpg', 76.2, 79.2], ['/code/flask/imagens/11 1.22-BL14-117.jpg', 81.3, 85.2], ['/code/flask/imagens/12 1.processador-im-intel-usado-com-menor-preco-hnd-D_NQ_NP_666256-MLB28805713069_112018-F.jpg', 85.7, 89.0], ['/code/flask/imagens/13 1.ESCUDOS001.jpg', 90.9, 92.7], ['/code/flask/imagens/14 1.c-s-lewis-quote.jpg', 92.7, 99.1], ['/code/flask/imagens/15 1.fear-the-walking-dead-season-3-troy-sharman-800x600-cast.jpg', 100.8, 105.2], ['/code/flask/imagens/16 1.DSCN0375.jpg', 105.7, 110.5], ['/code/flask/imagens/17 1.golf-bunker-shots.jpg', 110.6, 114.7], ['/code/flask/imagens/18 1.surface-go-hero.jpg', 115.6, 118.0], ['/code/flask/imagens/19 1.hopearmsraisedskycreditshutterstockcom.jpg', 118.1, 120.3], ['/code/flask/imagens/20 1.t1ondddeuod21.jpg', 120.3, 124.6], ['/code/flask/imagens/21 1.marietteshallowidolsweden.jpg', 126.1, 130.5], ['/code/flask/imagens/22 1.marietteshallowidolsweden.jpg', 131.1, 135.3], ['/code/flask/imagens/23 1.marietteshallowidolsweden.jpg', 136.2, 140.2], ['/code/flask/imagens/24 1.t1ondddeuod21.jpg', 140.2, 144.3], ['/code/flask/imagens/25 1.DSCN0375.jpg', 165.7, 170.3], ['/code/flask/imagens/26 1.42-18102572.jpg', 170.4, 174.9], ['/code/flask/imagens/27 1.surface-go-hero.jpg', 175.6, 178.1], ['/code/flask/imagens/28 1.img_9262.jpg', 178.1, 180.2], ['/code/flask/imagens/29 1.t1ondddeuod21.jpg', 180.3, 184.2], ['/code/flask/imagens/30 1.marietteshallowidolsweden.jpg', 186.3, 190.2], ['/code/flask/imagens/31 1.marietteshallowidolsweden.jpg', 191.2, 195.1], ['/code/flask/imagens/32 1.marietteshallowidolsweden.jpg', 196.1, 200.1], ['/code/flask/imagens/33 1.t1ondddeuod21.jpg', 200.2, 204.4]]
    # # image_timestamp = [
    # # ['/code/flask/dream_frames/0 1.how-to-tell-a-girl-you-like-her.jpg', 16.3, 18.8],
    # # ['/code/flask/dream_frames/1 1.image121.jpg', 21.3, 25.1],
    # # ['/code/flask/dream_frames/2 1.NFS-PAYBACK.jpg', 26.2, 28.8],
    # # ['/code/flask/dream_frames/3 1.coldplay-chainsmokers.jpg', 31.3, 35.0],
    # # ['/code/flask/dream_frames/4 1.b3e4c636216499.5714b50b95c7e.jpg', 35.7, 38.9],
    # # ['/code/flask/dream_frames/5 1.mesa-de-canto-good-moveis-paris-164-4-800x600.jpg', 41.0, 42.7],
    # # ['/code/flask/dream_frames/6 1.c-s-lewis-quote.jpg', 42.7, 49.3],
    # # ['/code/flask/dream_frames/7 1.fear-the-walking-dead-season-3-troy-sharman-800x600-cast.jpg', 50.9, 55.1],
    # # ['/code/flask/dream_frames/8 1.d4ythn1-748ba582-9f92-4a64-abb6-461f08723e13.jpg', 66.3, 69.4],
    # # ['/code/flask/dream_frames/9 1.dark_music_2x.jpg', 71.2, 75.3],
    # # ['/code/flask/dream_frames/10 1.NFS-PAYBACK.jpg', 76.2, 79.2],
    # # ['/code/flask/dream_frames/11 1.22-BL14-117.jpg', 81.3, 85.2],
    # # ['/code/flask/dream_frames/12 1.processador-im-intel-usado-com-menor-preco-hnd-D_NQ_NP_666256-MLB28805713069_112018-F.jpg', 85.7, 89.0],
    # # ['/code/flask/dream_frames/13 1.ESCUDOS001.jpg', 90.9, 92.7],
    # # ['/code/flask/dream_frames/14 1.c-s-lewis-quote.jpg', 92.7, 99.1],
    # # ['/code/flask/dream_frames/15 1.69465630.jpg', 100.8, 105.2],
    # # ['/code/flask/dream_frames/16 1.jun2019_f02_submarine_copy-edit.jpg', 105.7, 110.5],
    # # ['/code/flask/dream_frames/17 1.42-18102572.jpg', 110.6, 114.7],
    # # ['/code/flask/dream_frames/18 1.surface-go-hero.jpg', 115.6, 118.0],
    # # ['/code/flask/dream_frames/19 1.hopearmsraisedskycreditshutterstockcom.jpg', 118.1, 120.3],
    # # ['/code/flask/dream_frames/20 1.t1ondddeuod21.jpg', 120.3, 124.6],
    # # ['/code/flask/dream_frames/21 1.marietteshallowidolsweden.jpg', 126.1, 130.5],
    # # ['/code/flask/dream_frames/22 1.marietteshallowidolsweden.jpg', 131.1, 135.3],
    # # ['/code/flask/dream_frames/23 1.marietteshallowidolsweden.jpg', 136.2, 140.2],
    # # ['/code/flask/dream_frames/24 1.t1ondddeuod21.jpg', 140.2, 144.3],
    # # ['/code/flask/dream_frames/25 1.Bombfrog-3.jpg', 165.7, 170.3],
    # # ['/code/flask/dream_frames/26 1.golf-bunker-shots.jpg', 170.4, 174.9],
    # # ['/code/flask/dream_frames/27 1.surface-go-hero.jpg', 175.6, 178.1],
    # # ['/code/flask/dream_frames/28 1.ap_18163634981363-fb2d564e1aeebbb35bbe92eba960cc6ec110f912-s800-c85.jpg', 178.1, 180.2],
    # # ['/code/flask/dream_frames/29 1.t1ondddeuod21.jpg', 180.3, 184.2],
    # # ['/code/flask/dream_frames/30 1.marietteshallowidolsweden.jpg', 186.3, 190.2],
    # # ['/code/flask/dream_frames/31 1.marietteshallowidolsweden.jpg', 191.2, 195.1],
    # # ['/code/flask/dream_frames/32 1.marietteshallowidolsweden.jpg', 196.1, 200.1],
    # # ['/code/flask/dream_frames/33 1.t1ondddeuod21.jpg', 200.2, 204.4]
    # # ]

    # if op_deepDream:
    #     dream_image_timestamp = dreamVideo(image_timestamp)
    #     print '\n\nrodado no deep dream\n\n'
    #     print dream_image_timestamp
    #     # dream_image_timestamp = aux_dream(image_timestamp)
    #     make_video(dream_image_timestamp)
    # else:
    #     make_video(image_timestamp)
    # print json_code['Subtitle']
    json_code['Subtitle'] = improve_subtitle(json_code['Subtitle'])
    print '\n\ntimestamps modificado\n\n'
    if  op_deepDream:
        if deepDream_format == '1':
            json_code['Subtitle'] = dreamImage(json_code['Subtitle'])
            video_name = make_videoDeep(json_code,text_music_name,True)
        elif deepDream_format == '5':
            #opção para futura implementação de deepdream com 5 frames
            json_code['Subtitle'] = dreamImage_5(json_code['Subtitle'])
            video_name = make_videoDeep(json_code,text_music_name,False)
        else:
            #opção para futura implementação de deepdream com 10 frames
            json_code['Subtitle'] = dreamImage_10(json_code['Subtitle'])
            video_name = make_videoDeep(json_code,text_music_name,False)
    else:    
        video_name = make_video(json_code,text_music_name)
    # video_name = make_video_ffmpeg(json_code,text_music_name)
    print '\n\nclipe feito\n\n'
    # print "\n\n\n"
    # print json_code['Subtitle']

    done_job = True
    return video_name

# print project_structure('envolvimento', 'mc loma')







