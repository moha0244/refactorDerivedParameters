import csv

def parse_icd_file(file_obj):
    """
    parcourt un fichier CSV

    Paramètres :
    - file_obj : objet fichier ouvert

    Retour :
    - Liste de lignes (chaque ligne est une liste de colonnes CSV)
    """
    # Décode le contenu binaire en UTF-8 et découpe par ligne
    decoded = file_obj.read().decode("utf-8").splitlines()

    # Crée un lecteur CSV en utilisant le point-virgule comme séparateur
    reader = csv.reader(decoded, delimiter=';')

    # Ignore l'en-tête
    next(reader)

    # Retourne les lignes restantes sous forme de liste
    return list(reader)
