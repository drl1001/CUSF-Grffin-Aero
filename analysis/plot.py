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
    
    time = np.linspace(0,37.7,num=100)
    #getting simulation data from Excel
    simul_data = convert_from_excel(filename='Griffin_Prelim_Flight_Profile_5Deg.xlsx',sheet='altitude-mach data')
    sim_altitude, sim_mach = np.split(simul_data,2,axis=1)
    simul_data2 = convert_from_excel(filename='Griffin_Prelim_Flight_Profile_5Deg.xlsx',sheet='time-mach data')
    sim_time, sim_mach2 = np.split(simul_data2,2,axis=1)

    simul_data3 = convert_from_excel(filename='Griffin_Prelim_Flight_Profile_5Deg.xlsx',sheet='altitude-dynamic pressure data')
    sim_time2, sim_dpressure = np.split(simul_data3,2,axis=1)

    fig, axes = plt.subplots(nrows=1,ncols=3)
    plt.tight_layout()

    #plotting the two sets of data

    axes[0].plot(sim_altitude/1000,sim_mach,label='simulated mach values against altitude up to 30km')
    axes[0].plot(height/1000,mach_values,label='critical mach values')
    axes[0].set_xlabel('Altitude /km')
    axes[0].set_ylabel('Mach number')
    axes[0].grid()
    axes[0].legend()

    axes[1].plot(sim_time,sim_mach2,label='simulated mach values against flight time')
    axes[1].plot(time,mach_values,label='critical mach values')
    axes[1].set_xlabel('Flight time /s')
    axes[1].set_ylabel('Mach number')
    axes[1].grid()
    axes[1].legend()

    axes[2].plot(sim_time2,sim_dpressure,label='simulated dynamic pressure against whole flight time')
    axes[2].set_xlabel('Flight time /s')
    axes[2].set_ylabel('Dynamic pressure /Pa')
    axes[2].grid()
    
    plt.title(f'Flutter analysis for {fin.name}',loc='center')
    plt.show()


