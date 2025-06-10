def build_param_name(obj_id):
    parts = obj_id.split('-')
    return f"{parts[0]}_{parts[1]}" if len(parts) > 1 else obj_id

def build_condition(conv_signal, mux_values):
    if len(mux_values) == 1:
        return f"{conv_signal} == {mux_values[0]} && ({conv_signal} == Prev({conv_signal},2))"
    joined = " || ".join(f"{conv_signal} == {v}" for v in mux_values)
    return f"({joined}) && ({conv_signal} == Prev({conv_signal},2))"