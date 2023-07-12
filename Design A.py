from analysis.buildfin import Fin
from analysis.plot import plotdata
from analysis.Stability_and_COMs import stability_check

Fin_A = Fin(name='Design A',Gs=78e9,ts=0.7e-3,tc=11.1e-3,cr=1.1,ct=0.7  ,s=0.35,cf=254, sf=188)
plotdata(Fin_A,30e3)

cops=[294.27,294.27,297.81,307.58,303.29,295.7,287.87,279.97,272.15,264.73,257.55] #array length 11 of rasaero cops from mach 0,0.5....5 (in inches as given in software)
t=14
stability_check(cops,t)    #choose t to also find stability value at time t printed in terminal #markers are actual COP points to compare to graph fit
