class Personnage:
    def __init__(self, x, y, prenom):
        self.X = x
        self.Y = y
        self.prenom = prenom

    def AffichagePlateau(self):
        a,b,c,d,e,f,g,h,i = ' ',' ',' ',' ',' ',' ',' ',' ',' '
        if self.X == 0 and self.Y == 0:
            a = self.prenom
        elif self.X < 0 and self.Y == 0:
            c = self.prenom
            self.X = 2
        elif self.Y < 0 and self.X == 0:
            g = self.prenom
            self.Y = 2

        if self.X == 1 and self.Y == 0:
            b = self.prenom
        elif  self.Y < 0 and self.X == 1:
            h = self.prenom
            self.Y = 2

        if self.X == 2 and self.Y == 0:
            c = self.prenom
        elif self.Y < 0 and self.X == 2:
            i = self.prenom
            self.Y = 2
        elif self.X > 2 and self.Y == 0:
            a = self.prenom
            self.X = 0

        if self.X == 0 and self.Y == 1:
            d = self.prenom
        elif self.X < 0 and self.Y == 1:
            f = self.prenom
            self.X = 2

        if self.X == 1 and self.Y == 1:
            e = self.prenom

        if self.X == 2 and self.Y == 1:
            f = self.prenom
        elif self.X > 2 and self.Y == 1:
            d = self.prenom
            self.X = 0

        if self.X == 0 and self.Y == 2:
            g = self.prenom
        elif self.X < 0 and self.Y == 2:
            i = self.prenom
            self.X = 2
        elif self.Y > 2 and self.X == 0:
            a = self.prenom
            self.Y = 0

        if self.X == 1 and self.Y == 2:
            h = self.prenom
        elif self.Y > 2 and self.X == 1:
            b = self.prenom
            self.Y = 0

        if self.X == 2 and self.Y == 2:
            i = self.prenom
        elif self.X > 2 and self.Y == 2:
            g = self.prenom
            self.X = 0
        elif self.Y > 2 and self.X == 2:
            c = self.prenom
            self.Y = 0
        
        print("|---|---|---|")
        print("| {}   {}   {} |".format(g,h,i))
        print("|- -|- -|- -|")
        print("| {}   {}   {} |".format(d,e,f))
        print("|- -|- -|- -|")
        print("| {}   {}   {} |".format(a,b,c))
        print("|---|---|---|")

    def haut(self):
        self.Y += 1   

    def bas(self):
        self.Y -= 1

    def droite(self):
        self.X += 1

    def gauche(self):
        self.X -= 1

    def position(self):
        print("Les coordonnées du personnage sont : ", (self.X,self.Y))

p = Personnage(0, 0, 'p')
p.AffichagePlateau()
p.position()

x = 0
while 1:  
    try:
        new_place = input("Tapez z, s, d ou q pour haut, bas, droite ou gauche : ")
        if new_place == 'z':
            p.haut()
        elif new_place == 's':
            p.bas()
        elif new_place == 'd':
            p.droite()
        elif new_place == 'q':
            p.gauche()
        p.AffichagePlateau()
        p.position()

    except KeyboardInterrupt:
        break