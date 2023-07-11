from analysis.buildfin import Fin
from analysis.plot import plotdata

Fin_A = Fin(name='Design A',Gs=78e9,ts=1.0e-3,tc=10.5e-3,cr=0.9,ct=0.45,s=0.4)
plotdata(Fin_A,30e3)
