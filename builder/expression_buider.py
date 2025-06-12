def generate_disc_expr(das_studio_name, start_bit, size, condition):
    """
    Génère une expression IADS pour un signal de type discret (DISC).

    Paramètres :
    - das_studio_name : nom complet du signal
    - start_bit : bit de départ dans le vecteur
    - size : taille du champ binaire (en bits)
    - condition : condition logique à appliquer (seulement pour le level4)

    Retour :
    - Expression IADS au format Bit_Pick (ou IfThen(..., Bit_Pick(...)) si condition)
    """
    # Création de l'expression de base : extraction de bits à partir de la position donnée
    expr = f"Bit_Pick({das_studio_name},{start_bit - 1},{size})"

    # Si une condition de multiplexage est fournie (niveau 4), on encapsule l'expression dans un IfThen
    if condition:
        expr = f"IfThen({condition},{expr})"

    return expr


def generate_bnr_expr(das_studio_name, start_bit, size, condition, signed, used_min):
    """
    Génère une expression IADS pour un signal de type binaire numérique (BNR).

    Paramètres :
    - das_studio_name : nom complet du signal (ex. : "TTP1_PFCC1_COM_MUX_MSGBOX_16")
    - start_bit : bit de départ dans le vecteur
    - size : taille du champ binaire
    - condition : condition logique à appliquer (seulement pour level4 correspondant au multiplexage)
    - signed : indique si le champ est signé ou non
    - used_min : indique si la valeur min est disponible (seulement pour le level3, pour le level4 on suppose que c’est le cas)

    Retour :
    - Expression IADS au format ConvertToInt(...) ou Bit_Pick(...) (avec IfThen si condition)
    """
    # Calcul du bit de fin basé sur la taille du champ
    end_bit = (start_bit - 1) + (size - 1)

    if used_min or signed:
        # Si le signal est signé OU que l'on utilise une valeur min :
        # on effectue une conversion en entier signé
        expr = f"ConvertToInt({das_studio_name},{start_bit - 1},{end_bit})"
    else:
        # Sinon, simple extraction de bits (non signé, pas de min)
        expr = f"Bit_Pick({das_studio_name},{start_bit - 1},{size})"

    # Si une condition de multiplexage est présente (level 4), on encapsule l'expression dans un IfThen
    if condition:
        expr = f"IfThen({condition},({expr}))"

    return expr