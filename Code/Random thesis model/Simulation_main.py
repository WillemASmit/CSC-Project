# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 10:04:38 2017

@author: Wian
"""

import numpy as np
from scipy.optimize import fsolve
from Parameters_main import Parameters

def Simulation_solve(Vars, Temps,del_t, del_z):
    Tg_n, Ta_n, Tab_n, Tf_n, Ti_n, G_n = Vars
    Tg, Ta, Tab, Tf, Ti, Tam = Temps
    B,C,D,E,F,G,H,J,K,L,M,O,P,Q,R,S,U,V,W,X = Parameters(Temps,del_t,del_z)
    
    Eqn1 = -Tg_n + 1/(F*del_t)*Tg + B/F*Tam + C/F*Tab_n + D/F*Ta_n + E/F*G_n
    Eqn2 = -Ta_n + 1/(H*del_t)*Ta + G/H*(Tg_n + Tab_n)
    Eqn3 = -Tab_n + 1/(Q*del_t)*Tab + K/Q*G_n + L/Q*Tg_n + M/Q*Ta_n + O/Q*Tf_n + P/Q*Ti_n
    Eqn4 = -Tf_n + 1/(U*del_t)*Tf + R/U*Tab + S/(U*del_z)*Tf
    Eqn5 = -Ti_n + 1/(X*del_t)*Ti + V/X*Tab_n + W/X*Tam
    Eqn6 = -G_n + G*(Ta**2)/(Ta_n**2)
    
    return [Eqn1, Eqn2, Eqn3, Eqn4, Eqn5, Eqn6]

print(fsolve(Simulation_solve, [300,360,300,290,280,65],args=([360,370,280,300,290,310],0.05,0.1)))
