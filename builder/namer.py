def build_param_name(obj_id):
    """
    Construit un nom de paramètre standardisé à partir d’un identifiant.

    Paramètres :
    - obj_id : identifiant brut du paramètre (ex. : "TTP-12345")

    Retour :
    - Nom formaté sous la forme "TTP_12345"
      (ou inchangé si le format initial ne contient pas de tiret)
    """
    parts = obj_id.split('-')
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
    if len(mux_values) == 1:
        return f"{conv_signal} == {mux_values[0]} &&  ({conv_signal} == Prev({conv_signal},2))"
    joined = " || ".join(f"{conv_signal} == {v}" for v in mux_values)
    return f"({joined}) && ({conv_signal} == Prev({conv_signal},2))"
