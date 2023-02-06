from analysis.flutter import flutter_eq
import numpy as np
import matplotlib.pyplot as plt 
from analysis.simdata import convert_from_excel 

#generating some heights 
height = np.linspace(0,30e3,num=100)


#for reference dimensions are that of Aquila fins - now scaled up according to SolidWork simulation
c_r = 0.9
c_t = 0.4
fin_height = 0.4
#from computation and trial and error, thickness is best at 7mm
thick = 0.007

#using shear modulus of 7050 Aluminium 
Ge = 26.9e9

mach_values = []
for h in height:
    mach_no = flutter_eq(h,Ge,thick,c_r,c_t,fin_height)
    mach_values.append(mach_no)

simul_data = convert_from_excel(filename='Griffin_Prelim_Flight_Profile_5Deg.xlsx',sheet='altitude-mach data')
sim_altitude, sim_mach = np.split(simul_data,2,axis=1)

plt.plot(sim_altitude/1000,sim_mach,label='simulated mach values')
plt.plot(height/1000,mach_values,label='critical mach values')
plt.xlabel('Altitude /km')
plt.ylabel('Mach number')
plt.grid()
plt.legend()
plt.show()

#print('This value of shear modulus combined with the dimensions give a critical Mach number of around 7 at 23km which is above peak velocity from the Griffin Prelim Flight profile (which gives a peak velocity of Mach 6 with safety factor of 10%).')