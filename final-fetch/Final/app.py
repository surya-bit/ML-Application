# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 12:27:30 2023

@author: Patron
"""
import numpy as np
import pandas as pd
import xgboost as xgb
import calendar
import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

def load_model():
    return joblib.load('xgb_model.pkl')

reg = load_model()
df=pd.read_csv('data_daily.csv')
df.columns=['Date','Receipt_count']
df = df.set_index('Date')
df.index = pd.to_datetime(df.index)
FEATURES = ['dayofweek', 'quarter', 'month','dayofyear','dayofmonth','weekofyear']

user_input = 'May'

def create_features(df):
    """
    Create time series features based on time series index.
    """
    df = df.copy()
    df['dayofweek'] = df.index.dayofweek
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['dayofyear'] = df.index.dayofyear
    df['dayofmonth'] = df.index.day
    df['weekofyear'] = df.index.isocalendar().week
    return df

def value_for_month(user_input):
        # Create features for each month in 2022
        months_2022 = pd.date_range(start='2022-01-01', end='2022-12-31', freq='MS')
        df_2022 = pd.DataFrame(months_2022, columns=['Date'])
        df_2022 = create_features(df_2022.set_index('Date'))
        df_2022['quarter']=df_2022['quarter']+4
        df_2022['month']=df_2022['month']+12
        df_2022['dayofyear']=df_2022['dayofyear']+365
        df_2022['dayofmonth']=df_2022['dayofmonth']+365
        df_2022['weekofyear']=df_2022['weekofyear']+52
        df_2022['dayofweek']=df_2022['dayofweek']


        # Use the trained model to predict Receipt_count for each month in 2022
        X_2022 = df_2022[FEATURES]
        selected_month=user_input
        month_number = list(calendar.month_name).index(selected_month)
        selected_month_data = X_2022[X_2022.index.month == month_number]
        
        month_prediction= reg.predict(selected_month_data)
        return month_prediction


def data_for_month(user_input):
        # Create 2022 data
        months_2022 = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')
        df_2022 = pd.DataFrame(months_2022, columns=['Date'])
        df_2022 = create_features(df_2022.set_index('Date'))
        df_2022['quarter']=df_2022['quarter']+4
        df_2022['month']=df_2022['month']+12
        df_2022['dayofyear']=df_2022['dayofyear']+365
        df_2022['dayofmonth']=df_2022['dayofmonth']+365
        df_2022['weekofyear']=df_2022['weekofyear']+52
        df_2022['dayofweek']=df_2022['dayofweek']
        selected_month=user_input
        month_number = list(calendar.month_name).index(selected_month)

        # Filter data for the selected month
        selected_month_data = df_2022[df_2022.index.month == month_number]
        #selected_month_data = df_2022[df_2022.index.month == 6]

        X_2022 =selected_month_data[FEATURES]
        month_days_predictions= reg.predict(X_2022)
        return month_days_predictions


def data_for_year():
        df_2022 = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')
        df_2022 = pd.DataFrame(df_2022, columns=['Date'])
        df_2022 = create_features(df_2022.set_index('Date'))
        df_2022['quarter']=df_2022['quarter']+4
        df_2022['month']=df_2022['month']+12
        df_2022['dayofyear']=df_2022['dayofyear']+365
        df_2022['dayofmonth']=df_2022['dayofmonth']+365
        df_2022['weekofyear']=df_2022['weekofyear']+52
        df_2022['dayofweek']=df_2022['dayofweek']
        all_days=df_2022[FEATURES]
        year_predictions=reg.predict(all_days)
        return year_predictions

@app.route('/', methods=['POST'])
def search():
    

    data = request.get_json()
    #df = create_features(df)
    if 'key1' not in data:
            raise ValueError("Missing 'key1' in the request data")
    user_input = data['key1']
    # Example: Search by category (assuming you have a function called search_by_category)
    if not user_input == None:
        month_prediction = value_for_month(user_input).tolist()
        month_days_predictions = data_for_month(user_input).tolist()
        year_days_predictions = data_for_year().tolist()   
        final_results={'monthValue':month_prediction,'monthData':[month_days_predictions],'yearData':[year_days_predictions]}
        #print(final_results)
        #results = json.dumps(final_results)
        return jsonify(final_results)
    else:
        return jsonify({"message": "No relevant offers found."})
        
if __name__ == '__main__':
    app.run(debug=True)
