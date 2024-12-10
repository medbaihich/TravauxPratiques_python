class Person():
    def __init__(self,nom,prenom,age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    def se_presenter(self):
        print("le nom :", self.nom)
        print("le prenom :", self.prenom)
        print("le age :", self.age)

class Etudiant(Person):
    def __init__(self,nom,prenom,age,matricule):
        super().__init__(nom,prenom,age)
        self.matricule = matricule
    def se_presenter(self):
        super().se_presenter()
        print("le matricule :", self.matricule)
    def etudier(self):
        print(self.nom,self.prenom," :Etudier")

etu= Etudiant("bahi","mohamed", 22,"C15364215")
etu.se_presenter()
etu.etudier()
