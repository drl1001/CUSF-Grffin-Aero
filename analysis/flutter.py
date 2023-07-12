#contains flutter equation
from math import sqrt
from ambiance import Atmosphere


#need function to relate speed of sound and atmospheric temperature which varies with altitude. 
def flutter_eq(fin,h):
    '''returns critical mach number for given parameters:
    h - altitude (m)
    fin is a Fin object
    NB: all dimensions should be given as SI units'''

    

    #shear modulus in psi
<<<<<<< HEAD
    #effective shear modulus (we hope the formula is correct...) is the shear modulus of the solid fin (ie skin material) multiplied by ratio of natural frequencies of the composite to solid. 
    Ge = fin.skinshear * 0.000145038 * fin.cf / fin.sf 
=======
    #effective shear modulus (hopefully the formula is correct)
    Ge = fin.skinshear * 0.000145038 * fin.cf / fin.sf
>>>>>>> ccc633dab88da75d11f2c9a6e314c585307ffdab

       


    #critical velocity v_f at certain altitude depends on the speed of sound and atmospheric pressure at that altitude.
    
    atmosphere = Atmosphere(h)
    
    #speed of sound a (T in kelvin, R=8.3144598)
    a = sqrt(1.4*8.3144598*(atmosphere.temperature))

    #Panel aspect ratio AR

    #fin area A
    A = 0.5 * fin.semispan * (fin.tip + fin.root)
    AR = fin.semispan**2 / A

    #taper ratio TR
    TR = fin.tip / fin.root

    #pressure, p, at given altitude
    p = atmosphere.pressure #(p in pascals)
   
    #atmospheric pressure at sea-level p0 in Pa (only used in a ratio so units dont matter)
    p0 = 101325 
   
    #Mean aerodynamic chord c
    c = fin.root * 2/3 * ((1+TR+TR**2)/(1+TR)) 

    #parameter x (see NACA 4197)
    x = 39.3*AR**3 * 1/(fin.thick/c)**3 * 1/(AR+2)
    

    #critical mach number at a given altitude 
    mach = (sqrt(Ge/(x*(TR+1)/2*p/p0)))

    #critical Mach number mach at given altitude
    #mach = vf/a

    return mach


