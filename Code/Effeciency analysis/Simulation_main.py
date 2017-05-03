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
Nodes = 10
Times, Tin, Tout, G, Air_Temp = Import_data()
Tin = np.array(Tin) + 273.15
Tout = np.array(Tout) + 273.15

def mass_flow(t):
    return 0.09464

for mf in [0.09]:
    del_z = Ltube/Nodes
    Temps = np.array([290,290,290,290,290])
    
    iterations = 1000
    tspan = np.linspace(0,1*60,iterations)
    del_t = (tspan[1] - tspan[0])

    Tf_ult = []
    Tg_ult = []
    Ta_ult = []
    Tab_ult = []
    Ti_ult = []
    eff_list = []
    
        
    for t in tspan:
        Tam = 300
        Gstep = 800
    #    Temps = list(Temps) + [Tam]
        
        Tf_prev = 290
        
        for z in range(Nodes):
            Temps = list(Temps) + [Tam]
            Temps = Integration_step(Gstep,3,mf,Temps,Tf_prev, del_t, del_z)
            Tg, Ta, Tab, Tf, Ti = Temps
            Tf_prev = Tf
            
        print(mf, Cf, (Tf-290))
        Qsun = Gstep*A
        Q = mf*Cf*(Tf-290)
        
        eff = Q/Qsun
        
        print(Tf, Q, Qsun, eff)
        eff_list.append(eff)
        Tf_ult.append(Tf)
        Tg_ult.append(Tg)
        Ta_ult.append(Ta)
        Tab_ult.append(Tab)
        Ti_ult.append(Ti)
        print(str(t/tspan[-1]*100)[:5] + ' % complete')
    plt.plot(tspan/60, eff_list ,label = 'Flowrate = '+str(mf)+' kg/s')
    plt.plot(tspan/60, np.array(Tf_ult)-273.15, label="Temp = "+str(mf))
        

#plt.plot(np.array(Times)/60, Tin-273.15,'--', label='Exp_in')
plt.legend(loc = 0)   
plt.xlabel('Time (min)')
plt.ylabel('Efficiency')
#plt.ylim([0,500])
    