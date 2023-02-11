# creates a new Object called Fin, which holds attributes such as dimensions and material properties. 
# for easier usage and application in future analysis as this software gets updated with more features. 

class Fin:
    def __init__(self,name,Gs,Gc,ts,tc,cr,ct,s):
        #defines attributes of the fin: shear Modulus G, thickness t, root chord cr, tip chord ct, and fin height s.
        # name is the identity of the fin, which is a string of the name of the fin material

        self.name = name
        self.skinshear = Gs
        self.coreshear = Gc
        self.skinthick = ts
        self.corethick = tc
        self.root = cr
        self.tip = ct
        self.height = s

        #need to find overall shear modulus - using a rule of mixtures (IS THIS OKAY?????) HELP!!!! - ASK BARTY!?!?
        #first find total thickness - remember skin is above and below, so twice the thickness
        self.thick = 2*self.skinthick + self.corethick
        self.shear = self.skinshear*self.coreshear / ((2*self.skinthick/self.thick)**3 * self.coreshear + (self.corethick/self.thick)**3 * self.skinshear)


    def __str__(self):
        return str(self.name)

