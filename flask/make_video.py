#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
#import cv2
import os
from moviepy.editor import *
# from moviepy.audio.AudioClip import CompositeAudioClip
import ffmpeg
image_folder = '/code/flask/imagens/'
music_folder = '/code/flask/music'

def scroll(get_frame, t):
    """
    This function returns a 'region' of the current frame.
    The position of this region depends on the time.
    """
    frame = get_frame(t)
    frame_region = frame[int(t):int(t)+360,:]
    return frame_region

def make_video_ffmpeg(json_code,music_name):
    ffmpeg.input('/code/flask/imagens/*.jpg', pattern_type='glob', framerate=25).output('/code/flask/static/video/psiclipe-' + music_name + '.mp4').run()
    return '/code/flask/static/video/psiclipe-' + music_name + '.mp4'


def make_videoDeep(json_code,music_name,op_frame):
    
	frames = []

	frames.append( ImageClip('/code/flask/intro.jpg', duration = json_code['Subtitle'][0]['Begin']) )

	if op_frame:
		for sub in json_code['Subtitle']:
			frames.append( ImageClip( sub['ImageDeepDream'], duration = (sub['End'] - sub['Begin']) ) )
	else:
    		for subtitleView in json_code['Subtitle']:
				for sub in subtitleView['ImageDeepDream']:
					frames.append( ImageClip( sub['Image'], duration = (sub['End'] - sub['Begin']) ) )


	frames_concatenated = concatenate_videoclips(frames)

	audio = AudioFileClip(json_code['MusicPath'])

	video_clip = frames_concatenated.set_audio(audio)

	video_clip.write_videofile('/code/flask/static/video/psiclipe-' + music_name.replace(' ','-') + '.mp4', fps=5)
	return 'psiclipe-' + music_name.replace(' ','-') + '.mp4'

def make_videoDeep_lyric(json_code,music_name,op_frame):
    
	frames = []

	frames.append( ImageClip('/code/flask/intro.jpg', duration = json_code['Subtitle'][0]['Begin']) )

	if op_frame:
		for sub in json_code['Subtitle']:
			frames.append(CompositeVideoClip([ ImageClip( sub['ImageDeepDream'], duration = (sub['End'] - sub['Begin']) ), TextClip(sub['Lyric'], fontsize=30, color='yellow', stroke_color='black', stroke_width=0.7).set_position(('center', 'bottom'))]).set_duration((sub['End'] - sub['Begin'])))

	else:
    		for subtitleView in json_code['Subtitle']:
				for sub in subtitleView['ImageDeepDream']:
					frames.append(CompositeVideoClip([ ImageClip( sub['Image'], duration = (sub['End'] - sub['Begin']) ), TextClip(subtitleView['Lyric'], fontsize=30, color='yellow', stroke_color='black', stroke_width=0.7).set_position(('center', 'bottom'))]).set_duration((sub['End'] - sub['Begin'])))


	frames_concatenated = concatenate_videoclips(frames)

	audio = AudioFileClip(json_code['MusicPath'])

	video_clip = frames_concatenated.set_audio(audio)

	video_clip.write_videofile('/code/flask/static/video/psiclipe-' + music_name.replace(' ','-') + '.mp4', fps=5)
	return 'psiclipe-' + music_name.replace(' ','-') + '.mp4'

# def make_videoDeep_5(json_code,music_name):
#     frames = []
# 	frames.append( ImageClip('/code/flask/intro.jpg', duration = json_code['Subtitle'][0]['Begin']) )

#     return 'abc'

	# # for subtitleView in json_code['Subtitle']:
    # # 	for sub in subtitleView['ImageDeepDream']:
	# # 		frames.append( ImageClip( sub['Image'], duration = (sub['End'] - sub['Begin']) ) )

	# frames_concatenated = concatenate_videoclips(frames)

	# audio = AudioFileClip(json_code['MusicPath'])

	# video_clip = frames_concatenated.set_audio(audio)

	# video_clip.write_videofile('/code/flask/static/video/psiclipe-' + music_name.replace(' ','-') + '.mp4', fps=10)
	# return 'psiclipe-' + music_name.replace(' ','-') + '.mp4'


