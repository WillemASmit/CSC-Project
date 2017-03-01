# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 11:48:15 2017

@author: Wian
"""

from Integration_main import Integration_step
from Data_import import Import_data
from Constants_main import Constants
import matplotlib.pyplot as plt
import numpy as np

A,alpha_sab,alpha_sg,Ca,Cab,Cf,Cg,Ci,din,eg,eg,ep,g,ka,kf,ki,Lc,Li,Ltube,rhoa,rhoab,rhof,rhog,rhoi,sigma,tau,Va,Vab,Vg,Vi = Constants()
Nodes = 1
Times, DNI, DHI, WS, Air_Temp = Import_data()
del_z = Ltube/Nodes
Temps = [290,285,300,300,280]
Tf_prev = Temps[3]
mf = 0.1
iterations = 10000
tspan = np.linspace(0,Times[-1],iterations)
del_t = (tspan[1] - tspan[0])
np.round

Tg_l = []
Ta_l = []
Tab_l = []
Tf_l = []
Ti_l = []

for t in tspan:
    Tam = np.interp(t, list(Times), Air_Temp)
    Gdni = np.interp(t,list(Times),DNI)
    Gdhi = np.interp(t,list(Times),DHI)
    vwind = np.interp(t,list(Times),WS)
    Temps = list(Temps) + [Tam]
    Temps = Integration_step(Gdni,vwind,mf,Temps,Tf_prev, del_t, del_z)
    Tg_l.append(Temps[0])
    Ta_l.append(Temps[1])
    Tab_l.append(Temps[2])
    Tf_l.append(Temps[3])
    Ti_l.append(Temps[4])
    print (str(t/tspan[-1]*100)[:5], ' % complete')
#    print(Temps)

plt.plot(tspan, Tg_l, label = 'Tg')
plt.plot(tspan, Ta_l, label = 'Ta')
plt.plot(tspan, Tab_l, label = 'Tab')
plt.plot(tspan, Tf_l, label = 'Tf')
plt.plot(tspan, Ti_l, label = 'Ti') 
plt.legend(loc = 0)   
    