# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 19:54:48 2017

@author: Wian
"""

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
    columns_to_keep = ['Time', 'Tin','Tout', 'G','Tam']
    dataframe = pd.read_csv("./Exp_Thesis.csv", usecols=columns_to_keep)
    
    Times = np.array(dataframe['Time'])
    Tin = np.array(dataframe['Tin'])
    Tout = np.array(dataframe['Tout'])
    G = np.array(dataframe['G'])
    Air_Temp = np.array(dataframe['Tam'])
    
    
    return (Times, Tin, Tout, G, Air_Temp)