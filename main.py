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

users = get_database()

if __name__ == '__main__':        
#1) En bruker opprettes basert på tekstinnput
    while True:
        username = input('Enter the username: ')
        #Sjekker om bruker finnes fra før. Hvis burker finnes hentes info fra bruker, hvis ikke opprettes ny bruker
        if username in users.keys():
            user = User(users[username]["user_name"], users[username]["balance"], users[username]["portfolio"])
        else:
            user = create_user(username)
            users[user.user_name] = user
        print(user.user_name, user.balance)

#2) Brukeren får tilbudet om å kjøpe en valgfri aksje og deretter antall av aksjen
        #Initier aksjen
        user_stock_name = input('Enter stock name: ')
        action = input('Choose buy, sell or plot: ')
        
        if action != "plot":
            user_stock_quantity = int(input('Enter stock quantity: '))
            stock = Stock(user_stock_name)
        
#3) Aksjedata hentes fra API (siste tilgjengelige sluttpris og dato), og brukerens portefølje(kostpris, aksjenavn, kjøpsdato og antall askjer) og balanse oppdateres
        #Hent aksjepris
            stock_price = float(stock.get_lastest_stock_price())
            stock_purchase_date = stock.get_stock_purchasedate()
        
        if action == 'buy':
            #4) Oppdatere brukeren og brukerens portefølje og balanse
            buy(user, user_stock_name, stock_price, stock_purchase_date, user_stock_quantity)
        elif action == "plot":
            stock_plot = plot_stock_performance(user_stock_name, user.portfolio[user_stock_name]["Purchase_date"])
            get_stock_return(user_stock_name, user.portfolio[user_stock_name]["Purchase_price"])
        else:
            continue

        
        print(user.balance)
        
        #Oppdater bruker i databasen (users)
        users[user.user_name] = user.__dict__
        
        # Sjekke om brukeren ønsker å fortsette
        x = input("Ferdig? Y/N: ")
        if x == "Y":
            break
        else:
            continue
        

#5) Oppdatere databasen
    update_database(users)