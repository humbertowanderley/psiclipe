from google_images_download import google_images_download

def search_image(busc, limit):

	response = google_images_download.googleimagesdownload()

	arguments = {"keywords":busc,
			"limit":limit,
			"print_urls":True, 
			"delay":1, 
			"exact_size": "640,480",
			"format":'jpg',
			"output_directory":"/code/flask/imagens",
			"no_directory": True,
			"prefix":busc}
	paths = response.download(arguments)
	return(paths[0][busc][0])

def get_lyric_images(lyric):
	vetor = []
	for i in lyric:
		vetor.append([search_image(i[0].replace(',','').replace(u'\u2019','').replace(u'\u2018','').replace(u'\xea','e').replace(u'\xe9','e').replace(u'\xe3','a').replace(u'\xe1','a').replace(u'\xf3','o'),1),i[1],i[2]])
	return vetor

