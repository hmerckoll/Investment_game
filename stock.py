# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 12:44:32 2022

@author: hmerckoll
"""
from datapull import datapull

class Stock():
    def __init__(self, stock_name):
        self.stock_name = stock_name

        
    def get_lastest_stock_price(self):
        self.latest_stock_price = datapull(self.stock_name)['close'][10] #Getting stock price 10 days ago
        return self.latest_stock_price
    
    def get_stock_purchasedate(self):
        self.stock_purchasedate = datapull(self.stock_name).index[10] #Getting purchase date which is 10 days ago
        return str(self.stock_purchasedate)
    
    def get_latest_stock_price_performance(self):
        self.latest_stock_price_performance = datapull(self.stock_name)['close'][0] #Getting the actual stock price as of now
        return self.latest_stock_price_performance
    