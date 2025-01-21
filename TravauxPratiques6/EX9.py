def get_positive_integer():
    while 1:
        try :
            numb = int(input("entrer un nombre positif:"))
            if numb > 0:
                break
        except ValueError:
            print("\"entrer un nombre entier.\"")


get_positive_integer()