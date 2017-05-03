# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:41:04 2017

@author: Wian
"""

from Parameters_main import Parameters
from Constants_main import Constants

def Integration_step(G, vwind, mf, Tlist, Tf_prev, del_t, del_z):
    A,alpha_sab,alpha_sg,Ca,Cab,Cf,Cg,Ci,din,eg,eg,ep,g,ka,kf,ki,Lc,Li,Ltube,rhoa,rhoab,rhof,rhog,rhoi,sigma,tau,Va,Vab,Vg,Vi = Constants()
    Tg, Ta, Tab, Tf, Ti, Tam = Tlist
    
    B,C,D,E,F,H,I,J,K,L,M,N,O,P,Q = Parameters(vwind, Tlist, mf, del_z)
    
    Tsky = 0.0552*Tam**1.5
    
    G = G/2.9
    
    dTgdt = C/B*(Tam-Tg) + D/B*(Tab**4-Tg**4) + E/B*(Ta-Tg) + F/B*G + Q/B*(Tsky**4 - Tg**4)
    dTadt = E/H*(Tg-Ta) + I/H*(Tab-Ta)
    dTabdt = J/K*G + D/K*(Tg**4-Tab**4) + I/K*(Ta-Tab) + L/K*(Ti-Tab) + M/K*(Tf-Tab)
    dTfdt = M/O*(Tab-Tf) - P/O*(Tf-Tf_prev) 
    dTidt = L/N*(Tab-Ti) + C/N*(Tam - Ti)

    Tg += del_t*dTgdt
    Ta += del_t*dTadt
    Tab += del_t*dTabdt
    Tf += del_t*dTfdt
    Ti += del_t*dTidt
    
#    print(Tg,Ta,Tab,Tf,Ti)
    return [Tg,Ta,Tab,Tf,Ti]
