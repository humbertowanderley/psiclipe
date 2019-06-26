#!/usr/bin/env python
# -*- coding: utf-8 -*-
from google_images_download import google_images_download
from rake_nltk import Rake
import random
image_sequence = 0

def search_image(busc, limit):
	global image_sequence

	response = google_images_download.googleimagesdownload()

	arguments = {"keywords":busc,
			"limit":limit,
			"print_urls":True, 
			"delay":1, 
			"exact_size": "800,600",
			"format":'jpg',
			"output_directory":"/code/flask/imagens",
			"no_directory": True,
			"prefix": str(image_sequence)}
	paths = response.download(arguments)

	return(paths[0][busc][0])

def get_lyric_images(lyric):
	global image_sequence
	vetor = []
	r = Rake()

	for line in lyric:	
		text = line[0].replace(',','').replace(u'\u2019','').replace(u'\u2018','').replace(u'\xea','e').replace(u'\xe9','e').replace(u'\xe3','a').replace(u'\xe1','a').replace(u'\xf3','o')
		text = r.extract_keywords_from_text(text)
		text = r.get_ranked_phrases()
		aux = []
		search = ""
		for word in text:
			search = search + " " + random.choice(word.split())
		vetor.append([search_image(search,1), float(line[1]), float(line[2])])

		image_sequence = image_sequence + 1


	image_sequence = 0

	for element in vetor:
		print element





#	for i in lyric:
#		vetor.append([search_image(busc,1),i[1],i[2]])
	return vetor

