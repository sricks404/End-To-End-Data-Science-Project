# Flask Application (application.py)

'''
The purpose of making this file is for deployment purpose
The same content as in (app.py) is pasted here

For deployment purpose on AWS - we need to delete the app.py file
'''

# Importing necessary libraries
from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Creating the Flask Application
application = Flask(__name__) # Checking .ebextensions/python.config file

app = application

# Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods = ['GET', 'POST'])
def predict_datapoint():
    '''
    This function will be responsible for gettig the data
    and providing the prediction.
    '''
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData( # Reading all the values received
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline() # Initializing prediction pipeline
        results = predict_pipeline.predict(pred_df) # Model Prediction started
        return render_template('home.html', results = results[0]) # Returning the results


# Lets run app.py
if __name__=="__main__":
    # app.run(host="0.0.0.0", debug = True, port = 5000)
    app.run(host="0.0.0.0") # Debug mode should be made inactive during deployment  
