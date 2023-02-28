class Animal:
    def __init__(self, age = 0, prenom = ''):
        self.age = age
        self.prenom = prenom

    def viellir(self):
        self.age = int(self.age) + 1
        print("L'animal a viellit et a maintenant {} ans".format(self.age))
    
    def donner_age(self):
        self.age = input("Donner un age à votre animal : ")
        print("L'animal a {} ans".format(self.age))
    
    def nommer(self):
        self.prenom = input("Nommez votre animal : ")
        print("L'animal s'appelle {}".format(self.prenom))

animal = Animal()

animal.nommer()
animal.donner_age()
animal.viellir()



