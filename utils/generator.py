from handlers.handleLevel import handle_level_2, handle_level_3, handle_level_4

def generate_derived_parameters(rows):
    derived_lines = []
    mbox_name = ""
    for line in rows:
        level = line[2].strip()
        if level == "2":
            # nom de la boîte de message qui sera utilisé par tous les lignes subséquents de niveau supérieur
            mbox_name = handle_level_2(line)
        elif level == "3":
            # Ajout du paramètre dérivé pour la ligne de niveau 3
            derived_lines.extend(handle_level_3(line, mbox_name))
        elif level == "4":
            # Ajout du paramètre dérivé pour la ligne de niveau 4
            derived_lines.extend(handle_level_4(line, mbox_name))
    return derived_lines

