try:
    with open("inexistant.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Le fichier n'existe pas.")
