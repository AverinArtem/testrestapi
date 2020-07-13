# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 00:01:21 2020

@author: averin artem
"""

from flask import Flask, request
from werkzeug.utils import secure_filename
import numpy as np
from PIL import Image

ALLOWED_EXTENSION = set(['png'])


def dominant_color(filename):
    #Resizing parameters
    width, height = 150,150
    image = Image.open(filename)
    image = np.array(image)
    image = image[:,:,0:3]
    colors, count = np.unique(image.reshape(-1,image.shape[-1]), axis=0, return_counts=True)    
    return colors[count.argmax()]

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION

app = Flask(__name__)

@app.route("/test/form/upload_image")
def hello_world():
    return '<form action="/upload_image" method="POST"><input type="submit" value="Upload"></form>'

@app.route("/api/determine_dominate_color", methods=['POST'])
def print_filename():
    
    file = request.files['file']
    filename = secure_filename(file.filename)
    if allowed_file(file.filename):
        res = str(dominant_color(filename))
    else:
        res = 'input image must be png format'
    
    return res

if __name__=="__main__":
    app.run(port=8080, debug=True)