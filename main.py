# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 11:56:39 2022

@author: hmerckoll
"""

from datapull import datapull
from users import User
from orders import Order
from stock import Stock

df = datapull()

if __name__ == '__main__':        
        
        #Definere bruker
        bruker1 = User('dong', 100)
        
        stock1 = Stock('IBM')
        stock1.populate()
        stock1.closing_price
        
        
        #Printer initiell balance
        print(bruker1.balance)
        
        #Knytter en ordre til en bruker
        ordre1 = Order(bruker1)
        
        #Bruker kjøper 1000 aksjer 
        ordre1.buy(1000,'APPL')
        
        #Printer gjenværende balanse
        print(bruker1.balance)
        
        print(bruker1.portfolio)
        
        #if bruker1.name == ordre1.name:
         #   print('Dong har apple')