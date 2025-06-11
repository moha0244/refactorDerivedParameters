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


def generate_iads_line(param_name, type_str, bus, obj_text, gen_name, source, expr, unit="", suffix=""):
    """
    Génère une ligne IADS représentant un paramètre dérivé.

    Paramètres :
    - param_name : nom du paramètre (ex. : "TTP_12345")
    - type_str : type du paramètre (ex. : "discrete")
    - bus : nom du bus (ex. : "TTP1")
    - obj_text : description du signal (ex. : "Flight Control Mode")
    - gen_name : nom du signal dans le fichier d'origine (ex. : "PFCC1_COM_MUX_MSGBOX_16")
    - source : source des données (ex. : "BitVector")
    - expr : expression IADS à associer (ex. : "ConvertToInt(...)")
    - unit : unité physique du signal (ex. : "degC")
    - suffix : suffixe optionnel (ex. : "_EU" pour la version physique)

    Retour :
    - Ligne de texte complète au format IadsTppGenerated, prête à être écrite dans un fichier de sortie.
    """

    # Si on a un suffixe (ex. "_EU") et que l’unité est pertinente, on utilise l’unité en remplacement de la source
    unit_or_source = unit if suffix and unit not in ("", "N/A") else source

    # Construction et retour de la ligne IADS complète avec les champs séparés par des tabulations
    return (
        f"IadsTppGenerated\t{param_name}{suffix}\t{type_str}\tGroup\t{bus}\t"
        f"{obj_text}{'_EU' if suffix else ''}\t{gen_name}{'_EU' if suffix else ''}\t"
        f"{unit_or_source}\t16711680\t1\tDerived\t={expr}\t500\n"
    )



def generate_eu_line(param_name, bus, obj_text, gen_name, unit, resolution):
    """
    Génère une ligne IADS supplémentaire pour représenter une version physique (_EU) du paramètre.

    Paramètres :
    - param_name : nom du paramètre initial (ex. : "TTP_12345")
    - bus : nom du bus (ex. : "TTP1")
    - obj_text : description du signal (ex. : "Température ambiante")
    - gen_name : nom brut du champ dans le fichier ICD
    - unit : unité physique à utiliser (ex. : "°C", "psi", etc.)
    - resolution : facteur de conversion à appliquer à la valeur brute (ex. : "0.1")

    Retour :
    - Ligne IADS pour le paramètre converti physiquement, suffixé avec "_EU"
    """

    # Création de l'expression de conversion physique (ex. : (0.1*TTP_12345))
    eu_expr = f"({resolution}*{param_name})"

    # Génération de la ligne complète avec le suffixe "_EU"
    return generate_iads_line(param_name, "float", bus, obj_text, gen_name, unit, eu_expr, suffix="_EU")
