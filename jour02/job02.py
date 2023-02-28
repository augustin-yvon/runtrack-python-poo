class Livre:
    def __init__(self, titre, auteur, nbr_pages):
        self.titre = titre
        self.auteur = auteur
        self.nbr_pages = nbr_pages
    
    def afficher(self):
        print("Le livre s'appelle {}\nL'auteur s'appelle {}\nIl y a {} pages".format(self.titre, self.auteur, self.nbr_pages))
    
    def modifier_auteur(self, new_auteur):
        self.auteur = new_auteur

    def modifier_titre(self, new_titre):
        self.titre = new_titre

    def modifier_nbr_pages(self, new_nbr_pages):
        if type(new_nbr_pages) == int:
            self.nbr_pages = new_nbr_pages
        else:
            print('Entrez un nombre entier')