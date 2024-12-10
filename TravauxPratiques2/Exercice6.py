class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculerSurface(self):
        return self.largeur * self.hauteur

    def calculerPerimetre(self):
        return 2 * (self.largeur + self.hauteur)

rectangle = Rectangle(3, 15)

print("Surface du rectangle :", rectangle.calculerSurface())
print("Périmètre du rectangle :", rectangle.calculerPerimetre())