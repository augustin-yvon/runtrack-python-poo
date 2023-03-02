class Personne:
    def __init__(self, age = 14):
        self.age = age

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, new_age):
        self.age = new_age

class Eleve(Personne):
    def __init__(self, age = 14):
        super().__init__(age)
    
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print("J'ai {} ans".format(self.age))

class Professeur(Personne):
    def __init__(self, age, matiere):
        super().__init__(age)
        self.__matiere = matiere

    def afficherMatiere(self):
        print(self.__matiere)

    def enseigner(self):
        print("Le cours va commencer")

p = Personne()

e = Eleve()
e.afficherAge()