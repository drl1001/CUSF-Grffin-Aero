#contains flutter equation
from math import sqrt


#need function to relate speed of sound and atmospheric temperature which varies with altitude. 


def flutter_eq(a,G,t,cr,ct,s,p):
    '''returns critical mach number for given parameters:
    a - speed of sound at a given altitude
    G - shear modulus of material used for fin
    t - thickness of fin
    cr - root chord length
    ct - tip chord length
    s - height of fin
    p - atmospheric pressure at a given altitude
    NB: all dimensions are given as SI units'''

    #critical velocity v_f at certain altitude depends on the speed of sound and atmospheric pressure at that altitude.

    #Panel aspect ratio AR
    AR = 2*s / (ct + cr)

    #taper ratio TR
    TR = ct / cr

    #atmospheric pressure at sea-level p0 in Pa
    p0 = 101325 

    #critical velocity vf at a given altitude 
    vf = a*sqrt(G/(39.3*AR**3/((t/cr)**3*(AR+2)))*((TR+1)/2)*(p/p0))

    #critical Mach number mach at given altitude
    mach = vf * a

    return mach


