class Point:
    def __init__(self, x = 0, y = 0, nom = 'A'):
        self.x = x
        self.y = y
        self.nom = nom
    
    def afficherLesPoints(self):
        print("{}({},{})".format(self.nom,self.x,self.y))
    
    def afficherX(self):
        print("{}[x] = {}".format(self.nom,self.x))
    
    def afficherY(self):
        print("{}[y] = {}".format(self.nom,self.y))
    
    def changerX(self, new_x):
        self.x = new_x
        print("{}[x] = {}".format(self.nom,self.x))
    
    def changerY(self, new_y):
        self.y = new_y
        print("{}[y] = {}".format(self.nom,self.y))


A = Point(0, 0, 'A')

A.afficherLesPoints()

A.afficherX()
A.afficherY()

A.changerX(2)
A.changerY(5)

print('')

B = Point(1, 1, 'B')

B.afficherLesPoints()

B.afficherX()
B.afficherY()

B.changerX(8)
B.changerY(3)