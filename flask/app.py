#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
from flask import *
app = Flask(__name__)

from source_code import *


template_dir = '/code/flask/html'
static_dir = '/code/flask/static'





app = Flask(__name__,template_folder=template_dir, static_folder=static_dir)

@app.route('/', methods=['GET', 'POST'])
def index():
	global input_MusicName
	global input_ArtistName
	global input_ImageType
	global input_OpDeepDream 
	exec_flag = False

	if request.method == 'POST':
		input_MusicName = request.form['musicName']
		input_ArtistName = request.form['artistName']
		input_ImageType = request.form.get('typeImageOp')
		input_OpDeepDream = False
		input_deeoDreamForm = request.form['deepDreamOpFrame']
		if request.form.get('deepDreamOp'):
			input_OpDeepDream = True
		
		nv = project_structure(input_MusicName,input_ArtistName,input_ImageType,input_OpDeepDream,input_deeoDreamForm)
		return redirect('/clipe/'+nv)
		
	else:
		return render_template('index.html')



@app.route('/clipe/<clipeName>')
def clipe(clipeName):
		return render_template('clipe.html',name_video = '/static/video/'+clipeName)


if __name__ == '__main__':
	app.run(debug = True, use_reloader=False, host='0.0.0.0', port=5000)
		