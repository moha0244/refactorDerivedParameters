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
