# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 11:26:30 2017

@author: Wian
"""

import pandas as pd
import numpy as np
from datetime import datetime


def __datetime(str_datetime):
    str_datetime = str(str_datetime)
    return datetime.strptime(str_datetime[2:], '%y/%m/%d %H:%M')
    
def Import_data():
    columns_to_keep = ['Date', 'GHI_CMP11','DNI_CHP1','DHI_CMP11', 'WS','Air_Temp']
    dataframe = pd.read_csv("./Weather_data_(2_hour)(1).csv", usecols=columns_to_keep)
    start_date = __datetime(dataframe['Date'][0])
    
    Times = np.array(dataframe['Date'])
    GHI = np.array(dataframe['GHI_CMP11'])
    DNI = np.array(dataframe['DNI_CHP1'])
    DHI = np.array(dataframe['DHI_CMP11'])
    WS = np.array(dataframe['WS'])
    Air_Temp = np.array(dataframe['Air_Temp'])
    
    for i in range(len(Times)):
        Day_time = ((__datetime(Times[i]) - start_date).days)*24*3600
        Seconds_time = (__datetime(Times[i]) - start_date).seconds
        Times[i] = Day_time + Seconds_time

    return (Times, GHI, DNI, DHI, WS, Air_Temp)