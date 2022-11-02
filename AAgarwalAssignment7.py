# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 21:01:10 2022

@author: ankia
"""

import pandas as pd
import matplotlib.pyplot as plt

def get_csv(web_link):
    df = pd.read_csv(web_link)
    return df

df=pd.read.csv(r'https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')

fig = plt.plot(df, x = 'AAPL_x', y = 'AAPL_y', title='Apple Share Prices over time (2014)')
fig.show()