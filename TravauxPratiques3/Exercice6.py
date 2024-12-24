class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def __str__(self):
        return f"Produit(nom={self.nom}, prix={self.prix})"

class Commande:
    def __init__(self, produit, quantite):
        if quantite <= 0:
            raise ValueError("La quantité doit être supérieure à zéro.")
        self.produit = produit
        self.quantite = quantite

    def calculer_total(self):
        return self.produit.prix * self.quantite

    def __str__(self):
        return f"Commande(produit={self.produit.nom}, quantite={self.quantite}, total={self.calculer_total()})"

class Panier:
    def __init__(self):
        self.commandes = []

    def ajouter_commande(self, commande):
        if not isinstance(commande, Commande):
            raise TypeError("L'objet ajouté doit être une instance de Commande.")
        self.commandes.append(commande)

    def calculer_total(self):
        return sum(commande.calculer_total() for commande in self.commandes)



