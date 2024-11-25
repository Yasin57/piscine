liste = [("Pierre","Dos",10),("Paul","Brasse",13),("Léa","Crawl",6), ("Léa","Brasse",8) ]
commande = ''

def cmd_exit():
    tmp = input("En etes-vous sur ? (o)ui/(n)on")
    if tmp == 'o':
            return False
    else:
            return True

def cmd_ajout(liste):
        a = input("Qui nage ? ")
        b = input("quelle nage ? ")
        c = input("combien de longueur ? ")
        liste.append((a,b,c))

def cmd_liste(liste):
        '''affiche toutes les performances des nageurs'''
        print("Prénom   -  nage  - longueur")
        print("---------------------------")
        for elt in liste:
            print(f"{elt[0]:11},{elt[1]:8},{elt[2]}")

def cmd_nageur(liste):
    '''affiche toutes les performances d'un nageur'''
    nom_nageurs = input("Quel nageur?")
    print("Performance de ", nom_nageurs)
    print(" nage  -longueur")
    print("-----------------")
    for elt in liste:
            if elt[0]== nom_nageurs:
                print(f"{elt[1]:8},{elt[2]}")


    


isAlive = True
while isAlive:
    commande = input('que faut il faire')
    if commande == 'ajout':
        cmd_ajout(liste)
        continue

    if commande == 'liste':
        cmd_liste(liste)
        continue

    if commande == 'exit':
        isAlive = cmd_exit()
        continue

    if commande == 'nageurs':
          cmd_nageur(liste)
          continue

    print(f"Commande {commande} inconnnue")