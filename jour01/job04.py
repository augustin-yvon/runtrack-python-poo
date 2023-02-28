class Personne:
    def __init__(self, prenom = 'JeSappelle', nom = 'Groot'):
        self.prenom = prenom
        self.nom = nom
    
    def SePresenter(self):
        return "Je m'appelle {} {}".format(self.prenom, self.nom)

humain_1 = Personne("Johnny", "dubled")
result = humain_1.SePresenter()
humain_2 = Personne("Jean", "Michel")
result2 = humain_2.SePresenter()
humain_3 = Personne()
result3 = humain_3.SePresenter()
print(result)
print(result2)
print(result3)
