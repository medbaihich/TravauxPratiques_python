def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        print("\'value\' n'est pas convertible vers \'int\'")

#a = input("entrer un nombre :")
#r =convert_to_int(a)
#print(r)