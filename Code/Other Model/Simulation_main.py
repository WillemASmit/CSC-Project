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
from Data_Exp import Import_data
from Constants_main import Constants
import matplotlib.pyplot as plt
import numpy as np

A,alpha_sab,alpha_sg,Ca,Cab,Cf,Cg,Ci,din,eg,eg,ep,g,ka,kf,ki,Lc,Li,Ltube,rhoa,rhoab,rhof,rhog,rhoi,sigma,tau,Va,Vab,Vg,Vi = Constants()
Nodes = 1
Times, Tin, Tout, G, Air_Temp = Import_data()
Tin = np.array(Tin) + 273.15
Tout = np.array(Tout) + 273.15

def mass_flow(t):
    return 0.09464

for Nodes in [20]:
    del_z = Ltube/Nodes
    Temps = np.array([35,35,30,Tin[0]-273.15,35])+273.15
    
    iterations = 2000
    tspan = np.linspace(0,Times[-1],iterations)
    del_t = (tspan[1] - tspan[0])

    Tf_ult = []
    Tg_ult = []
    Ta_ult = []
    Tab_ult = []
    Ti_ult = []
    
        
    for t in tspan:
        Tam = np.interp(t, Times, Air_Temp) + 273.15
        Gstep = np.interp(t, list(Times), G)
    #    Temps = list(Temps) + [Tam]
        
        Tf_prev = float(np.interp(t, np.array(Times), Tin))
        
        for z in range(Nodes):
            mf = mass_flow(t)
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
    plt.plot(tspan/60, np.array(Tf_ult)-273.15, label = 'Predicted Temperature ')
#    plt.plot(list(tspan/60), np.array(Ti_ult)-273.15, label = 'Ti') 
plt.plot(np.array(Times)/60, Tout-273.15,'--', label='Measured Temperature')
#plt.plot(np.array(Times)/60, Tin-273.15,'--', label='Exp_in')
plt.legend(loc = 0)   
plt.xlabel('Time (min)')
plt.ylabel('Temperature ($^o$C)')
#plt.ylim([0,500])
    