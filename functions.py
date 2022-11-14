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
    df = df.iloc[::-1]
    df["close"].loc[purchase_date:].plot()
    
def get_stock_return(stock_name, purchase_price, latest_price):
    stock_return = round(((latest_price-purchase_price)/purchase_price)*100,2)
    print(f"Your stock return for the period is: {stock_return}%.")
    
    
def get_portfolio_return(portfolio):
    portfolio_cost_price = 0
    portfolio_current_value = 0
    for stock in portfolio.keys():
        portfolio_cost_price += portfolio[stock]['Cost_price']
        share = Stock(stock)
        portfolio_current_value += share.get_latest_stock_price_performance()*portfolio[stock]['Purchase_quantity']
    portfolio_return = round(((portfolio_current_value-portfolio_cost_price)/portfolio_cost_price)*100,2)
    print(f"Your portfolio return for the period is: {portfolio_return}%.")
    
