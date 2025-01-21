import logging

def log_error(message):
    logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s - %(message)s')
    logging.error(message)

def read_file(filename):
    try:
        f = open(filename , 'r')
        return f.read()
    except FileNotFoundError:
        log_error(f"Le fichier '{filename}' est introuvable.")
        print(f"Erreur : Le fichier '{filename}' n'existe pas.")
        return None
    finally:
        try:
            f.close() 
        except:
            pass       

filename = input("entrer le chemin de cette fichier:").strip()
r = read_file(filename)
if r is not None:
    print("le contenu de fichier :\n",r)

