from abc import ABC, abstractmethod
import math

class Form(ABC):
    @abstractmethod
    def calculer_surface(self):
        pass

class Rectangle(Form):
    def __init__(self,l,L):
        self.L = L
        self.l = l 
    def calculer_surface(self):
        return self.L*self.l 

class Circle(Form):
    def __init__(self,rayon):
        self.rayon = rayon
    def calculer_surface(self):
        return math.pi*(self.rayon**2)
r1 = Rectangle(4,5)
c1 = Circle(6)
print(r1.calculer_surface())
print(c1.calculer_surface())