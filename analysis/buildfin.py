# creates a new Object called Fin, which holds attributes such as dimensions and material properties. 
# for easier usage and application in future analysis as this software gets updated with more features. 

class Fin:
    def __init__(self,name,Gs,ts,tc,cr,ct,s,sf,cf):
        #defines attributes of the fin: shear Modulus G, thickness t, root chord cr, tip chord ct, and fin height s.
        # name is the identity of the fin, which is a string of the name of the fin material, sf is solid natural frequency, cf is composite natural frequency. 

        self.name = name
        self.skinshear = Gs
        #self.coreshear = Gc
        self.skinthick = ts
        self.corethick = tc
        self.root = cr
        self.tip = ct
        self.semispan = s
        self.sf = sf 
        self.cf = cf 

        #need to find overall shear modulus - using a rule of mixtures (IS THIS OKAY?????) HELP!!!! - ASK BARTY!?!?
        #first find total thickness - remember skin is above and below, so twice the thickness
        self.thick = 2*self.skinthick + self.corethick
        


    
        #self.shear = (2*self.skinthick/self.thick + 0.516*self.corethick/self.thick)*self.coreshear*self.skinshear/(self.coreshear*(2*self.skinthick/self.thick)+0.400*self.skinshear*(self.corethick/self.thick)) * 1/self.thick  #This is using eq.14 from the same document, which is semi-empirical Halpin-Tsai theory 
        

    def __str__(self):
        return str(self.name)

