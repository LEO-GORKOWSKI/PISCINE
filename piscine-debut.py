liste = [("Pierre","Dos",10),("Paul","Brasse",13),("Léa","Crawl",6), ("Léa","Brasse",8) ]
commande = ''


"""Création de fonction"""
def cmd_exit():
    tmp = input("En êtes vous sûr ? (o)ui/(n)on")
    if tmp == 'o':
         return False
    else:
         return True

def cmd_ajout(liste):
        """Ajoute un évènement à la liste"""
        a = input("Qui nage ? ")
        b = input("quelle nage ? ")
        c = input("combien de longueur ? ")
        liste.append((a,b,c))

def cmd_liste(liste):
    """Affiche toutes les performances des nageurs"""
    print("Prénom    -  nage  -  longeur")
    print("-----------------------------")
    for elt in liste:
        print(f"{elt[0]:7} / {elt[1]} / {elt[2]}")

def cmd_nageur(liste):
     '''Affiche les performances d'un seul nageur'''
     tmp = input("Quel nageur ?")
     print("Performance de ", tmp)
     print("nage  -  longeur")
     print("----------------")
     for elt in liste:
        if elt[0]== tmp: 
            print(f"{elt[1]:8} / {elt[2]}")
     
"""Exécution des fonctions"""
isAlive = True
while isAlive:
    commande = input("Que faut-il faire ? ")
    if commande == 'ajout':
        cmd_ajout(liste)
        continue

    if commande == 'liste':
        cmd_liste(liste)
        continue

    if commande == 'exit':
        isAlive = cmd_exit()
        continue
 
    if commande == 'nageur':
         cmd_nageur(liste)
         continue

    print(f"Commande {commande} inconnue")
    