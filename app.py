import re
import numpy as np
import os
import pandas as pd
import tensorflow as tf

from flask import Flask, request, app, render_template
from tensorflow.keras import models

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image    

from werkzeug.utils import secure_filename
#loading the model
model=load_model(r"crime_vision.h5",compile=False)
app=Flask(__name__,template_folder='templates')

#homepage
@app.route('/')
def home():
    return render_template('index.html')

#prediction page
@app.route('/prediction')
def prediction():
    return render_template('predict.html')

#prediction function
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the file from the request
        file = request.files['image']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(file.filename))
        file.save(file_path)
        img= image.load_img(file_path, target_size=(224, 224))
        
        x=image.img_to_array(img) #converting to array
        x=np.expand_dims(x,axis=0)  #expanding the dimensions
        pred=np.argmax(model.predict(x))
        op=['Fighting','Arrest','Vandalism','Assault','Stealing','Arson','NormalVideos','Abuse','Explosion','Robbery','Burglary','Shooting','Shoplifting','RoadAccidents']
        result = 'The Predicted Crime Type is '+str(op[pred])           # Convert to string
    return render_template("predict.html", prediction_text=result)  # Return the result to the frontend

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.2')