class Animal:
    def faire_du_bruit(self):
        pass

class Chien(Animal):
    def faire_du_bruit(self):
        print("Aboiement")

class Chat(Animal):
    def faire_du_bruit(self):
        print("Miaoulement")

chat = Chat()
chat.faire_du_bruit()
chien = Chien()
chien.faire_du_bruit()