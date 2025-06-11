from utils.constants import CONVERSION_SIGNALS

def is_valid_signal(name):
    """
    Vérifie si le nom d'un signal est valide.
    On considère qu'un signal est invalide s'il contient 'SPARE' ou 'RESERVED'.

    Paramètres :
        name: Nom du signal à vérifier

    Retourne :
        bool: True si le signal est valide, False sinon
    """
    name_upper = name.upper()
    return not ("SPARE" in name_upper or "RESERVED" in name_upper)


def get_conversion_signal(bus, gen_name):
    """
    Récupère le signal de conversion (MUX) à utiliser pour une ligne de niveau 4,
    basé sur le bus et le nom du générateur de signal.

    Paramètres :
        bus : Le bus (ex: "TTP1", "TTP2", ...)
        gen_name : Le nom du générateur de signal (ex: "PFCC1_MON", "PFCC2_COM", ...)

    Retourne :
        str | None: Le nom du signal de conversion associé, ou None si aucun ne correspond
    """
    gen_name = gen_name.upper()
    if "PFCC3" in gen_name:
        return CONVERSION_SIGNALS[bus]["PFCC3"]
    if "PFCC2" in gen_name:
        return CONVERSION_SIGNALS[bus]["PFCC2"]
    if "PFCC1" in gen_name:
        return CONVERSION_SIGNALS[bus]["PFCC1"]
    return None