#!/usr/bin/env python
import shutil
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
	exec_flag = False
	shutil.rmtree('/code/flask/music', ignore_errors=True)
	shutil.rmtree('/code/flask/imagens', ignore_errors=True)
	

	if request.method == 'POST':
		input_MusicName = request.form['musicName']
		input_ArtistName = request.form['artistName']
		project_structure(input_MusicName,input_ArtistName)
		return redirect('/clipe')
		
	else:
		return render_template('index.html')



@app.route('/clipe', methods=['GET', 'POST'])
def clipe():
		return render_template('clipe.html')


if __name__ == '__main__':
	app.run(debug = True, use_reloader=False, host='0.0.0.0', port=5000)
		