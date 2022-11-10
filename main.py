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
        
        #Definere bruker
        bruker1 = Users('dong', 100)
        
        #Printer initiell balance
        print(bruker1.balance)
        
        #Knytter en ordre til en bruker
        ordre1 = Orders(bruker1)
        
        #Bruker kjøper 1000 aksjer 
        ordre1.buy(1000,'APPL')
        
        #Printer gjenværende balanse
        print(bruker1.balance)
        
        #if bruker1.name == ordre1.name:
         #   print('Dong har apple')