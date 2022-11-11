# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 11:56:39 2022

@author: hmerckoll
"""

from datapull import datapull
from users import User
from stock import Stock
#from functions 

#df = datapull()

users = {}

if __name__ == '__main__':        
#1) En bruker opprettes basert på tekstinnput
    while True:
        username = input('Enter the username: ')
        user_balance = float(input('Enter your balance: '))
        user = User(username, user_balance)
        print(user.user_name, user.balance)

#2) Brukeren får tilbudet om å kjøpe en valgfri aksje og deretter antall av aksjen
        #Initier aksjen
        user_stock_name = input('Enter stock name: ')
        user_stock_quantity = int(input('Enter stock quantity: '))
        stock = Stock(user_stock_name)

#3) Aksjedata hentes fra API (siste tilgjengelige sluttpris og dato), og brukerens portefølje(kostpris, aksjenavn, kjøpsdato og antall askjer) og balanse oppdateres
        #Hent aksjepris
        stock_price = float(stock.get_lastest_stock_price())
        stock_purchase_date = stock.get_stock_purchasedate()
        
        #Oppdatere brukerens portefølje
        user.portfolio[user_stock_name] = {}
        user.portfolio[user_stock_name]['Purchase_date'] = stock_purchase_date
        user.portfolio[user_stock_name]['Purchase_price'] = stock_price
        user.portfolio[user_stock_name]['Purchase_quantity'] = user_stock_quantity
        user.portfolio[user_stock_name]['Cost_price'] = stock_price * user_stock_quantity
        
        #Oppdater brukerens balanse
        user.balance -= stock_price * user_stock_quantity
        
        print(user.balance)
        
#4) Print brukeren og brukerens portefølje og balanse