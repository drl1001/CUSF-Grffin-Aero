#testing the code for the Orion fin design 

from analysis.buildfin import Fin
from analysis.plot import plotdata

Fin_Orion = Fin(name='Design Orion',Gs=26e9,ts=1.5e-3,tc=11e-3,cr=0.589,ct=0.4,s=0.68)
plotdata(Fin_Orion,30e3)