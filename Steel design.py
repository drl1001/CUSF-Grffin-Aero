from analysis.buildfin import Fin
from analysis.plot import plotdata


#Materials: 
#Skin: AISI 4340 Normalized
#Core: SS 304
#Adhesive: resbond
Fin_steel = Fin(name='Steel composite design',Gs=78e9,ts=0.5e-3,tc=12e-3,cr=1.2,ct=1,s=0.25,sf=188.35,cf=254.69)
plotdata(Fin_steel,30e3)