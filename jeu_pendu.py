
import random

def choisir_mot():
    mots = ["python", "ordinateur", "faith", "programmation", "pendu", "mot"]
    return random.choice(mots)

def afficher_mot_cache(mot, lettres_trouvees):
    mot_cache = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_cache += lettre
        else:
            mot_cache += "_"
    return mot_cache

def jeu_pendu():
    mot_a_deviner = choisir_mot()
    lettres_trouvees = []
    tentatives_restantes = 7

    print("Bienvenue dans le jeu du pendu !")

    while True:
        mot_cache = afficher_mot_cache(mot_a_deviner, lettres_trouvees)
        print("Mot à deviner :", mot_cache)
        print("Tentatives restantes :", tentatives_restantes)

        if "_" not in mot_cache:
            print("Félicitations, vous avez trouvé le mot :", mot_a_deviner)
            break

        lettre = input("Entrez une lettre : ")

        if lettre in lettres_trouvees:
            print("Vous avez déjà deviné cette lettre.")
        elif lettre in mot_a_deviner:
            print("Bonne devinette !")
            lettres_trouvees.append(lettre)
        else:
            print("Dommage, cette lettre n'est pas dans le mot.")
            tentatives_restantes -= 1

        if tentatives_restantes == 0:
            print("Vous avez perdu. Le mot à deviner était :", mot_a_deviner)
            break

if __name__ == "__main__":
    jeu_pendu()