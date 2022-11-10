# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 12:44:32 2022

@author: hmerckoll
"""

from users import Users

class Orders():
    def __init__(self, users: Users):
        self.user = users
        
    def buy(self, quantity, stock):
        self.quantity = quantity
        self.stock = stock
        self.user.balance -= self.quantity*1