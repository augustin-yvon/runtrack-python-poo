class CompteBancaire:
    def __init__(self, num_compte, nom, prenom, solde, decouvert):
        self.__num_compte = num_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
    
    def afficher(self):
        print("Numéro de compte : {}\nNom : {}\nPrénom : {}\nSolde : {}".format(self.__num_compte, self.__nom, self.__prenom, self.__solde))

    def afficherSolde(self):
        print("Solde : {}".format(self.__solde))
    
    def versement(self, montant):
        if type(montant) == int:
            self.__solde += montant
        else:
            print("Le montant doit être un entier")

    def retrait(self, montant):
        if self.__decouvert == True:
            if type(montant) == int:
                self.__solde -= montant
                return True
            else:
                print("Le montant doit être un entier") 
        elif self.__decouvert == False:
            if type(montant) == int:
                if self.__solde > montant:
                    self.__solde -= montant
                    return True
                else:
                    print("vous n'avez pas assez de solde disponible")
            else:
                print("Le montant doit être un entier")
            
    def set_decouvert(self, boolean):
        self.__decouvert = boolean

    def agios(self):
        if self.__solde < 0:
            self.__solde = self.__solde-(self.__solde*0.07)

    def virement(self, compte_crediter, montant):
        if self.retrait(montant) == True:
            compte_crediter.versement(montant)
            print("Virement effectué")
        else:
            print("Le virement n'a pas fonctionné !")

compte1 = CompteBancaire(1578, 'Yvon', 'Augustin', 1500, False)
compte1.afficher()
compte1.afficherSolde()

compte1.versement('banane')
compte1.versement(150)
compte1.afficherSolde()

compte1.retrait(500)
compte1.afficherSolde()

compte1.retrait(4000)
compte1.set_decouvert(True)
compte1.retrait(4000)
compte1.afficherSolde()

compte2 = CompteBancaire(2945, 'Durand', 'Michel', -120, True)
compte1.versement(4000)
compte1.set_decouvert(False)
compte1.virement(compte2, 15000)
compte1.virement(compte2, 120)
compte2.afficherSolde()