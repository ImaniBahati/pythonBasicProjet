import requests
def trouverTauxDeChange(deviceSource, deviseCible):
    """

    Récuperer le taux de change entre deux devises.

    Args :
        deviseSource : c'est la devise source ( donc le code ISO 4217),
        deviseCible : c'est la devise cible ( donc le code ISO 4217).

    Retourne :
        Le taux de change entre deux devises.

    """

    # Accéder à une Api de taux de change 
    # a notre façon nous allons utiliser l'Api "exchangeratesapi.io"

    url = f"https://api.exchangeratesapi.io/latest/{deviceSource}"
    response = requests.get(url)
    data = response.json()
    tauxDeChange = data["rates"][deviseCible]
    return tauxDeChange

def conversionMontant(montant, deviceSource, deviseCible):
    """
    Convertir un montant d'une deviseà une autre.

    Args :
        montant : Le montant à convertir,
        deviseSource : c'est la devise source ( donc le code ISO 4217),
        deviseCible : c'est la devise cible ( donc le code ISO 4217).

    Retourne :
        Le montant converti dans la devise cible.
    """

    tauxDeChange = trouverTauxDeChange(deviceSource, deviseCible)
    montantConverti = montant * tauxDeChange
    return montantConverti
def afficheResultat(montant, deviseSource, deviseCible, montantConverti):

    """
    Affichage du resultat de la conversion.

    Args :
        montant : Le montant initial,
        deviseSource : La devise source,
        deviseCible : La devise cible.
    """
    
    print(f"{montant}{deviseSource} équivaut à {montantConverti:.2f}{deviseCible}")
    #vous pouvez remplacer ou etendre cette liste selon votre besoins
CODES_DEVISES = {
    "AED": "Dirhan des Emirates arabes unis",
    "AOA": "Kwanza angolais",
    "CDF": "Franc congolais",
    "USD": "Dollar américan",
    "ZWL": "Dollar zimbabwéen",
    }

# Saisir un montant
montant = float(input("Entrez un montant : "))

# Choisir la devise source
deviceSource = input("Choisissez la device source (code ISO) : ").upper()

while deviceSource not in CODES_DEVISES :
    deviceSource = input("Devise invalide. Veuillez choisir encore(réesayer) : ").upper()
# Choisir la devise cible
deviceCible = input("Choisissez la device cible (code ISO) : ").upper()

while deviceCible not in CODES_DEVISES :
    deviceCible= input("Devise invalide. Veuillez choisir encore(réesayer) : ").upper()

#Convertir le montant
montantConverti = conversionMontant(montant, deviceSource, deviceSource)
#Afficehr le résultat (la conversion)
afficheResultat(montant, deviceSource, deviceCible, montantConverti)