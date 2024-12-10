class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.amis = [] 

    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.prenom} {self.nom}, j'ai {self.age} ans.")

    def ajouter_ami(self, ami):
        if ami not in self.amis:
            self.amis.append(ami)
            print(f"{ami.prenom} {ami.nom} a été ajouté à la liste d'amis.")
        else:
            print(f"{ami.prenom} {ami.nom} est déjà dans la liste d'amis.")

    def afficher_amis(self):
        if self.amis:
            print("Liste des amis :")
            for ami in self.amis:
                print(f"* {ami.prenom} {ami.nom}")
        else:
            print("La liste des amis est vide.")

class Etudiant(Personne):
    def __init__(self, nom, prenom, age, matricule):
        super().__init__(nom, prenom, age)
        self.matricule = matricule

    def etudier(self):
        print(f"{self.prenom} {self.nom} avec le matricule {self.matricule} est en train d'étudier.")


personne1 = Personne("ryad", "akram", 21)
personne2 = Personne("oubalout", "brahim", 23)
etudiant1 = Etudiant("med", "baihich", 22, "C15351")
personne1.se_presenter()
personne2.se_presenter()
etudiant1.se_presenter()
etudiant1.etudier()
personne1.ajouter_ami(personne2)
personne1.ajouter_ami(etudiant1)
personne1.afficher_amis()
