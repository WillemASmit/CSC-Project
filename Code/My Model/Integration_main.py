# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:41:04 2017

@author: Wian
"""

from Parameters_main import Parameters

def Integration_step(G, vwind, mf, Tlist, Tf_prev, del_t, del_z):
    Tg, Ta, Tab, Tf, Ti, Tam = Tlist
    B,C,D,E,F,H,I,J,K,L,M,N,O,P,Q,R,S,V,W,X,Y = Parameters(G, vwind, Tlist, mf, del_z)
    Tsky = 0.0552*Tam**1.5
    
    dTgdt = Y/B*G - C/B*(Tg**4 - Tsky**4) - E/B*(Tg-Tam) - F/B*(Tg-Ta) #- D/B*G
    dTadt = I/H*(Tg-Ta) + J/H*(Tab-Ta)
    dTabdt = L/K*G - M/K*(Tab-Ta) - N/K*(Tab-Tf) - O/K*(Tab-Ti) - P/K*(Tab**4 - Tg**4)
    dTfdt = -V/W*(Tf-Tf_prev) + X/W*(Tab-Tf)
    dTidt = R/Q*(Tab-Ti) - S/Q*(Ti-Tam)
    
#    print(dTgdt, dTadt, dTabdt, dTfdt, dTidt)
    Tg += del_t*dTgdt
    Ta += del_t*dTadt
    Tab += del_t*dTabdt
    Tf += del_t*dTfdt
    Ti += del_t*dTidt
    return [Tg,Ta,Tab,Tf,Ti]
