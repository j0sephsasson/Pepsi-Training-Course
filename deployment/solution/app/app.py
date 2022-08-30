import os
import warnings
warnings.filterwarnings('ignore')

import pickle, pandas as pd
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f2db5c122a2d53aa35c4963db91cd0b5e9009316e80f07a2294ba16f136f8723'

clf = pickle.load(open(r'C:\Users\12482\Desktop\Ashling\client\pepsi\Pepsi-Training-Course\deployment\solution\classifier.pkl', 'rb'))

# default page of our web-app
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/model', methods=['POST'])
def model():
    f = request.files['upload']
    row = int(request.form['row'])

    data = pd.read_csv(f, index_col=0)
    data.drop(columns='species', inplace=True)
    
    prediction = clf.predict(data.iloc[[row]])

    return render_template('prediction.html', prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)