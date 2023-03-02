class Ville:
    def __init__(self, nom, nb_habitants):
        self.__nom = nom
        self.__nb_habitants = nb_habitants

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    def get_nb_habitants(self):
        return self.__nb_habitants

    def set_nb_habitants(self, nb_habitants):
        self.__nb_habitants = nb_habitants


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
    
    def ajouterPopulation(self):
        self.__ville.set_nb_habitants(self.__ville.get_nb_habitants() + 1)

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_ville(self):
        return self.__ville

    def set_ville(self, ville):
        self.__ville = ville

ville1 = Ville("Paris", 1000000)
print("Population de la ville de {} : {}".format(ville1.get_nom(), ville1.get_nb_habitants()))

ville2 = Ville("Marseille", 861635)
print("Population de la ville de {} : {}".format(ville2.get_nom(), ville2.get_nb_habitants()))

personne1 = Personne('John', 45, ville1)
personne1.ajouterPopulation()

personne2 = Personne('Myrtille', 4, ville1)
personne2.ajouterPopulation()

personne3 = Personne('Chloé', 18, ville2)
personne3.ajouterPopulation()
print("Maj Population de la ville de {} : {}".format(ville1.get_nom(), ville1.get_nb_habitants()))
print("Maj Population de la ville de {} : {}".format(ville2.get_nom(), ville2.get_nb_habitants()))