# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 11:56:39 2022

@author: hmerckoll
"""

from datapull import datapull
from users import Users

df = datapull()

if __name__ == '__main__':
    print(df)