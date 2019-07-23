from __future__ import unicode_literals
import youtube_dl
import json


def download_song(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '/code/flask/music/'+url+'.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        
    return '/code/flask/music/'+url+'.mp3'