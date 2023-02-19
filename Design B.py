from analysis.buildfin import Fin
from analysis.plot import plotdata

Fin_B = Fin(name='Design B',Gs=26.9e9,ts=0.35e-3,tc=6e-3,cr=1,ct=0.4,s=0.3)
plotdata(Fin_B,30e3)