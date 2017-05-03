import numpy as np
from Constants_main import Constants

A, alpha_sab, alpha_sg, Ca, Cab, Cf, Cg, Ci, din, eg, eg, ep, g, ka, kf, ki, \
    Lc, Li, Ltube, rhoa, rhoab, rhof, rhog, rhoi, sigma, tau, Va, Vab, Vg, Vi\
    = Constants()


def hgam_fun(v_wind, Tlist, del_z):
    Tg, Ta, Tab, Tf, Ti, Tam = Tlist
    mu = 1.849E-5
    Re = rhoa*v_wind*Lc/mu
    Pr = 0.7202
    if Re > 5E5:
        Nu = 0.037*Re**0.8*Pr**(1/3)
    else:
        Nu = 0.664*Re**0.5*Pr**(1/3)
    return Nu*ka/Lc


def hf_fun(mf, Tlist, del_z):
    Tg, Ta, Tab, Tf, Ti, Tam = Tlist
    muf = 8.9E-4
    u = mf/(np.pi/4*din**2)/rhof/8
    Re = rhof*u*din/muf
    Pr = 1.5
    if Re > 2000:
        Nu = 0.023*Re**0.8*Pr**0.4
    else:
        Nu = 3.66 + (0.065*din/Ltube*Re*Pr)/(1+0.04*((din/Ltube)*Re*Pr)**(2/3))
    return Nu*kf/din


def hga_fun(Tlist, del_z):
    Tg, Ta, Tab, Tf, Ti, Tam = Tlist
    Pr = 0.7202
    v = 1.568E-5
    p = 6
    L = A/p
    Beta = 1/((Tg+Ta)/2)
    Ra = abs(g*Beta*(Tg-Ta)*L**3/(v**2)*Pr)
    if Ra < 10E7:
        Nu = 0.54*Ra**(1/4)
    else:
        Nu = 0.15*Ra**(1/3)
    return Nu*ka/Lc


def haab_fun(Tlist, del_z):
    Tg, Ta, Tab, Tf, Ti, Tam = Tlist
    Pr = 0.7202
    v = 1.568E-5
    p = 6
    L = A/p
    Beta = 1/((Ta+Tab)/2)
    Ra = abs(g*Beta*(Tab-Ta)*L**3/(v**2)*Pr)
    if Ra < 10E7:
        Nu = 0.54*Ra**(1/4)
    else:
        Nu = 0.15*Ra**(1/3)
    return Nu*ka/Lc


def Parameters(vwind, Tlist, mf, del_z):
    A = Constants()[0]
    hgam = hgam_fun(vwind, Tlist, del_z)
    hga = hga_fun(Tlist, del_z)
    haab = haab_fun(Tlist, del_z)
    hf = hf_fun(mf, Tlist, del_z)
    hr1 = sigma/(1/ep + 1/eg - 1)
    Vol_correct = del_z/Lc
    b = A/Lc

    B = Cg*rhog*Vg*Vol_correct
    C = hgam*b*del_z
    D = hr1*b*del_z
    E = hga*b*del_z
    F = tau*alpha_sg*b*del_z
    H = Ca*rhoa*Va*Vol_correct
    I = haab*b*del_z
    J = alpha_sab*b*del_z
    K = Cab*rhoab*Vab*Vol_correct
    L = ki*b*del_z/Li
    M = np.pi*din*del_z*hf*8
    N = Ci*rhoi*Vi*Vol_correct
    O = Cf*rhof*(np.pi/4*din**2)*del_z*8
    P = mf*Cf
    Q = sigma*b*del_z

    return [B, C, D, E, F, H, I, J, K, L, M, N, O, P, Q]
