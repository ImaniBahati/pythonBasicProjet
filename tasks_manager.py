liste_taches = [] # initialisation de la liste pour stocker les tâches

#Fonction pour ajouter une tâche
def ajouter_tache(tache):
    liste_taches.append(tache)
    print(f"La tâche [{tache}] est ajoutée avec succès ! ")

#Fonction pour afficher toutes les tâches enregistrées
def afficher_tache(tache):
    if liste_taches:
        print("La liste des tâches sont : ")
        for index, tache in enumerate(liste_taches, start=1):
            print(f"{index}. {tache}")
    else:
        print("Aucune tâche enregistrée pour le moment ")

#Fonction pour Supprimer une tâche par son index ou numérotation
def supprimer_tache(index):
    if 1 <= index <= len(liste_taches):
        tache_supprimee = liste_taches.pop(index-1)
        print(f"Tâche [{tache_supprimee}] supprimée avec succès ! ")
    else:
        print("L'index de la tâche invalide, veuiller saisir un index valide.")

# Exemple d'utilisation du programme

while True :
    print("\n \tMenu \n\t 1. Ajouter une tâche \n\t 2. Supprimer une tâche \n\t 3. Afficher une tâche \n\t 4. Quitter")

    choix = input("Choisissez une option parmi ces quatres : ")

    if choix == "1":
        nombres = int(input("saisir le nombre de tâches à ajouter : "))
        for nombre in range(0, nombres):
            tache = input("Entrez une tâche à ajouter: ")
            ajouter_tache(tache)
    elif choix == "2":
        nombres = int(input("Saisir le nombre de tâches à supprimer : "))
        for nombre in range(0, nombres):
            index = int(input("Saisir un index de la tâche à supprimer : "))
            supprimer_tache(index)
    elif choix == "3":
        afficher_tache(tache)
    elif choix == "4":
        break
    else :
        print("Choix est invalide, Veuillez réessayer .")
        