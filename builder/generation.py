def generate_iads_line(param_name, type_str, bus, obj_text, gen_name, source, expr, unit="", suffix=""):
    """
    Génère une ligne IADS représentant un paramètre dérivé.

    Paramètres :
    - param_name : nom du paramètre (ex. : "TTP_12345")
    - type_str : type du paramètre (ex. : "discrete")
    - bus : nom du bus (ex. : "TTP1")
    - obj_text : description du signal (ex. : "Flight Control Mode")
    - gen_name : nom du signal dans le fichier d'origine (ex. : "PFCC1_COM_MUX_MSGBOX_16")
    - source : source des données
    - expr : expression IADS (ex. : "ConvertToInt(...)")
    - unit : unité physique
    - suffix : suffixe ajouté au nom (EU),

    Retour :
    - Ligne complète au format IadsTppGenerated, qui vont être écrite dans un fichier .txt
    """
    # Si suffixe (_EU) n'est pas vide et l’unité est valide, l’unité devient la source à afficher
    unit_or_source = unit if suffix and unit not in ("", "N/A") else source

    return (
        f"IadsTppGenerated\t{param_name}{suffix}\t{type_str}\tGroup\t{bus}\t"
        f"{obj_text}{'_EU' if suffix else ''}\t{gen_name}{'_EU' if suffix else ''}\t"
        f"{unit_or_source}\t16711680\t1\tDerived\t={expr}\t500\n"
    )


def generate_eu_line(param_name, bus, obj_text, gen_name, unit, resolution):
    """
    Génère une ligne IADS supplémentaire pour représenter une version physique (_EU) du paramètre.

    Paramètres :
    - param_name : nom du paramètre initial (sans _EU)
    - bus : nom du bus (ex. : "TTP1")
    - obj_text : description textuelle
    - gen_name : nom du champ d’origine
    - unit : unité physique (ex. : "degC")
    - resolution : facteur de conversion à appliquer (ex. : "0.1")

    Retour :
    - Ligne IADS convertie au format physique (_EU) avec multiplicateur
    """
    eu_expr = f"({resolution}*{param_name})"
    return generate_iads_line(param_name, "float", bus, obj_text, gen_name, unit, eu_expr, suffix="_EU")
