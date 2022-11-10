# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 12:42:48 2022

@author: hmerckoll
"""

class Users():
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        
    def orders(self, quantity):
        self.quantity = quantity
        self.cash -= self.quantity
        
    