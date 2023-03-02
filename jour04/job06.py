class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix
        self.modele = modele
    
    def informationsVehicule(self):
        print("Marque : {}".format(self.marque))
        print("Modèle : {}".format(self.modele))
        print("Année : {}".format(self.annee))
        print("Prix : {}".format(self.prix))

    def demarrer(self):
        print("Attention, je roule.")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes = 4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes : {}".format(self.portes))

    def demarrer(self):
        print("Je démarre ma voiture.")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roue = 2):
        super().__init__(marque, modele, annee, prix)
        self.roue = roue
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de roues : {}".format(self.roue))

    def demarrer(self):
        print("Je démarre ma moto.")


print('')
voiture1 = Voiture("Peugeot", "206", 2015, 8000, 5)
voiture1.informationsVehicule()
voiture1.demarrer()
print('')

moto1 = Moto("Kawasaki", "H2R", 2018, 5000)
moto1.informationsVehicule()
moto1.demarrer()
print('')