# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 19:38:20 2020

@author: tjcombs

"""

from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
     df = pd.read_json(request.json)
     prediction = model.predict(df)
     return jsonify({'prediction': list(prediction)})
 
if __name__ == '__main__':
    # Import your model
    # In our case, we will create a example model just for the sake of
    # development.
    from sklearn.linear_model import LinearRegression
    df = pd.DataFrame({'A':[1, 2, 3, 4], 'B':[2, 3, 4, 5]})
    df['y'] = df['A'] + df['B'] + 5
    model = LinearRegression()
    model.fit(df[['A', 'B']], df['y'])
    
    app.run()