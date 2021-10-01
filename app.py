from flask import Flask, render_template, url_for, redirect, request
import pickle
import pandas as pd
import numpy as np
from forms import ticket_details
from pathlib import Path
from notebook import le, ss # for scaling user inputs

app = Flask(__name__)

app.config['SECRET_KEY'] = '21d58b5f23bcc9fc0a8759e261dddbae' # this is for wtf-forms

@app.route("/")
def home():
    return render_template('layout.html')

@app.route("/overview")
def overview():
    return render_template('overview.html')

@app.route("/prediction_results",  methods = ['GET', 'POST'])
def prediction_results():
    form = ticket_details()
    if request.method == 'POST':
        #grabbing user inputs
        Age = form.age.data
        Sex = form.sex.data
        Pclass = form.pclass.data
        SibSp = form.sibsp.data
        Parch = form.parch.data
        Fare = form.fare.data

        #converting a dict to transfer to a dataframe
        data = {'Pclass': [Pclass],'Sex': [Sex],'Age': [Age],'SibSp': [SibSp],'Parch': [Parch],'Fare': [Fare]}
        user_df = pd.DataFrame(data)
        
        # Cleaning, transforming and scaling to transform user inputs before predicting
        user_df = user_df.fillna(user_df.Age.mean())
        user_df = user_df.values
        user_df[:,1] = le.transform(user_df[:,1])
        user_inputs = ss.transform(user_df)


        # We load decision tree classifier model that we saved earlier in pickl-csv-files folder
        loaded_model=pickle.load(open('pickel-csv-files/Decision-tree.pkl', 'rb'))
        #load inputs to the model to generate results
        predictionn = loaded_model.predict(user_inputs)

        #converting the number to readable format
        if predictionn[0] == 1:
            result = 'survive'
        if predictionn[0] == 0:
            result = 'not survive'
    return render_template('prediction_results.html', result = result)

@app.route("/form", methods = ['GET', 'POST'])
def form():
    form = ticket_details()
    return render_template('ticket_form.html', title = 'Ticket Form', form = form )

@app.route("/down_arrow")
def down_arrow():
    return render_template('down_arrow.html')

@app.route("/facts")
def facts():
    return render_template('facts.html')

@app.route("/prediction")
def prediction():
    return render_template('prediction.html')

@app.route("/advice", methods = ['GET', 'POST'])
def advice():
    form = ticket_details()
    return render_template('advice.html', title = 'Ticket Form', form = form )


if __name__ == '__main__':
    app.run(debug=True)
