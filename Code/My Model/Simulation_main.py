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
from Data_import import Import_data
from Constants_main import Constants
import matplotlib.pyplot as plt
import numpy as np

A,alpha_sab,alpha_sg,Ca,Cab,Cf,Cg,Ci,din,eg,eg,ep,g,ka,kf,ki,Lc,Li,Ltube,rhoa,rhoab,rhof,rhog,rhoi,sigma,tau,Va,Vab,Vg,Vi = Constants()
Nodes = 5
Times, GHI, DNI, DHI, WS, Air_Temp = Import_data()
del_z = Ltube/Nodes
Temps = [290,280,350,350,280]
Tf_prev = Temps[3]
mf = 0.0944
iterations = 2000
tspan = np.linspace(0,Times[-1],iterations)
#tspan = np.linspace(0, 7200, iterations)
del_t = (tspan[1] - tspan[0])

Tf_ult = [[Tf_prev]]
Tg_ult = []
Ta_ult = []
Tab_ult = []
Ti_ult = []

for z in range(Nodes):
    Tf_l = []
    Tg_l = []
    Ta_l = []
    Tab_l = []
    Ti_l = []
    Tf_prev = Tf_ult[-1][0]
    
    for t in tspan:
        Tam = np.interp(t, list(Times*60), Air_Temp)+273.15
        Gstep = np.interp(t, list(Times*60), GHI)
        WSstep = np.interp(t, list(Times*60), WS)
        Temps = list(Temps) + [Tam]
        if z == 0 and t == 0:            
            Temps[3] = 298.15
        elif z!=0 and t==0:
            Temps[0] = float(np.interp(t, tspan,Tg_ult[-1]))
            Temps[1] = float(np.interp(t, tspan,Ta_ult[-1]))
            Temps[2] = float(np.interp(t, tspan,Tab_ult[-1]))
            Temps[3] = float(np.interp(t, tspan,Tf_ult[-1]))
            Temps[4] = float(np.interp(t, tspan,Ti_ult[-1]))
        Temps = Integration_step(Gstep,WSstep,mf,Temps,Tf_prev, del_t, del_z)
        Tg_l.append(Temps[0])
        Ta_l.append(Temps[1])
        Tab_l.append(Temps[2])
        Tf_l.append(Temps[3])
        Ti_l.append(Temps[4])
#        print (str(t/tspan[-1]*100)[:5], ' % complete')
    Tg_ult.append(Tg_l)
    Ta_ult.append(Ta_l)
    Tab_ult.append(Tab_l)
    Ti_ult.append(Ti_l)
    Tf_ult.append(Tf_l)

#plt.plot(list(tspan/60)*Nodes, np.array(Tg_l)-273.15, label = 'Tg')
#plt.plot(list(tspan/60)*Nodes, np.array(Ta_l)-273.15, label = 'Ta')
plt.plot(tspan/60, np.array(Tab_ult[0])-273.15, label = 'Tab')
plt.plot(tspan/60, np.array(Tab_ult[1])-273.15, label = 'Tab')
plt.plot(tspan/60, np.array(Tab_ult[2])-273.15, label = 'Tab')
plt.plot(tspan/60, np.array(Tab_ult[3])-273.15, label = 'Tab')
plt.plot(tspan/60, np.array(Tab_ult[4])-273.15, label = 'Tab')
plt.plot(tspan/60, np.array(Tf_ult[1])-273.15, label = 'Tf1')
plt.plot(tspan/60, np.array(Tf_ult[2])-273.15, label = 'Tf2')
plt.plot(tspan/60, np.array(Tf_ult[3])-273.15, label = 'Tf3')
plt.plot(tspan/60, np.array(Tf_ult[4])-273.15, label = 'Tf4')
plt.plot(tspan/60, np.array(Tf_ult[5])-273.15, label = 'Tf5')
#plt.plot(list(tspan/60)*Nodes, np.array(Ti_l)-273.15, label = 'Ti') 
#plt.plot(Times, Tout,'--', label='Exp_out')
#plt.plot(Times, Tin,'--', label='Exp_in')
plt.legend(loc = 0)   
    