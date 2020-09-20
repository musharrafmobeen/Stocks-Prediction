# Install The Dependencies
import numpy as np
import pandas as pd
import os
import datetime as dt
from sklearn.tree import DecisionTreeRegressor as DTR
from sklearn.tree import DecisionTreeClassifier as DSC
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression as lr
import matplotlib
import time
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# import joblib
plt.style.use('bmh')


def train(stocks_data):
    stocks_data['Date'] = pd.to_datetime(stocks_data['Date'])
    stocks_data['Date'] = stocks_data['Date'].map(dt.datetime.toordinal)
    stocks_data['Date']
    x = stocks_data.drop(columns=['Open', 'High', 'Low', 'Close', 'Volume'])
    y = stocks_data.drop(columns=['Date'])
    model = DTR()
    model.fit(x, y)
    return model

def prediction(prediction_date, model):
    predictions = model.predict([[prediction_date]])
    return predictions

def graph(stocks_data,prediction_date, company_name):
    current_date = dt.datetime.now().toordinal()
    future_days = prediction_date - current_date
    stocks_data['prediction'] = stocks_data[['Close']].shift(-future_days)
    plt.figure(figsize=(16, 8))
    plt.title(company_name)
    plt.xlabel('Date')
    plt.ylabel('close Price USD ($)')
    plt.plot(stocks_data['prediction'])
    new_graph_name = "graph"+ str(time.time()) + ".png"
    for filename in os.listdir('static/graphs/'):
        if filename.startswith('graph'):
            os.remove('static/graphs/'+ filename)
    plt.savefig('static/graphs/' + new_graph_name)
    return new_graph_name

