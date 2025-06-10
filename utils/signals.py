from utils.constants import CONVERSION_SIGNALS

def is_valid_signal(name):
    name_upper = name.upper()
    return not ("SPARE" in name_upper or "RESERVED" in name_upper)

def get_conversion_signal(bus, gen_name):
    gen_name = gen_name.upper()
    if "PFCC3" in gen_name:
        return CONVERSION_SIGNALS[bus]["PFCC3"]
    if "PFCC2" in gen_name:
        return CONVERSION_SIGNALS[bus]["PFCC2"]
    if "PFCC1" in gen_name:
        return CONVERSION_SIGNALS[bus]["PFCC1"]
    return None