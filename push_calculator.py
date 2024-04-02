from colorama import init, Fore, Style

init(autoreset=True)
while True :
    choix = input(" Faire un choix de calcul : \n\n \t1. Table de multiplication \n \t2. Opération entre les nombres\n"
                  " \t3. Calcul de Puissance\n \t4. Calcul de racine carrée \n\n Tu choisis le numéro : ")

    if choix in ["1", "2", "3", "4"] :

        if choix == "1":
            a = int(input("Saisir un nombre à trouver sa table de multiplication : "))
            n = int(input("Saisir le nombre autant sera multiplié : "))
            for i in range(1, a+1):
                print(Fore.LIGHTCYAN_EX + Style.BRIGHT +f"La Table de Multiplication de {i}"+ Fore.RESET + Style.RESET_ALL)
                for j in range(1, n+1):
                    resultat = i * j
                    operation = f"{i} x {j}"
                    color_resultat = f"{Fore.RED}{resultat}{Style.RESET_ALL}"
                    color_operation = f"{Fore.BLUE}{operation}{Style.RESET_ALL}"
                    print(f"{color_operation} = {color_resultat}")
            break

        elif choix == "2":
            while True:
                choix1 = input("Choisir une des opérations suivantes :\n \t1. Addition \n\t2. Soustraction \n\t3. Division "
                               "\n\t4. Multiplication\n \t5. Melange des opérations\nTu choisis le numéro : ")
                if choix1 == "1":
                    nombres = input("Saisir les nombres en mettant de l'espace entre eux : ").split()
                    nombres = [float(nombre) for nombre in nombres]
                    la_somme = sum(nombres)
                    color_resultat = f"{Fore.RED}{la_somme}{Style.RESET_ALL}"
                    signe = ' + '
                    color_signe = f"{Fore.GREEN}{signe}{Style.RESET_ALL}"
                    affiche_somme = color_signe.join([f"({x})" if x < 0 else str(x) for x in nombres])

                    print(f"{affiche_somme} = {color_resultat}")
                    break
                elif choix1 == "2":
                    nombres = input("Saisir les nombres en mettant de l'espace entre eux : ").split()
                    nombres = [float(nombre) for nombre in nombres]
                    la_difference = nombres[0] - sum(nombres[1:])
                    color_resultat = f"{Fore.RED}{la_difference}{Style.RESET_ALL}"
                    signe = ' - '
                    color_signe = f"{Fore.GREEN}{signe}{Style.RESET_ALL}"
                    affiche_difference = color_signe.join([f"({x})" if x < 0 else str(x) for x in nombres])

                    print(f"{affiche_difference} = {color_resultat}")
                    break

                elif choix1 == "3":
                    nombres = input("Saisir les nombres en mettant de l'espace entre eux : ").split()
                    nombres = [float(nombre) for nombre in nombres]
                    quotient = nombres[0]
                    for nombre in nombres[1:]:
                        quotient /= nombre
                    color_resultat = f"{Fore.RED}{quotient}{Style.RESET_ALL}"
                    signe = ' / '
                    color_signe = f"{Fore.GREEN}{signe}{Style.RESET_ALL}"
                    affiche_quotient = color_signe.join([f"({x})" if x < 0 else str(x) for x in nombres])

                    print(f"{affiche_quotient} = {color_resultat}")
                    break

                elif choix1 == "4":
                    nombres = input("Saisir les nombres en mettant de l'espace entre eux : ").split()
                    nombres = [float(nombre) for nombre in nombres]
                    produit = 1
                    for nombre in nombres[1:]:
                        produit *= nombre
                    color_resultat = f"{Fore.RED}{produit}{Style.RESET_ALL}"
                    signe = ' / '
                    color_signe = f"{Fore.GREEN}{signe}{Style.RESET_ALL}"
                    affiche_produit = color_signe.join([f"({x})" if x < 0 else str(x) for x in nombres])

                    print(f"{affiche_produit} = {color_resultat}")
                    break

                elif choix1 == "5":
                    nombres = input("Saisir les nombres en mettant de l'espace entre eux : ").split()
                    nombres = [float(nombre) for nombre in nombres]

                    operations = input("Entrez les opérations que vous souhaitez effuctuer le calcul en mettant de "
                                       "l'espace entre eux (+, -, /, *) : ").split()
                    calcul_etape1 = f"{nombres[0]}"
                    total = nombres[0]

                    for i in range(1, len(nombres)):
                        if operations[i-1] == '*' or operations[i-1] == '/':
                            calcul_etape1 = calcul_etape1 + f" {Fore.GREEN}{operations[i-1]}{Style.RESET_ALL}{nombres[i]} "
                            if operations[i-1] == '*':
                                total *= nombres[i]
                            else :
                                if nombres[i] == 0:
                                    print(Fore.RED + Style.BRIGHT+"Division par zéro est impossible"+Fore.RESET + Style.RESET_ALL)
                                total /= nombres[i]
                        else :
                            calcul_etape1 += f"{operations[i-1]}{nombres[i]}"
                            if operations[i-1] == '+':
                                total += nombres[i]
                            elif operations[i-1] == '-':
                                total -=nombres[i]
                    print(f"{calcul_etape1} = {Fore.GREEN}{total}{Style.RESET_ALL}")

                    break

                else :
                    print(Fore.RED + Style.BRIGHT+"Veuillez saisir un bon choix parmi le cinq" + Fore.RESET+Style.RESET_ALL)
            break
        elif choix == "3":
            nombre = int(input("Saisir un nombre : "))
            indice = int(input("Saisir l'indice : "))
            puissance_nombre = nombre**indice
            affiche_puissance = f"({nombre})^{indice}"
            color_affiche = f"{Fore.CYAN}{affiche_puissance}{Style.RESET_ALL}"
            color_result = f"{Fore.BLUE}{puissance_nombre}{Style.RESET_ALL}"

            print(f"{color_affiche} = {color_result}")

            break

        elif choix == "4":
            nombre = int(input("Saisir un nombre : "))
            indice = int(input("Saisir l'indice : "))
            racine_nombre = nombre ** (1/indice)
            affiche_racine = f"({nombre})^1/{indice}"
            color_affiche = f"{Fore.CYAN}{affiche_racine}{Style.RESET_ALL}"
            color_result = f"{Fore.BLUE}{racine_nombre}{Style.RESET_ALL}"

            print(f"{color_affiche} = {color_result}")

            break

    else :
        print(Fore.RED + Style.BRIGHT + "Veuillez saisir un bon choix" + Fore.RESET+ Style.RESET_ALL)