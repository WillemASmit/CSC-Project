# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 09:29:39 2017

@author: Wian
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def x_e(row):
    return row['WS']*np.cos(row['WD'] + np.pi/2)
    
def y_e(row):
    return row['WS']*np.sin(row['WD'] + np.pi/2)
    
columns_to_keep = ['Date', 'WS', 'WD','Air_Temp']
dataframe = pd.read_csv("./Weather_data.csv", usecols=columns_to_keep)
    
dataframe['xplots'] = dataframe.apply(x_e, axis=1)
dataframe['yplots'] = dataframe.apply(y_e, axis=1)

plt.plot(dataframe['xplots'], dataframe['yplots'], ',')
plt.plot([-10,10],[0,0],'k')
plt.plot([0,0], [-10,10],'k')
plt.xlim([-10,10])
plt.ylim([-10,10])
plt.show()