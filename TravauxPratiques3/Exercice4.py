class Produit:
    def __init__(self,nom,prix):
        self.__nom = nom
        self.__prix = prix
    
    @property
    def nom(self):
        return self.nom 
    
    @property
    def prix(self):
        return self.prix
    
    @nom.setter
    def nom(self,nom):
        self.nom = nom

    @prix.setter
    def prix(self,prix):
        self.prix = prix
    
    def calculer_remise(self, remise,s):
            if self.__prix > s:
                return self.__prix *(1-remise)
            else :
                print("aucun remise ici: le prix doit être supérieur ou égal à ",s)
        

p1 = Produit("tablette", 1600)

print(p1.calculer_remise(0.1,1500))
