def build_param_name(obj_id):
    """
    Construit un nom de paramètre standardisé à partir d’un identifiant.

    Paramètres :
    - obj_id : identifiant brut du paramètre (ex. : "TTP-12345")

    Retour :
    - Nom formaté sous la forme "TTP_12345"
      (ou inchangé si le format initial ne contient pas de tiret)
    """
    # On découpe l'identifiant en deux parties à partir du tiret
    parts = obj_id.split('-')

    # Si on a bien deux parties, on les assemble avec un underscore
    # Sinon  on retourne l’identifiant tel quel
    return f"{parts[0]}_{parts[1]}" if len(parts) > 1 else obj_id




def build_condition(conv_signal, mux_values):
    """
    Construit une condition logique basée sur les valeurs de multiplexage.

    Paramètres :
    - conv_signal : signal de conversion (ex. : "TTP_18737")
    - mux_values : liste de valeurs acceptées pour ce signal (ex. : ["6", "7"])

    Retour :
    - Expression conditionnelle logique utilisée dans une expression IADS :
        - Pour une seule valeur : "TTP_18737 == 6 && (TTP_18737 == Prev(TTP_18737,2))"
        - Pour plusieurs : "(TTP_18737 == 6 || TTP_18737 == 7) && (TTP_18737 == Prev(TTP_18737,2))"
    """

    # Cas où il n’y a qu’une seule valeur de multiplexage
    if len(mux_values) == 1:
        return f"{conv_signal} == {mux_values[0]} &&  ({conv_signal} == Prev({conv_signal},2))"

    # Cas avec plusieurs valeurs : construction de la condition en chaîne
    joined = " || ".join(f"{conv_signal} == {v}" for v in mux_values)

    # Retourne la condition complète avec vérification de stabilité sur deux cycles (Prev)
    return f"({joined}) && ({conv_signal} == Prev({conv_signal},2))"