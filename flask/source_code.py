#!/usr/bin/env python
# -*- coding: utf-8 -*-
from search_lyric import get_lyric_videoLink
from download_music import download_song
from get_images import get_images
from make_video import make_video
from make_video import make_video_lyric
from make_video import make_videoDeep
from make_video import make_videoDeep_lyric
from make_video import improve_subtitle
import json
from dream import dreamImage
from dream import dreamImage_5
from dream import dreamImage_10
import shutil


def project_structure(text_music_name,text_artist_name,image_type,op_lyric,op_deepDream,deepDream_format):
    global current_job
    shutil.rmtree('/code/flask/music', ignore_errors=True)
    shutil.rmtree('/code/flask/imagens', ignore_errors=True)

    json_code = get_lyric_videoLink(text_music_name,text_artist_name)
    
    json_code['MusicPath'] = download_song(json_code['VideoID'])

    print '\n\nmusica baixada\n\n'

    json_code['Subtitle'] = get_images(json_code['Subtitle'],image_type)
    print '\n\nimagens pegadas\n\n'
    
    json_code['Subtitle'] = improve_subtitle(json_code['Subtitle'])
    print '\n\ntimestamps modificado\n\n'
    if  op_deepDream:
        if deepDream_format == '1':
            json_code['Subtitle'] = dreamImage(json_code['Subtitle'])
            if op_lyric:
                video_name = make_videoDeep_lyric(json_code,text_music_name,True)
            else:
                video_name = make_videoDeep(json_code,text_music_name,True)
        elif deepDream_format == '5':
            json_code['Subtitle'] = dreamImage_5(json_code['Subtitle'])
            if op_lyric:
                video_name = make_videoDeep_lyric(json_code,text_music_name,False)
            else:
                video_name = make_videoDeep(json_code,text_music_name,False)
        else:
            json_code['Subtitle'] = dreamImage_10(json_code['Subtitle'])
            if op_lyric:
                video_name = make_videoDeep_lyric(json_code,text_music_name,False)
            else:
                video_name = make_videoDeep(json_code,text_music_name,False)
    else:
        if op_lyric:
            video_name = make_video_lyric(json_code,text_music_name)
        else:
            video_name = make_video(json_code,text_music_name)

    print '\n\nclipe feito\n\n'
    
    return video_name
