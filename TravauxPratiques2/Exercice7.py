class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

    def __str__(self):
        return f"{self.titre} par {self.auteur}, publié en {self.annee_publication}"

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def afficher_livres(self):
        if not self.livres:
            print("La bibliothèque est vide.")
        else:
            print("Liste des livres dans la bibliothèque :")
            for livre in self.livres:
                print("*", livre)


livre1 = Livre("The Brothers Karamazov", "Fyodor Dostoevsky", 1880)
livre2 = Livre("The metamorphosis", "Franz Kafka", 1915)
ma_bibliotheque = Bibliotheque()
ma_bibliotheque.ajouter_livre(livre1)
ma_bibliotheque.ajouter_livre(livre2)
ma_bibliotheque.afficher_livres()
