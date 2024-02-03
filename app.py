import pickle
from flask import Flask, request, app, jsonify, url_for, render_template, redirect
import numpy as np
import pandas as pd
from loggerMain import InsurancePredictLogger
import pymongo
import io
import os
import time
from werkzeug.serving import make_server

app = Flask(__name__)
model= pickle.load(open('R_model.pkl', 'rb'))


@app.route('/')
def home():
    try:
        log = InsurancePredictLogger.ineuron_scrap_logger()
        log.info("Index initialization successfull")
        #return 'Hello World'
        return render_template('index.html')
    except Exception as e:
        log.exception(" Something went wrong on initiation process")

"""@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        log = FirePredictLogger.ineuron_scrap_logger()
        log.info("predict_api for Postman initialization successfull")
        data = request.json['data']
        print(data)
        new_data = [list(data.values())]
        output = int(modelC.predict(new_data)[0])
        log.info("Predication for predict_api successfull with value")
        print(data)
        print(new_data)
        return jsonify(output)
    except Exception as e:
        log.exception(" Something went wrong on predict_api for Postman process")"""


@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_features = [np.array(data)]
    print(data)
        
    
    try:
        log = InsurancePredictLogger.ineuron_scrap_logger()
        log.info("Single regression prediction initialization successfull")
        data = [float(x) for x in request.form.values()]
        final_features = [np.array(data)]
        print(data)
        
        output = model.predict(final_features)[0]
        log.info("Prediction for predict-single regression successfull with value")
        print(output)
        
        return render_template('index.html', prediction_text = "Predicted Charge is  {:.2f} ".format(output))
    except Exception as e:
        log.exception(" Something went wrong on Single regression prediction initiation process")


if __name__ == "__main__":
    app.run(debug = True)