class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
    
    def afficher_info(self):
        return f"->la marque de la vehicule:{self.marque}\n->le modele de la vehicule:{self.modele}\n->annee de fabrication:{self.annee}"

class Moteur:
    def __init__(self, puissance, type_moteur):
        self.puissance = puissance
        self.type_moteur = type_moteur
    def afficher_info(self):
        return f"->la puissance de moteur:{self.puissance}\n->le type de moteur:{self.type_moteur}"

class Voiture(Vehicule,Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, nombre_de_places):
        Vehicule.__init__(self,marque,modele,annee)
        Moteur.__init__(self,puissance,type_moteur)
        self.nombre_de_places = nombre_de_places
    def afficher_info(self):
        return f"{Vehicule.afficher_info(self)}\n->{Moteur.afficher_info(self)}\n->le nombre de places dans la voiture:{self.nombre_de_places}"

class Moto(Vehicule,Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, type_moto):
        Vehicule.__init__(self,marque,modele,annee)
        Moteur.__init__(self,puissance,type_moteur)
        self.type_moto = type_moto
    def afficher_info(self):
        return f"{Vehicule.afficher_info(self)}\n->{Moteur.afficher_info(self)}\n->le type de moto:{self.type_moto}"

v1 = Voiture("Mercedes","G-class", 2010,20,"Deisel",4)
m1 = Moto("BMW","F6010",2011,10,"Deisel","Sport")
print(v1.afficher_info())
print("\n",m1.afficher_info())