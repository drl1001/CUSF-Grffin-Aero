#contains flutter equation
from math import sqrt
from ambiance import Atmosphere

#need function to relate speed of sound and atmospheric temperature which varies with altitude. 
def flutter_eq(h,G,t,cr,ct,s):
    '''returns critical mach number for given parameters:
    h - altitude
    G - shear modulus of material used for fin
    t - thickness of fin
    cr - root chord length
    ct - tip chord length
    s - height of fin
    NB: all dimensions should be given as SI units'''

    #shear modulus in psi
    Ge = G * (.9144/36)**2 * 1/9.80665 * 1/.45359237 #NB:NOT ACTUAL SHEAR MODULUS. equation uses effective shear modulus, which is different 

    #critical velocity v_f at certain altitude depends on the speed of sound and atmospheric pressure at that altitude.
    atmosphere = Atmosphere(h)
    
    #speed of sound a (T in kelvin, R=8.3144598)
    a = sqrt(1.4*8.3144598*(atmosphere.temperature))

    #Panel aspect ratio AR
    AR = 2*s / (ct + cr)

    #taper ratio TR
    TR = ct / cr

    #pressure, p, at given altitude
    p = atmosphere.pressure #(p in pascals)
   
    #atmospheric pressure at sea-level p0 in Pa (only used in a ratio so units dont matter)
    p0 = 101325 
   
    #Mean aerodynamic chord c
    c = cr * 2/3 * ((1+TR+TR**2)/(1+TR)) 

    #parameter x (see NACA 4197)
    x = 39.3*AR**3 * 1/(t/c)**3 * 1/(AR+2)
    
    #critical mach number at a given altitude 
    mach = sqrt(Ge/(x*(TR+1)/2*p/p0))

    #critical Mach number mach at given altitude
    #mach = vf/a

    return mach


