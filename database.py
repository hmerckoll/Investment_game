# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 13:15:11 2022

@author: vfjeldstad
"""
import json

def update_database(users):
    with open('database.txt', mode = 'w') as file:
        str(users)
        file.write(json.dumps(users))

def get_database():    
    with open('database.txt', mode = 'r') as file:
        dict1 = file.read()
        dict2 = json.loads(dict1)
        #print(type(dict2))
        return dict2

    