# module that plots the critical mach number vs altitude data for a certain fin design against the flight simulation data imported from Excel. 
from .simdata import convert_from_excel
from .flutter import flutter_eq
import numpy as np
import matplotlib.pyplot as plt

def plotdata(fin,altitude):
    '''Plots critical mach number vs altitude data analysed for a certain fin design and compare it with the smulation data from Excel
    fin - a Fin object
    altitude - altitude up to which the flutter is analysed
    '''


    #generating some heights up to 30 km - all that is needed for significant flutter to occur. 
    height = np.linspace(0,30e3,num=100)
    mach_values = []
    for h in height:
        mach_no = flutter_eq(fin,h)
        mach_values.append(mach_no)
    
    #getting simulation data from Excel
    simul_data = convert_from_excel(filename='Griffin_Prelim_Flight_Profile_5Deg.xlsx',sheet='altitude-mach data')
    sim_altitude, sim_mach = np.split(simul_data,2,axis=1)

    #plotting the two sets of data
    plt.plot(sim_altitude/1000,sim_mach,label='simulated mach values')
    plt.plot(height/1000,mach_values,label='critical mach values')
    plt.xlabel('Altitude /km')
    plt.ylabel('Mach number')
    plt.title(f'Flutter analysis for {fin.name}')
    plt.grid()
    plt.legend()
    plt.show()
