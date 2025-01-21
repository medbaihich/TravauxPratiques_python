
def safe_division(a, b):
    try:
        r =a/b
    except ZeroDivisionError:
        print("Erreur => b ne peut pas être égal à 0.")
    else:
        print("La division a été effectuée avec succès.")
        return f"la division = {r}"
    finally:
        print("La fonction 'safe_division' est terminée.")

a = int(input("Entrer le 1er nombre a : "))
b = int(input("Entrer le 2ème nombre b : "))

result = safe_division(a, b)
print(result)