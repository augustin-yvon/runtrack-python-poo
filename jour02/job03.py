from job02 import Livre

class Livre(Livre):
    def __init__(self, titre, auteur, nbr_pages, disponible = True):
        super().__init__(titre, auteur, nbr_pages)
        self.disponible = disponible

    def verification(self):
        if self.disponible == True:
            return True
        else:
            return False
        
    def emprunter(self):
        if self.verification():
            self.disponible = False
            return "Le livre a été emprunté"
        else:
            return "Le livre est indisponible"

    def rendre(self):
        if not self.verification():
            self.disponible = True
            return "Le livre a été rendu"
     
livre1 = Livre('mamma','john',150)
print(livre1.verification())
print(livre1.emprunter())
print(livre1.verification())
print(livre1.emprunter())
print(livre1.rendre())
print(livre1.verification())