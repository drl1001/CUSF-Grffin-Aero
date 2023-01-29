
import numpy as np
import matplotlib.pyplot as plt 
from ambiance import Atmosphere 

#generating some heights 
h = np.linspace(0,100e3,num=1000)
atmosphere = Atmosphere(h)

#for reference dimensions are that of Aquila fins
r = 0.36
t = 0.16
s = 0.2
#thickness unkown, so will assume to be 10mm = 0.01 m for now

plt.plot(atmosphere.temperature_in_celcius,h/1000)
plt.xlabel('Height /km')
plt.ylabel('Temperature /C')
plt.grid
plt.show()