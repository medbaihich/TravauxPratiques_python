class Personne:
    def __init__(self,nom,prenom,age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
    @property
    def nom(self):
        return self.__nom
    
    @property
    def prenom(self):
        return self.__prenom
    
    @property
    def age(self):
        return self.__age
    

    @age.setter
    def age(self,age):
        if age > 0:
            self.__age = age
        else: 
            print("Erreur")
        

p1 = Personne("med","baihich",22)
print(p1.nom,p1.prenom,p1.age) 
