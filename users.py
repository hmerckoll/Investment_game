# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 12:42:48 2022

@author: hmerckoll
"""

class User():
    def __init__(self, user_name, balance):
        self.user_name = user_name
        self.balance = balance
        self.portfolio = {}
        
#    def orders(self, quantity):
#        self.quantity = quantity
#        self.cash -= self.quantity
        
    