# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 06:52:11 2017

@author: Wian
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 19:53:55 2017

@author: Wian
"""

from Integration_main import Integration_step
from Data_Experimental import Import_data
from Constants_main import Constants
import matplotlib.pyplot as plt
import numpy as np

A,alpha_sab,alpha_sg,Ca,Cab,Cf,Cg,Ci,din,eg,eg,ep,g,ka,kf,ki,Lc,Li,Ltube,rhoa,rhoab,rhof,rhog,rhoi,sigma,tau,Va,Vab,Vg,Vi = Constants()
Nodes = 1
Times, Tin, Tout, G, Air_Temp = Import_data()
Tin = np.array(Tin) + 273.15
Tout = np.array(Tout) + 273.15

def mass_flow(t):
    if t<34*60:
        return 0.01296
    elif t<55*60:
        return 0.0327
    else:
        return 0.007788

for Nodes in [20]:
    del_z = Ltube/Nodes
    Temps = np.array([35,35,25,37,35])+273.15
    
    iterations = 2000
    tspan = np.linspace(0,Times[-1],iterations)
    del_t = (tspan[1] - tspan[0])

    Tf_ult = []
    Tg_ult = []
    Ta_ult = []
    Tab_ult = []
    Ti_ult = []
    Tmax = []
    Eff = []
        
    for t in tspan:
        Tam = np.interp(t, Times, Air_Temp) + 273.15
        Gstep = np.interp(t, list(Times), G)

        mf = mass_flow(t)
        Tf_prev = float(np.interp(t, np.array(Times), Tin))
        
        Tmax.append(Gstep/2.9*A/mf/Cf + Tf_prev)        
        
        for z in range(Nodes):
            Temps = list(Temps) + [Tam]
            Temps = Integration_step(Gstep,3,mf,Temps,Tf_prev, del_t, del_z)
            Tg, Ta, Tab, Tf, Ti = Temps
            Tf_prev = Tf
        
        Tf_ult.append(Tf)
        Tg_ult.append(Tg)
        Ta_ult.append(Ta)
        Tab_ult.append(Tab)
        Ti_ult.append(Ti)
        print(str(t/tspan[-1]*100)[:5] + ' % complete')
    
#    plt.plot(list(tspan/60), np.array(Tg_ult)-273.15, label = 'Tg')
#    plt.plot(list(tspan/60), np.array(Ta_ult)-273.15, label = 'Ta')
#    plt.plot(tspan/60, np.array(Tab_ult)-273.15, label = 'Tab: '+str(Nodes))
    plt.plot(tspan/60, np.array(Tf_ult)-273.15, label = 'Predicted Temperature')
#    plt.plot(list(tspan/60), np.array(Ti_ult)-273.15, label = 'Ti') 
    
plt.plot(np.array(Times)/60, Tout-273.15,',', label='Measured Temperature')
plt.plot(tspan/60, np.array(Tmax) -273.15,label='Maximum Temperature')

plt.xlabel('Time (min)')
plt.ylabel('Temperature ($^o$C)')
plt.legend(loc = 0)   

error = [abs(np.interp(t,tspan,Tf_ult) - np.interp(t,np.array(Times),Tout)) for t in tspan]

print('Standard deviation of error = ',np.std(error))
print('Average error = ',np.average(error))