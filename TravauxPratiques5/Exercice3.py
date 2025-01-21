while 1:
    choix = input("Voulez-vous ajouter des phrases: ").lower()
    if choix == "oui":
        phrases = input("Entrez vos phrases (séparées par des virgules): ").split(",")
        with open("phrases.txt", "a") as file:
            file.write("\n" + "\n".join(phrases))
    else:
        break
