#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
	# rake = Rake()
	# r = Rake()
   while count < len(json_subtitle):
		# words = rake.extract_keywords_from_text(change_decode(json_subtitle[count]['Lyric'].decode('utf-8')))
		words = rake.extract_keywords_from_text(json_subtitle[count]['Lyric'].decode('utf-8').replace(',','').replace(u'\u2019','').replace(u'\u2018','').replace(u'\xea','e').replace(u'\xe9','e').replace(u'\xe3','a').replace(u'\xe1','a').replace(u'\xf3','o').replace(u'\xf1','n').replace(u'\xed','i').replace(u'\xe7','c'))
		words = rake.get_ranked_phrases()

		# search_text = ''
		# for word in words:
		# 	search_text += word + ' '
		search_text = words[0]
		img = Image.open(search_image(search_text,1,image_type,count))
		img = img.resize((800,600),Image.ANTIALIAS)
		img.save("/code/flask/imagens/"+str(count)+".jpg")
		print img
		json_subtitle[count]['Image'] = "/code/flask/imagens/"+str(count)+".jpg"
		# json_subtitle[count]['Image'] = search_image(search_text,1,image_type,count)
		print json_subtitle[count]['Image']
		count += 1
	
   return json_subtitle
    	


def get_lyric_images(lyric,image_type):
	global image_sequence
	vetor = []
	r = Rake()

	for line in lyric:	
		text = line[0].replace(',','').replace(u'\u2019','').replace(u'\u2018','').replace(u'\xea','e').replace(u'\xe9','e').replace(u'\xe3','a').replace(u'\xe1','a').replace(u'\xf3','o')
		text = r.extract_keywords_from_text(text)
		text = r.get_ranked_phrases()

		search = ""
		for word in text:
			search = search + " " + random.choice(word.split())
		vetor.append([search_image(search+" artistic",1,image_type), float(line[1]), float(line[2])])

		image_sequence = image_sequence + 1


	image_sequence = 0

	for element in vetor:
		print element

#	for i in lyric:
#		vetor.append([search_image(busc,1),i[1],i[2]])
	return vetor

def change_decode(text):
	text.replace(',','')
	text.replace(u'\u2019','').replace(u'\u2018','')
	text.replace(u'\xea','e').replace(u'\xe9','e')
	text.replace(u'\xe3','a').replace(u'\xe1','a')
	text.replace(u'\xf3','o').replace(u'\xf3','o')
	text.replace(u'\xf1','n')
	return text