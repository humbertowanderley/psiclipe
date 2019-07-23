#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from google_images_download import google_images_download
from rake_nltk import Rake
import random
import json
import Image
image_sequence = 0

def search_image(busc, limit, image_type,prefix):
	global image_sequence

	response = google_images_download.googleimagesdownload()

	arguments = {"keywords":busc,
			"limit":limit,
			"print_urls":True,
			"exact_size": "800,600",
			"type": image_type,
			"format":'jpg',
			"output_directory":"/code/flask/imagens",
			"no_directory": True,
			"color_type": 'full-color',
			"prefix": str(prefix)
			}
	paths = response.download(arguments)

	return(paths[0][busc][0])

def get_images(json_subtitle,image_type):
   rake=Rake()
   count = 0
	
   while count < len(json_subtitle):
		words = rake.extract_keywords_from_text(json_subtitle[count]['Lyric'].decode('utf-8').replace(',','').replace(u'\u2019','').replace(u'\u2018','').replace(u'\xea','e').replace(u'\xe9','e').replace(u'\xe3','a').replace(u'\xe1','a').replace(u'\xf3','o').replace(u'\xf1','n').replace(u'\xed','i').replace(u'\xe7','c'))
		words = rake.get_ranked_phrases()

		search_text = random.choice(words[0].split())
		img_before = search_image(search_text,1,image_type,count)

		img = Image.open(img_before)
		img = img.resize((800,600),Image.ANTIALIAS)
		img.save("/code/flask/imagens/"+str(count)+".jpg")
		img_after = "/code/flask/imagens/"+str(count)+".jpg"
		json_subtitle[count]['Image'] = img_after

		os.remove(img_before)
		
		print json_subtitle[count]['Image']
		count += 1
	
   return json_subtitle
    	
