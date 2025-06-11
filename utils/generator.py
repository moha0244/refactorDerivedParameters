from handlers.handleLevel import handle_level_2, handle_level_3, handle_level_4

def generate_derived_parameters(rows):
    """
       Parcourt les lignes du fichier ICD et génère les paramètres dérivés.

       Paramètres :
       - rows : liste des lignes du fichier ICD

       Retour :
       - Liste des lignes représentant les lignes IADS dérivées.
       """

    derived_lines = []  # Liste pour accumuler toutes les lignes dérivées générées
    mbox_name = ""  # Nom de la boîte de message
    for line in rows:
        level = line[2].strip() # Le champ de niveau est en position 2 (Level 2 / 3 / 4)
        if level == "2":
            # Met à jour le nom de la boîte de message qui sera utilisé pour toutes les lignes suivantes
            mbox_name = handle_level_2(line)
        elif level == "3":
            # Génère les lignes dérivées pour un signal de niveau 3
            derived_lines.extend(handle_level_3(line, mbox_name))
        elif level == "4":
            # Génère les lignes dérivées pour un signal multiplexé de niveau 4
            derived_lines.extend(handle_level_4(line, mbox_name))
    return derived_lines

