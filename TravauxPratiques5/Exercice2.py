phrases = [input(f"entrer le {i+1} phrase:") for i in range(3)]

with open("phrases.txt", "w") as file:
    file.write("\n".join(phrases))