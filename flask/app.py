#!/usr/bin/env python

from flask import *
app = Flask(__name__)

from source_code import *

template_dir = '/code/flask/html'
static_dir = '/code/flask/static'


app = Flask(__name__,template_folder=template_dir, static_folder=static_dir)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        input_MusicName = request.form['musicName']
        input_ArtistName = request.form['artistName']
        return project_structure(input_MusicName,input_ArtistName)
    else:
        return render_template('index.html')

if __name__ == '__main__':
	app.run(debug = True, use_reloader=False, host='0.0.0.0', port=5000)