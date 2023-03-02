class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur

    def afficher(self):
        rectangle = ''
        for i in range(self.__longueur):
            if i == 0:
                rectangle += "╭──"
            elif i == self.__longueur -1:
                rectangle += "──╮"
            else:
                rectangle += '──'
        rectangle += ' '
        for i in range(self.__largeur):
            rectangle += '\n┃'
            for j in range(self.__longueur):
                rectangle += '  '
            rectangle += '┃'
        rectangle += '\n'
        for i in range(self.__longueur):
            if i == 0:
                rectangle += "╰──"
            elif i == self.__longueur -1:
                rectangle += "──╯"
            else:
                rectangle += '──'
        return rectangle

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.surface() * self.__hauteur


rectangle = Rectangle(10, 5)
print(rectangle.afficher())
print('')

print("Périmètre du rectangle : {}".format(rectangle.perimetre()))
print("Surface du rectangle: {}".format(rectangle.surface()))

rectangle.set_longueur(8)
print("Maj longueur : {}".format(rectangle.get_longueur()))

rectangle.set_largeur(4)
print("Maj largeur : {}".format(rectangle.get_largeur()))

print("Périmètre du rectangle : {}".format(rectangle.perimetre()))
print("Surface du rectangle: {}".format(rectangle.surface()))

print(rectangle.afficher())
print('')

parallelepipede = Parallelepipede(5, 3, 4)
print("Volume du parallélépipède : {}".format(parallelepipede.volume()))