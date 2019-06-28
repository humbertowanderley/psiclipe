#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
#import cv2
import os
from moviepy.editor import *

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


def make_video(images_timestamp):
	video_name = 'video.avi'
	
	first_image = True

	all_clips = []

	previousLine = []

	for line in images_timestamp:
		if(first_image):
			all_clips.append(ImageClip('/code/flask/intro.jpg',duration=(float(line[1]))))
			first_image = False
		else:
			all_clips.append(ImageClip(previousLine[0],duration=(float(line[1])-float(previousLine[2]))))
		
		all_clips.append(ImageClip(line[0],duration=(float(line[2])-float(line[1]))))
		previousLine = line
	
	final_clip = concatenate_videoclips(all_clips)

	music = [mus for mus in os.listdir(music_folder) if mus.endswith(".mp3")]
	audioclip = AudioFileClip(os.path.join(music_folder, music[0]))

	final_clip= final_clip.set_audio(audioclip)

	final_clip.write_videofile("/code/flask/static/video/psiclipe.mp4", fps=24)

	 

