class Employe:
    def __init__(self, nom ,prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
    def __str__(self):
        return f"{self.nom} {self.prenom} :: Salaire: {self.salaire}"
    

class Menage(Employe):
    def __init__(self,nom, prenom, salaire):
        super().__init__(nom,prenom,salaire)
        self.employees = []
    def ajoute_employe(self,employe):
        return self.employees.append(employe)
    def affichage(self):
        if not self.employees:
            print("aucun employe")
        else:
            for employe in self.employees:
                print("+",employe)

emp1 = Employe("med","baihich", 16000)
emp2 = Employe("yassin","brh",15000)
mng = Menage("y","w",20000)
mng.ajoute_employe(emp1)
mng.ajoute_employe(emp2)
mng.affichage()


