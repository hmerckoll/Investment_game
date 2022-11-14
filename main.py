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
        print(f'Hello {user.user_name}, your current balance is: {user.balance}$. Good luck :D')

#2) Brukeren får tilbudet om å kjøpe en valgfri aksje og deretter antall av aksjen
        #Initier aksjen
        action = input('Choose buy or performance: ')
        
#3) Aksjedata hentes fra API (siste tilgjengelige sluttpris og dato), og brukerens portefølje(kostpris, aksjenavn, kjøpsdato og antall askjer) og balanse oppdateres
        
        if action == 'buy':
            #4) Oppdatere brukeren og brukerens portefølje og balanse
            user_stock_name = input('Choose between: IBM, MSFT or TSCO.LON to buy: ')
            user_stock_quantity = int(input('Enter stock quantity: '))
            
            stock = Stock(user_stock_name)
            stock_price = float(stock.get_lastest_stock_price())
            stock_purchase_date = stock.get_stock_purchasedate()
            
            #check if user has sufficent funds
            if stock_price*user_stock_quantity > user.balance:
                print('You don\'t have enough funds to execute this transaction')
                users[user.user_name] = user.__dict__
                continue
            
            buy(user, user_stock_name, stock_price, stock_purchase_date, user_stock_quantity)
            
        elif action == "performance":
            if user.portfolio == {}:
                print('You don\'t have any stock performance')
                users[user.user_name] = user.__dict__
                continue
            
            #Plot perfromance for each stock in the portfolio
            for stock in user.portfolio.keys():
                stock_plot = plot_stock_performance(stock, user.portfolio[stock]["Purchase_date"])
                #stock_plot.legend()
                
            get_portfolio_return(user.portfolio)
        else:
            continue

        
        print(f' Your current balance is: {user.balance}$')
        
        #Oppdater bruker i databasen (users)
        users[user.user_name] = user.__dict__
        
        # Sjekke om brukeren ønsker å fortsette
        x = input("Do you want to continue? Y/N: ")
        if x == "N":
            break
        else:
            continue
    

#5) Oppdatere databasen
    update_database(users)
    
    

    



