import json

etudiants = [
    {"nom": "Alice", "âge": 22, "note": 17},
    {"nom": "med", "âge": 22, "note": 14},
    {"nom": "brahim", "âge": 21, "note": 19},
]
with open("etudiants.json", "w") as file:
    json.dump(etudiants, file)
with open("etudiants.json", "r") as file:
    data = json.load(file)
    for etudiant in data:
        print(etudiant)
