
from search_lyric import get_lyric_videoLink
from download_music import download_song

def project_structure(text_music_name,text_artist_name):
    
    temp = get_lyric_videoLink(text_music_name,text_artist_name)
    
    if temp is None:
        return 'Nao foi possivel concluir, escolha outra musica.'
    
    youtube_link = temp[0]
    lyric = temp[1] 

    download_song(youtube_link)

    return 'tudo certo ate agora.'

# print project_structure('envolvimento', 'mc loma')