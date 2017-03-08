# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 17:02:12 2017

@author: Wian
"""

import numpy as np
from Constants_main import Constants

A,alpha_sab,alpha_sg,Ca,Cab,Cf,Cg,Ci,din,eg,eg,ep,g,ka,kf,ki,Lc,Li,Ltube,rhoa,rhoab,rhof,rhog,rhoi,sigma,tau,Va,Vab,Vg,Vi = Constants()

def hgam_fun(v_wind, Tlist,del_z): #hiam has same function
    Tg, Ta, Tab, Tf, Ti, Tam = Tlist
    mu = 1.849E-5
    Re = rhoa*v_wind*Lc/mu
    Pr = 0.7202
    Nu = 0
    if Re>5E5:
        Nu = 0.037*Re**0.8*Pr**(1/3)
    elif Re<5E5:
        Nu = 0.664*Re**0.5*Pr**(1/3)
    return Nu*ka/Lc
    
def hf_fun(mf, Tlist,del_z):
    Tg, Ta, Tab, Tf, Ti, Tam = Tlist
    muf = 8.9E-4
    V = mf/(np.pi/4*din**2)/rhof
    Re = rhof*V*Ltube/muf
    Pr = 1.5
    Nu = 0
    if Re>2000:
        Nu = 0.023*Re**0.8*Pr**0.4  #kyk maar net na die n van 0.4
    elif Re>2000:
        Nu = 3.66 + (0.065*din/Ltube*Re*Pr)/(1+0.04*((din/Ltube)*Re*Pr)**(2/3))
    return Nu*kf/Ltube
    
def hga_fun(Tlist,del_z):
    Tg, Ta, Tab, Tf, Ti, Tam = Tlist
    Pr = 0.7202
    v = 1.568E-5
    p = 6
    L = A/p
    Beta = 1/((Tg+Ta)/2)
    Ra = abs(g*Beta*(Tg-Ta)*L**3/(v**2)*Pr)
    Nu = 0
    if Ra<10E7:
        Nu = 0.54*Ra**(1/4)
    elif Ra>10E7:
        Nu = 0.15*Ra**(1/3)
    return Nu*ka/Lc
    
def haab_fun(Tlist,del_z):
    Tg, Ta, Tab, Tf, Ti, Tam = Tlist
    Pr = 0.7202
    v = 1.568E-5
    p = 6
    L = A/p
    Beta = 1/((Ta+Tf)/2)
    Ra = abs(g*Beta*(Tab-Ta)*L**3/(v**2)*Pr)
#    print(Tlist)
#    print(Beta)
    Nu = 0.27*Ra**(1/4)
    return Nu*ka/Lc

def Parameters(G, vwind, Tlist, mf, del_z):
    A = Constants()[0]
    hgam = hgam_fun(vwind,Tlist,del_z)
    hga = hga_fun(Tlist,del_z)
    haab = haab_fun(Tlist,del_z)
    hf = hf_fun(mf,Tlist,del_z)
    hiam = hgam
    Af = din*np.pi*del_z
    A = A/Lc*del_z
#    print (hgam, hga, haab, hf, hiam)
    
    B = rhog*Vg*Cg
    C = eg*sigma
    D = tau*G*A
    E = hgam*A
    F = hga*A
    H = Ca*rhoa*Va #rhoa
    I = hga*A
    J = haab*A
    K = Cab*rhoab*Vab
    L = tau*alpha_sab*G*A
    M = haab*A
    N = hf*Af
    O = ki*A/Li
    P = sigma*A/((1/ep)+(1/eg)-1)
    Q = Ci*rhoi*Vi
    R = ki*A/Li
    S = hiam*A
    V = mf*Cf/del_z
    W = rhof*Af*Cf
    X = hf*np.pi*din
    Y = alpha_sg*A
    
    return [B,C,D,E,F,H,I,J,K,L,M,N,O,P,Q,R,S,V,W,X,Y]
