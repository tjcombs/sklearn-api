# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 19:55:51 2020

@author: tjcombs

This script contains functions for users to interact with the api.

"""

import pandas as pd
import requests

class ModelAPI:
    def __init__(self, api_url):
        if not api_url.endswith('/'):
            api_url = api_url+'/'
        self.api_url = api_url
        
    def predict(self, df_X):
        df_json = df_X.to_json()
        r = requests.post(url = self.api_url+'predict', json=df_json)
        prediction = pd.DataFrame(r.json())
        r.close()
        return prediction['prediction']

if __name__ == '__main__':
    model = ModelAPI(api_url = 'http://127.0.0.1:5000/')
    df = pd.DataFrame({'A': [3, 6, 7], 'B': [9, 4, 3]})
    df['y'] = model.predict(df[['A', 'B']])
    assert((df['y'] == df['A'] + df['B'] + 5).all())