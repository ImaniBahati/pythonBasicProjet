import re

motDePasse = input("Veuiller saisir un mot de passe : ")

def validerMotDePasse(motDePasse):
    if len(motDePasse)< 8:
        return "le mot de passe doit contenir au moins 8 caracteres"
    if not re.search("[a-z]", motDePasse):
        return "le mot de passe doit contenir au moins une lettre miniscule"
    if not re.search("[A-Z]", motDePasse):
        return "le mot de passe doit contenir au moins une lettre majuscule"
    if not re.search("[0-9]", motDePasse):
        return "le mot de passe doit contenir au moins un chiffre."
    if not re.search("[!@#$%^&*()-_+/^?§~|\]", motDePasse):
        return "le mot de passe doit contenir au moins un carctère special."
    return "Votre mot de passe est valide et robuste"

resultatTest = validerMotDePasse(motDePasse)
print(resultatTest)