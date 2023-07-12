from analysis.buildfin import Fin
from analysis.plot import plotdata

Fin_D = Fin(name='Design C',Gs=26.9e9,ts=0.6e-3,tc=9e-3,cr=1,ct=0.5,s=0.5,sf=188,cf=254)
plotdata(Fin_D,30e3)