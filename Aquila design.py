#dimensions of Aquila fin

from analysis.buildfin import Fin
from analysis.plot import plotdata

Fin_Aquila = Fin(name='Design Aquila',Gs=26.9e9,ts=0.6e-3,tc=9e-3,cr=0.360,ct=0.158,s=0.215)
plotdata(Fin_Aquila,30e3)