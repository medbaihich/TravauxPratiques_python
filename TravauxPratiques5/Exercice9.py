def Statistiques_de_fichier():
    with open("exemple.txt", "r") as file:
        lines = file.readlines()
        n_lignes = len(lines)
        n_mots = sum(len(line.split()) for line in lines)
        n_caracteres = sum(len(line) for line in lines)
        return f"Nombre de lignes : {n_lignes}\nNombre de mots : {n_mots}\nNombre de caractères : {n_caracteres}"


print(Statistiques_de_fichier())