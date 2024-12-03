def analyse_text(texte):
    espace=0
    for i in texte:
        if i == " ":
            espace += 1
    return{
    "nombre_de_mote" : len(texte.split()),
    "nombre_de_chaine_de_caracteres" : len(texte)-espace
    }
text="hello world med"
print(analyse_text(text))