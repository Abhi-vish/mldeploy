from flask import Flask, jsonify, request,render_template
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.base import BaseEstimator
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/info')
def EnterDetails():
    return render_template('Detail.html')

@app.route('/aboutus')
def aboutus():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    try:
        if request.method == 'POST':
            gre_score = float(request.form['GRE'])
            toefl_score = float(request.form['TOFEL'])
            university_rating = float(request.form['University'])
            sop = float(request.form['SOP'])
            lor = float(request.form['LOR'])
            cgpa = float(request.form['CGPA'])
            research = float(request.form['Research'])
            filename = 'model/linear_model.pickle'
            load_model = pickle.load(open(filename, 'rb'))

            """"
            Loading the dataset and loading the features in variable x
            """
            df = pd.read_csv("model/Admission_Predict.csv")
            df.drop(columns='Serial No.',inplace=True)
            x = df.drop(columns=['Chance of Admit '])

            """
            we transfored the data using StandardScale to reduce highly correlation
            that's we again using StandardScale to pass the Actual data to model
            """
            scaler = StandardScaler()
            arr = scaler.fit_transform(x)
            # print(arr)

            data =scaler.transform([[gre_score, toefl_score, university_rating, sop, lor, cgpa, research]])

            # Predicting the the result
            prediction = load_model.predict(data)

            

            return render_template('output.html', prediction=round(100*prediction[0]))
        
    except Exception as e:
        print("the error is : ",e)

if __name__ == '__main__':
    app.run(debug=True)