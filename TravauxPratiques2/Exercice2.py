class Voiture:
    def __init__(self,marque,modele,annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
    def afficher_info(self):
        print("marque: "+self.marque)
        print("modele: "+self.modele)
        print("annee: "+str(self.annee))

voiture1 = Voiture("Mercedes","190",2002)
voiture2 = Voiture("aston martin","Vanquish 3",2010)
voiture1.afficher_info()
voiture2.afficher_info()