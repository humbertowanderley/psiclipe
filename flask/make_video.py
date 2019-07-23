#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from moviepy.editor import *
import ffmpeg

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

def improve_subtitle(json_subtitle):
	count = 0
	json_before = {}
	while (count+1) < len(json_subtitle):
		
		json_subtitle[count]['End'] = json_subtitle[count+1]['Begin']

		count += 1
	
   	return json_subtitle
