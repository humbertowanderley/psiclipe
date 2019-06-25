from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
import cv2
import os
from moviepy.editor import *

image_folder = '/code/flask/imagens/'
music_folder = '/code/flask/music'


def make_video():
	video_name = 'video.avi'

	images = [(image_folder + img) for img in os.listdir(image_folder) if img.endswith(".jpg")]


	videoclip = ImageSequenceClip(images, fps=1)
	music = [mus for mus in os.listdir(music_folder) if mus.endswith(".mp3")]
	audioclip = AudioFileClip(os.path.join(music_folder, music[0]))

	videoOut= videoclip.set_audio(audioclip)
	videoOut.write_videofile("/code/flask/static/video/psiclipe.mp4")
