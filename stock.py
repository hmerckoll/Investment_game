# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 12:44:32 2022

@author: hmerckoll
"""
from datapull import datapull

class Stock():
    def __init__(self, stock_name):
        self.stock_name = stock_name

        
    def get_price(self):
        df = datapull()[self.stock_name]
        self.closing_price