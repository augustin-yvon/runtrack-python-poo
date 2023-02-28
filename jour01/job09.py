class Produit:
    def __init__(self, nom, prixHT, TVA = 0.2):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA)

    def afficher_info(self):
        return "Nom : {}\nPrix HT : {}€\nTVA : {}\nPrix TTC : {}€".format(self.nom,self.prixHT,self.TVA,self.CalculerPrixTTC())
    
    def return_nom(self):
        return "Nom : {}".format(self.nom)
    
    def return_prixHT(self):
        return "Prix HT : {}€".format(self.prixHT)
    
    def return_TVA(self):
        return "TVA : {}".format(self.TVA)
    
    def return_prixTTC(self):
        return "Prix TTC : {}€".format(self.CalculerPrixTTC())

    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifier_prixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

p1 = Produit("PC", 1200, 0.2)
p2 = Produit("Bureau", 200, 0.2)

print(p1.afficher_info())
print('')
print(p2.afficher_info())
print('')

p1.modifier_nom('Souris')
p1.modifier_prixHT(150)
print(p1.afficher_info())
print('')

p2.modifier_nom('Chaise')
p2.modifier_prixHT(300)
print(p2.afficher_info())