# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 12:38:15 2022

@author: hmerckoll
"""

import requests
import pandas as pd

#stocks = ['IBM', 'MSFT']
dataframes ={}

def datapull(input_stock):
        
    URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={input_stock}&outputsize=full&apikey=demo"
    
    response = requests.get(URL)
    
    if response.status_code != 200:
        raise ValueError("Could not retrieve data, code:", response.status_code)
    
    raw_data = response.json()
    
    data = raw_data['Time Series (Daily)']
    df = pd.DataFrame(data).T.apply(pd.to_numeric)
    
    # Next we parse the index to create a datetimeindex
    #df.index = pd.DatetimeIndex(df.index)
    
    # Let's fix the column names by chopping off the first 3 characters
    df.rename(columns=lambda s: s[3:], inplace=True)
    
    #df[['open', 'high', 'low', 'close']].plot()
    
    #close_per_day = df.close.resample('B').last()
    #close_per_day.plot()
    
    return df
        
