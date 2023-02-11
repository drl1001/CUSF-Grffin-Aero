from analysis.buildfin import Fin
from analysis.plot import plotdata

Fin_A = Fin(name='Design A',Gs=26.9e9,Gc=115e6,ts=0.3e-3,tc=5.2e-3,cr=0.8,ct=0.4,s=0.2)
plotdata(Fin_A,30e3)
