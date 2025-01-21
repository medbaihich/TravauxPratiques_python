with open("exemple.txt","w") as file:
    file.write("Ligne1: bonjour\nLigne2:Bon après-midi\nLigne3:Bonsoir")

with open("exemple.txt", "r") as file:
    for index, line in enumerate(file, start=1):
        print(f"{index}=> {line.strip()}")