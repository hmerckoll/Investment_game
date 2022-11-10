# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 11:56:39 2022

@author: hmerckoll
"""

from datapull import datapull
from users import Users
from orders import Orders

#df = datapull()

if __name__ == '__main__':        
        bruker1 = Users('dong', 100)
        print(bruker1.cash)
        
        ordre1 = Orders(bruker1)
        
        ordre1.buy(1000,'APPL')
        print(bruker1.quantity)
        
        #if bruker1.name == ordre1.name:
         #   print('Dong har apple')