# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 06:53:42 2017

@author: Wian
"""


import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt


def __datetime(str_datetime):
    str_datetime = str(str_datetime)
    return datetime.strptime(str_datetime[2:], '%y/%m/%d %H:%M')
    
def Import_data():
    columns_to_keep1 = ['Times', 'Tin','Tout','Tam']
    dataframe1 = pd.read_csv("./Test_2_Data.csv", usecols=columns_to_keep1)
    
    columns_to_keep2 = ['GHI_CMP11','Time']
    dataframe2 = pd.read_csv("./Test_2_Sun_Data.csv", usecols=columns_to_keep2)
    
    Times_prelim = np.array(dataframe1['Times'])
    Tin = np.array(dataframe1['Tin'])
    Tout = np.array(dataframe1['Tout'])
    G_prelim = np.array(dataframe2['GHI_CMP11'])
    Time_prelim = np.array(dataframe2['Time'])
    Air_Temp = np.array(dataframe1['Tam'])
    
    G = [np.interp(t, Time_prelim, G_prelim) for t in Times_prelim]
    Times = []    
    Out = []
    In = []
    AT = []
    
    for i in range(len(Tin)):
#        a = Tin[i].replace(',','.')
#        print(float(a))
        In.append(float(Tin[i].replace(',','.')))
        Out.append(float(Tout[i].replace(',','.')))
        AT.append(float(Air_Temp[i].replace(',','.')))
        Times.append(float(Times_prelim[i]))
        
    return (Times, In, Out, G, AT)
    
#T,Ti,To,G,AT = Import_data()
#
#print(Ti)
#plt.plot(T,Ti)
#plt.plot(T,To)
#plt.plot(T,np.array(G))
#plt.plot(T,AT)
#plt.show()