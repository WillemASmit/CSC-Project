# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 14:40:37 2017

@author: Wian
"""

import csv


def Constants():
    ss_values = {}

    with open('Constants.csv', 'r') as csvfile:
        ss = csv.reader(csvfile, delimiter=',')

        for row in ss:
            ss_values[row[0]] = float(row[1])
    
    A = ss_values["A"]
    a = ss_values["a"]
    a_Nu = ss_values["a_Nu"]
    a_Ra = ss_values["a_Ra"]
    alpha = ss_values["alpha"]
    b = ss_values["b"]
    b_Nu = ss_values["b_Nu"]
    Beta = ss_values["Beta"]
    ca = ss_values["ca"]
    cab = ss_values["cab"]
    cf = ss_values["cf"]
    cg = ss_values["cg"]
    ci = ss_values["ci"]
    dela = ss_values["dela"]
    delab = ss_values["delab"]
    delg = ss_values["delg"]
    deli = ss_values["deli"]
    din = ss_values["din"]
    eab = ss_values["eab"]
    eg = ss_values["eg"]
    ei = ss_values["ei"]
    g = ss_values["g"]
    ka = ss_values["ka"]
    kam = ss_values["kam"]
    kf = ss_values["kf"]
    ki = ss_values["ki"]
    L = ss_values["L"]
    m_Nu = ss_values["m_Nu"]
    mf = ss_values["mf"]
    n_Nu = ss_values["n_Nu"]
    Nu_inf = ss_values["Nu_inf"]
    p = ss_values["p"]
    rhoa = ss_values["rhoa"]
    rhoab = ss_values["rhoab"]
    rhof = ss_values["rhof"]
    rhog = ss_values["rhog"]
    rhoi = ss_values["rhoi"]
    rin = ss_values["rin"]
    rout = ss_values["rout"]
    sigma = ss_values["sigma"]
    taualpha = ss_values["taualpha"]
    v = ss_values["v"]
    
    return [A,a,a_Nu,a_Ra,alpha,b,b_Nu,Beta,ca,cab,cf,cg,ci,dela,delab,delg,deli,din,eab,eg,ei,g,ka,kam,kf,ki,L,m_Nu,mf,n_Nu,Nu_inf,p,rhoa,rhoab,rhof,rhog,rhoi,rin,rout,sigma,taualpha,v]
