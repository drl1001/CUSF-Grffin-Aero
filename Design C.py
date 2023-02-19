from analysis.buildfin import Fin
from analysis.plot import plotdata

Fin_C = Fin(name='Design C',Gs=26.9e9,ts=0.6e-3,tc=7e-3,cr=0.8,ct=0.4,s=0.4)
plotdata(Fin_C,30e3)