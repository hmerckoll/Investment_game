# -*- coding: utf-8 -*-
from users import User
from stock import Stock
from datapull import*


def create_user(username):
    user_balance = float(input('Enter your balance: '))
    user = User(username, user_balance)
    return user

#Oppdatere brukerens portefølje
def buy(user, user_stock_name, stock_price, stock_purchase_date, user_stock_quantity):
    user.portfolio[user_stock_name] = {}
    user.portfolio[user_stock_name]['Purchase_date'] = stock_purchase_date
    user.portfolio[user_stock_name]['Purchase_price'] = stock_price
    user.portfolio[user_stock_name]['Purchase_quantity'] = user_stock_quantity
    user.portfolio[user_stock_name]['Cost_price'] = stock_price * user_stock_quantity
    
    #Oppdater brukerens balanse
    user.balance -= stock_price * user_stock_quantity
    
def plot_stock_performance(stock_name, purchase_date):
    df = datapull(stock_name)
    df_x = str(df.index[:])
    pos = df_x.find('2022-11-10 16:15:00')
    print(pos)
    #df_purchase_date = df[df.index[] >= purchase_date]
    #df_dates = str(df.index[:])
    #print(df_dates)
    #df['close'].plot()
    
plot_stock_performance("IBM", "123")
    