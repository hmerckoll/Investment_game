# -*- coding: utf-8 -*-
from users import User

username = 'vilde'
users = {}

def create_user(username):
    user_balance = float(input('Enter your balance: '))
    user = User(username, user_balance)
    users[user.user_name] = user
    
    #user = User(username, user_balance)
    #print(user.user_name, user.balance)

user = create_user(username)
