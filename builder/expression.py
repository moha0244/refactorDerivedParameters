
def generate_disc_expr( das_studio_name, start_bit, size, condition=None):
    expr = f"Bit_Pick({das_studio_name},{start_bit - 1},{size})"
    if condition:
        expr = f"IfThen({condition},{expr})"
    return expr

def generate_bnr_expr( das_studio_name, start_bit, size, condition=None, signed=True, UsedMin=True):
    end_bit = (start_bit - 1) + (size - 1)
    if UsedMin or signed:
        expr = f"ConvertToInt({das_studio_name},{start_bit - 1},{end_bit})"
    else:
        expr = f"Bit_Pick({das_studio_name},{start_bit - 1},{size})"
    if condition:
        expr = f"IfThen({condition},({expr}))"
    return expr
