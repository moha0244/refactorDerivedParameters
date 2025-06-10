# Dictionnaire contenant les signaux de conversion MUX spécifiques à chaque bus et contrôleur PFCC.

CONVERSION_SIGNALS = {
    # Bus TTP1
    "TTP1": {
        "PFCC1": "TTP_18737",  # Signal MUX pour PFCC1 sur TTP1
        "PFCC2": "TTP_18743",  # Signal MUX pour PFCC2 sur TTP1
        "PFCC3": "TTP_18749",  # Signal MUX pour PFCC3 sur TTP1
    },
    # Bus TTP2
    "TTP2": {
        "PFCC1": "TTP_18739",  # Signal MUX pour PFCC1 sur TTP2
        "PFCC2": "TTP_18745",  # Signal MUX pour PFCC2 sur TTP2
        "PFCC3": "TTP_18751",  # Signal MUX pour PFCC3 sur TTP2
    },
    # Bus TTP3
    "TTP3": {
        "PFCC1": "TTP_18741",  # Signal MUX pour PFCC1 sur TTP3
        "PFCC2": "TTP_18747",  # Signal MUX pour PFCC2 sur TTP3
        "PFCC3": "TTP_18753",  # Signal MUX pour PFCC3 sur TTP3
    }
}
