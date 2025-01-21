def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erreur => b ne peut pas être égal à 0"




"""a = int(input("Entrer le 1er nombre a : "))
b = int(input("Entrer le 2ème nombre b : "))
result = safe_division(a, b)
print("Résultat :", result)"""