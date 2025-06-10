
from handlers.handleLevel import handle_level_2, handle_level_3, handle_level_4

def generate_derived_parameters(rows):
    derived_lines = []
    mbox_name = ""
    for line in rows:
        level = line[2].strip()
        if level == "2":
            mbox_name = handle_level_2(line)
        elif level == "3":
            derived_lines.extend(handle_level_3(line, mbox_name))
        elif level == "4":
            derived_lines.extend(handle_level_4(line, mbox_name))
    return derived_lines

