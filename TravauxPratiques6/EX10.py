def read_file(filename):
    f = None
    try:
        f = open(filename , 'r')
        return f.read()
    except FileNotFoundError:
        print("file n'exist pas.")
        return None
    finally:
        if f is not None:
            f.close() 

def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        print("\'value\' n'est pas convertible vers \'int\'")


file = input("Taper PATH de fichier:").strip()
numb = input("Entrer un nombre entrier:")
try:
    print(read_file(file))
    print(convert_to_int(numb))
except Exception as e:
    print(e)