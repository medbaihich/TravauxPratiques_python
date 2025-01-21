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

#filename = input("entrer le chemin de cette fichier:").strip()
#r = read_file(filename)
#print("le contenu de fichier :\n",r)

