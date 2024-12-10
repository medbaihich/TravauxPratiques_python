class Chien:
    def __init__(self, nom, race, age):
        self.nom = nom
        self.race = race
        self.age = age

    def aboyer(self):
        print("Woof!")


mon_chien = Chien("Rex", "Haskey", 5)

mon_chien.aboyer()
