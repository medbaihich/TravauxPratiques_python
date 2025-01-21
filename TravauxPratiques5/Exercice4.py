import csv

with open("contacts.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Nom", "Age", "Ville"])
    writer.writerows([["Alice", 30, "Paris"], ["med", 22, "agadir"], ["brahim", 21, "agadir"]])

with open("contacts.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Nom : {row['Nom']}, Age : {row['Age']}, Ville : {row['Ville']}")
