class Student:
    def __init__(self, prenom, nom, numero_etudiant, credits = 0):
        self.prenom = prenom
        self.nom = nom
        self.numero_etudiant = numero_etudiant
        self.credits = credits
        self.level = self.studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.credits += credits
        else:
            print('Le nombre de crédits doit être supérieur à 0')
    
    def studentEval(self):
        if self.credits >= 90:
            return "Excellent"
        elif self.credits >= 80:
            return "Très bien"
        elif self.credits >= 70:
            return "Bien"
        elif self.credits >= 60:
            return "Passable"
        elif self.credits < 60:
            return "Insuffisant"
    
    def studentInfo(self):
        self.level = self.studentEval()
        print("Nom : {}\nPrénom : {}\nNuméro étudiant : {}\nNiveau : {}".format(self.nom,self.prenom,self.numero_etudiant,self.level))

etudiant1 = Student('John','Doe',145)

etudiant1.add_credits(10)
etudiant1.add_credits(45)
etudiant1.add_credits(20)

print("Le nombre de crédits de {} {} est de {} points".format(etudiant1.prenom,etudiant1.nom,etudiant1.credits))

etudiant1.studentInfo()