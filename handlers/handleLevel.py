from builder.namer import build_param_name, build_condition
from builder.generation import generate_iads_line, generate_eu_line
from builder.expression import generate_bnr_expr, generate_disc_expr
from utils.signals import is_valid_signal, get_conversion_signal

def handle_signal(line, mbox_name, is_level_4):
    output = []
    obj_id, obj_text, gen_name = line[0], line[3].strip(), line[4].strip()
    bus, data_type = line[9].strip(), line[8].strip()
    start_bit, size = int(line[16]), int(line[17])
    signed = line[18] != "N"
    resolution = line[19].strip()
    unit = line[20].strip()
    min_val=True

    # Si c'est un niveau 4, on récupère les informations supplémentaires
    if is_level_4:
        mux_rounds = line[13].strip()
        conv_signal = get_conversion_signal(bus, obj_text)
        if not conv_signal:
            return output
        mux_values = [v.strip() for v in mux_rounds.split(',')]
        condition = build_condition(conv_signal, mux_values)
    else:
        condition = None
        min_val = line[21] == "N/A"

    # Si la signal n'est pas valide ou si le gen_name contient "MUX" et le data_type est BNR ou DISC, on l'ignore pour le niveau 3
    if not is_valid_signal(obj_text) or (not is_level_4 and "MUX" in gen_name.upper() and data_type in {"BNR", "DISC"}):
        return output

    param_name = build_param_name(obj_id)
    das_studio_name = f"{bus}_{mbox_name}"

    # Traiter le type de données (BNR ou DISC)
    if data_type == "BNR":
        expr = generate_bnr_expr( das_studio_name, start_bit, size, condition=condition, signed=signed,UsedMin=min_val)
        output.append(generate_iads_line(param_name, "float", bus, obj_text, gen_name, "BitVector", expr))
        if resolution != "N/A":
            output.append(generate_eu_line(param_name, bus, obj_text, gen_name, unit, resolution))
    else:
        expr = generate_disc_expr(das_studio_name, start_bit, size, condition=condition)
        output.append(generate_iads_line(param_name, "discrete", bus, obj_text, gen_name, "BitVector", expr))

    return output


def handle_level_2(line):
    return line[4].strip()

def handle_level_3(line, mbox_name):
    return handle_signal(line, mbox_name,False)


def handle_level_4(line, mbox_name):
    return handle_signal(line, mbox_name, True)