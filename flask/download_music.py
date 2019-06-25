from __future__ import unicode_literals
import youtube_dl

#comando adicionado: sudo apt-get install ffmpeg

def url_search(music_name):
    url_ret = 'ytsearch1:' + music_name + 'official music'
    return url_ret

def music(music_name):
    class MyLogger(object):
        def debug(self, msg):
            pass

        def warning(self, msg):
            pass

        def error(self, msg):
            print(msg)


    def my_hook(d):
        if d['status'] == 'downloading':
            print('It\'s downloading...')
        if d['status'] == 'finished':
            print('Done downloading, now converting ...')

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '/code/flask/music/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url_search(music_name)])
        
    return 'music downloaded'

def download_song(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '/code/flask/music/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print 'ok'
    return 'ok'