# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 19:53:55 2017

@author: Wian
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 11:48:15 2017

@author: Wian
"""

from Integration_main import Integration_step
from Data_Exp import Import_data
from Constants_main import Constants
import matplotlib.pyplot as plt
import numpy as np

A,alpha_sab,alpha_sg,Ca,Cab,Cf,Cg,Ci,din,eg,eg,ep,g,ka,kf,ki,Lc,Li,Ltube,rhoa,rhoab,rhof,rhog,rhoi,sigma,tau,Va,Vab,Vg,Vi = Constants()
Nodes = 5
Times, Tin, Tout, G, Air_Temp = Import_data()
del_z = Ltube/Nodes
Temps = [290,285,300,300,280]
Tf_prev = Temps[3]
mf = 0.0944
iterations = 1000
tspan = np.linspace(0,Times[-1]*60,iterations)
del_t = (tspan[1] - tspan[0])

Tg_l = []
Ta_l = []
Tab_l = []
Ti_l = []

Tf_ult = [[Tf_prev]]

for z in range(Nodes):
    Tf_l = []
    Tf_prev = Tf_ult[-1][0]
    for t in tspan:
        Tam = np.interp(t, list(Times*60), Air_Temp)+273.15
        Tf_in = float(np.interp(t, list(Times*60), Tin)+273.15)
        Gstep = np.interp(t, list(Times*60), G)
        Temps = list(Temps) + [Tam]
        if z == 0:            
            Temps[3] = 300
        else:
            Temps[3] = float(np.interp(t, tspan,Tf_ult[-1])) 
        Temps = Integration_step(150,0.447,mf,Temps,Tf_prev, del_t, del_z)
        Tg_l.append(Temps[0])
        Ta_l.append(Temps[1])
        Tab_l.append(Temps[2])
        Tf_l.append(Temps[3])
        Ti_l.append(Temps[4])
#        print (str(t/tspan[-1]*100)[:5], ' % complete')
    Tf_ult.append(Tf_l)

#plt.plot(tspan/60, np.array(Tg_l)-273.15, label = 'Tg')
#plt.plot(tspan/60, np.array(Ta_l)-273.15, label = 'Ta')
plt.plot(list(tspan/60)*Nodes, np.array(Tab_l)-273.15, label = 'Tab')
plt.plot(tspan/60, np.array(Tf_ult[1])-273.15, label = 'Tf1')
plt.plot(tspan/60, np.array(Tf_ult[2])-273.15, label = 'Tf2')
plt.plot(tspan/60, np.array(Tf_ult[3])-273.15, label = 'Tf3')
plt.plot(tspan/60, np.array(Tf_ult[4])-273.15, label = 'Tf4')
plt.plot(tspan/60, np.array(Tf_ult[5])-273.15, label = 'Tf5')
#plt.plot(tspan/60, np.array(Ti_l)-273.15, label = 'Ti') 
#plt.plot(Times, Tout,'--', label='Exp_out')
#plt.plot(Times, Tin,'--', label='Exp_in')
plt.legend(loc = 0)   
    