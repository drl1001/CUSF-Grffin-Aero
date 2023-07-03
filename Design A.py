from analysis.buildfin import Fin
from analysis.plot import plotdata

Fin_A = Fin(name='Design A',Gs=78e9,ts=0e-3,tc=6.5e-3,cr=0.9,ct=0.45,s=0.2)
plotdata(Fin_A,30e3)
