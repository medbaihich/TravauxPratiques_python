class  NegativeAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError("l'age est negatif.")
    return age

try:
    a = int(input("taper l'age :"))  
    print(set_age(a))
except NegativeAgeError as e:
    print("Erreur:",e)