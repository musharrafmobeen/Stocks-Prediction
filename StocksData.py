import yfinance as yf
from flask import Flask 
import StocksPrediction as SP
import pandas as pd
from flask import render_template
import  webbrowser
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import json


def prediction(Company_Name,Date):
    a_string = Company_Name
    stripped_string = a_string.strip("'")
    company_name = stripped_string
    stock_name = yf.Ticker(company_name)
    prediction_date = Date
    date = pd.to_datetime(prediction_date)
    date = date.toordinal()
    print(date)
    # stock_name.info
    stock_data = stock_name.history(period="2Y")
    stock_data = stock_data.drop(columns=['Dividends', 'Stock Splits'])

    dates =[]
    for x in range(len(stock_data)):
        newdate = str(stock_data.index[x])
        newdate = newdate[0:10]
        dates.append(newdate)

    stock_data['Date'] = dates
    model = SP.train(stock_data)
    prediction = SP.prediction(date,model)
    global graph_name
    graph_name = SP.graph(stock_data,date, company_name)
    return prediction 


def return_graph_url():
    return graph_name