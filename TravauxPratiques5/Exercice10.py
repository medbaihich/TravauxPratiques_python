import csv

def ajouter_contact():
    nom = input("Nom : ")
    age = input("Age : ")
    ville = input("Ville : ")
    with open("contacts.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([nom, age, ville])

def afficher_contacts():
    with open("contacts.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Nom : {row['Nom']}, Age : {row['Age']}, Ville : {row['Ville']}")

def rechercher_contact():
    recherche = input("Entrez le nom à rechercher : ")
    with open("contacts.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Nom"].lower() == recherche.lower():
                print(f"Nom : {row['Nom']}, Age : {row['Age']}, Ville : {row['Ville']}")
                return
        print("Contact non trouvé.")

def supprimer_contact():
    nom = input("Nom du contact à supprimer : ")
    lignes = []
    with open("contacts.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Nom"].lower() != nom.lower():
                lignes.append(row)

    with open("contacts.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Nom", "Age", "Ville"])
        writer.writeheader()
        writer.writerows(lignes)
    print("Contact supprimé.")

while 1:
    print("\n1. Ajouter un contact\n2. Afficher les contacts\n3. Rechercher un contact\n4. Supprimer un contact\n5. Quitter")
    nombre = int(input("Choisissez une option : "))
    match nombre:
        case 1:
            ajouter_contact()
        case 2:
            afficher_contacts()
        case 3:
            rechercher_contact()
        case 4:
            supprimer_contact()
        case 5:
            break
        case _:
            print("Option invalide.")
