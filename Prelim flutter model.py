from analysis.flutter import flutter_eq
import numpy as np
import matplotlib.pyplot as plt 
from ambiance import Atmosphere 

#generating some heights 
height = np.linspace(0,80e3,num=100)


#for reference dimensions are that of Aquila fins
c_r = 0.36
c_t = 0.16
fin_height = 0.2
#thickness unkown, so will assume to be 10mm = 0.01 m for now
thick = 0.01 

#using shear modulus Ge of phenolic resin, measured in Pa
Ge = 4.5e6

mach_values = []
for h in height:
    mach_no = flutter_eq(h,Ge,thick,c_r,c_t,fin_height)
    mach_values.append(mach_no)

plt.plot(height/1000,mach_values)
plt.xlabel('Altitude /km')
plt.ylabel('Critical Mach number')
plt.grid()
plt.show()
