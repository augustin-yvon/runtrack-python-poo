class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        return "Le résultat de l'addition est : {}".format(resultat)


objet = Operation(5,8)
result = objet.addition()
print(result)