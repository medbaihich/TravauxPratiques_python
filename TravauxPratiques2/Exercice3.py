class CompteBancaire:
    def __init__(self,titulaire,solde):
        self.titulaire = titulaire
        self.solde = solde
    def deposer(self,montant):
        self.solde += montant
    def retirer(self,montant):
        if self.solde != 0:
            self.solde -= montant
        else:
            print('Erreur!!!!!!')
    def afficher_solde(self):
        print("le solde actuel: "+str(self.solde))   

compte = CompteBancaire("MedBaihich", 15000)
compte.afficher_solde()
compte.retirer(10000)
compte.afficher_solde()
compte.deposer(2000)
compte.afficher_solde()