def make_video(json_code,music_name):
    
	frames = []

	frames.append( ImageClip('/code/flask/intro.jpg', duration = json_code['Subtitle'][0]['Begin']) )

	for sub in json_code['Subtitle']:
		frames.append( ImageClip( sub['Image'], duration = (sub['End'] - sub['Begin']) ) )

	frames_concatenated = concatenate_videoclips(frames)

	audio = AudioFileClip(json_code['MusicPath'])

	video_clip = frames_concatenated.set_audio(audio)

	video_clip.write_videofile('/code/flask/static/video/psiclipe-' + music_name.replace(' ','-') + '.mp4', fps=5)
	return 'psiclipe-' + music_name + '.mp4'

def make_video_lyric(json_code,music_name):
    
	frames = []

	frames.append( ImageClip('/code/flask/intro.jpg', duration = json_code['Subtitle'][0]['Begin']) )

	for sub in json_code['Subtitle']:#precisa installar isso: apt install imagemagick
		frames.append(CompositeVideoClip([ ImageClip( sub['Image'], duration = (sub['End'] - sub['Begin']) ) , TextClip(sub['Lyric'], fontsize=30, color='yellow', stroke_color='black', stroke_width=0.7).set_position(('center', 'bottom'))]).set_duration((sub['End'] - sub['Begin'])))

	frames_concatenated = concatenate_videoclips(frames)

	audio = AudioFileClip(json_code['MusicPath'])

	video_clip = frames_concatenated.set_audio(audio)

	video_clip.write_videofile('/code/flask/static/video/psiclipe-' + music_name.replace(' ','-') + '.mp4', fps=5)
	return 'psiclipe-' + music_name + '.mp4'


# def make_video(images_timestamp):
# 	video_name = 'video.avi'
	
# 	first_image = True

# 	all_clips = []

# 	previousLine = []

# 	for line in images_timestamp:
# 		if(first_image):
# 			all_clips.append(ImageClip('/code/flask/intro.jpg',duration=(float(line[1]))))
# 			first_image = False
# 		else:
#     			all_clips.append(ImageClip(previousLine[0],duration=(float(line[1])-float(previousLine[2]))))
		
# 		all_clips.append(ImageClip(line[0],duration=(float(line[2])-float(line[1]))))
# 		previousLine = line
	
# 	final_clip = concatenate_videoclips(all_clips)

# 	music = [mus for mus in os.listdir(music_folder) if mus.endswith(".mp3")]
# 	audioclip = AudioFileClip(os.path.join(music_folder, music[0]))

# 	final_clip= final_clip.set_audio(audioclip)

# 	final_clip.write_videofile("/code/flask/static/video/psiclipe.mp4", fps=24)



def improve_subtitle(json_subtitle):
	count = 0
	json_before = {}
	while (count+1) < len(json_subtitle):
		
		json_subtitle[count]['End'] = json_subtitle[count+1]['Begin']

		count += 1
	
   	return json_subtitle

# def improve_timestamp(images_timestamp):
# 	iti = []

# 	firstLine = True
# 	lineBefore = []
# 	for line in images_timestamp:
# 		if firstLine:
# 			lineBefore = line
# 			firstLine = False
# 			continue
# 		else:
#     			iti.append( [lineBefore[0], lineBefore[1], line[1]] )
#     		# iti.append([lineBefore[0],lineBefore[1],line[1]])
# 			lineBefore = line
# 	iti.append( [lineBefore[0], lineBefore[1], lineBefore[2]] )
# 	# iti.append([lineBefore[0],lineBefore[1],lineBefore[2]])

# 	return iti