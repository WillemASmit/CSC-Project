# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 10:22:36 2017

@author: Wian
"""

import numpy as np
from Constants_main import Constants

def Parameters(Temps, del_t, del_z):
    Tg, Ta, Tab, Tf, Ti, Tam = Temps
    A,a,a_Nu,a_Ra,alpha,b,b_Nu,Beta,ca,cab,cf,cg,ci,dela,delab,delg,deli,din,eab,eg,ei,g,ka,kam,kf,ki,L,m_Nu,mf,n_Nu,Nu_inf,p,rhoa,rhoab,rhof,rhog,rhoi,rin,rout,sigma,taualpha,v = Constants()
    del_T = Tf-Ti    
    Ream, Ref = 10000, 12000
    Pram, Prf = 12, 24    
    
    def Nua_fun(Beta, Raa):
        Anu = 1 - 1708/(Raa*np.cos(Beta))
        Bnu = (Raa*np.cos(Beta)/5830)*(1/3) - 1
        Cnu = 1.44*(1 - (1708*np.sin(1.8*Beta))**1.6/(Raa*np.cos(Beta)))
        if Anu<0: Anu=0
        if Bnu<0: Bnu=0
        return 1 + Cnu*Anu + Bnu
        
    hr1 = sigma*(Tab**2 + Tg**2)*(Tab*Tg)/((1/eab)+(1/eg)-1)
    Raa = g*Beta*del_T*L**3/(v*a_Ra)
    Nua = Nua_fun(Beta, Raa)
    hc1 = Nua*ka/dela
    
    Nuam = 0.86*Ream**2*Pram**2
    delta = 4*a*b/np.sqrt(a**2 + b**2)
    hc2 = Nuam*kam/delta
    
    Tsky = 0.0552*Tam**1.5
    hgam = sigma*eg*(Tg**4-Tsky**4)/(Tg-Tam) + hc2
    hiam = sigma*ei*(Ti**4-Tsky**4)/(Ti-Tam) + hc2
    
    Nuf = Nu_inf + a_Nu*(Ref*Prf*(din/L))**m_Nu/(1+(b_Nu*(Ref*Prf*(din/L))**n_Nu))
    hf = Nuf*kf/din
    
    B = hgam/(cg*rhog*delg)
    C = hr1/(cg*rhog*delg)
    D = hc1/(cg*rhog*delg)
    E = alpha/(cg*rhog*delg)
    F = 1/del_t + B + C + D
    J = cab*Tab*rhoab*Tab*(p*delab + np.pi*(rout**2 - rin**2))
    K = p*(taualpha)/J
    L = hr1*p/J
    M = hc1*p/J
    O = np.pi*din*hf/J
    P = p*ki/(J*delta)
    G = hc1*p/(ca*Ta*rhoa*Ta*(p*delab + np.pi*rout**2))
    H = 1/del_t + 2*G
    Q = 1/del_t + L + M + O + P
    R = np.pi*din*hf/(cf*Tf*rhof*Tf*A)
    S = mf/(rhof*Tf*A)
    U = 1/del_t + R + S/del_z
    V = 2*ki/(ci*rhoi*deli**2)
    W = 2*hiam/(ci*rhoi*deli)
    X = 1/del_t + V + W
    
    return [B,C,D,E,F,G,H,J,K,L,M,O,P,Q,R,S,U,V,W,X]