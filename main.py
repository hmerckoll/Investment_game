# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 11:56:39 2022

@author: hmerckoll
"""

from datapull import datapull
from users import User
from stock import Stock
from functions import *
from database import *

users = {}

if __name__ == '__main__':        
#1) En bruker opprettes basert på tekstinnput
    while True:
        username = input('Enter the username: ')
        #Sjekker om bruker finnes fra før. Hvis burker finnes hentes info fra bruker, hvis ikke opprettes ny bruker
        if username in users.keys():
            user = users[username]
        else:
            user = create_user(username)
            users[user.user_name] = user
        print(user.user_name, user.balance)

#2) Brukeren får tilbudet om å kjøpe en valgfri aksje og deretter antall av aksjen
        #Initier aksjen
        user_stock_name = input('Enter stock name: ')
        action = input('Choose buy or sell: ')
        user_stock_quantity = int(input('Enter stock quantity: '))
        stock = Stock(user_stock_name)
        
#3) Aksjedata hentes fra API (siste tilgjengelige sluttpris og dato), og brukerens portefølje(kostpris, aksjenavn, kjøpsdato og antall askjer) og balanse oppdateres
        #Hent aksjepris
        stock_price = float(stock.get_lastest_stock_price())
        stock_purchase_date = stock.get_stock_purchasedate()
        
        if action == 'buy':
            buy(user, user_stock_name, stock_price, stock_purchase_date, user_stock_quantity)
        else:
            continue

        
        print(user.balance)
        
        #Oppdater bruker i databasen (users)
        users[user.user_name] = user
#4) Print brukeren og brukerens portefølje og balanse

        update_database(users)