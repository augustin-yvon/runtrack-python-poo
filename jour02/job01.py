class Rectangle:
    def __init__(self, longueur = 1, largeur = 1):
        self.L = longueur
        self.l = largeur
    
    def afficher(self):
        rectangle = ' '
        for i in range(self.L):
            rectangle += '__'
        rectangle += ' '
        for i in range(self.l):
            rectangle += '\n|'
            for j in range(self.L):
                if i == self.l-1:
                    for k in range(self.L):
                        rectangle += '__'
                    rectangle += '|'
                    return rectangle
                rectangle += '  '
            rectangle += '|'
        return rectangle
    
    def modifier_longueur(self, new_longueur):
        self.L = new_longueur

    def modifier_largeur(self, new_largeur):
        self.l = new_largeur

rect = Rectangle(10,5)
print(rect.afficher())
print('')

rect.modifier_largeur(8)
rect.modifier_longueur(3)
print(rect.afficher())