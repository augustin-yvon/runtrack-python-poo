import math
class Cercle:
    def __init__(self, rayon = 1):
        self.rayon = rayon

    def changerRayon(self, new_rayon):
        self.rayon = new_rayon
    
    def afficherInfos(self):
        print("Le cercle a pour rayon {}".format(self.rayon))
        print("Le cercle a pour circonférence {}".format(self.circonférence()))
        print("Le cercle a pour aire {}".format(self.aire()))
        print("Le cercle a pour diamètre {}".format(self.diamètre()))
    
    def circonférence(self):
        return 2*math.pi*self.rayon
    
    def aire(self):
        return math.pi*(self.rayon**2)
    
    def diamètre(self):
        return 2*self.rayon

Cercle1 = Cercle()
Cercle1.afficherInfos()
print('')
Cercle1.changerRayon(4)
Cercle1.afficherInfos()
print('')
Cercle2 = Cercle(7)
Cercle2.afficherInfos()

