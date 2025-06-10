def generate_iads_line(param_name, type_str, bus, obj_text, gen_name, source, expr, unit="", suffix=""):
    unit_or_source = unit if suffix and unit not in ("", "N/A") else source
    return (
        f"IadsTppGenerated\t{param_name}{suffix}\t{type_str}\tGroup\t{bus}\t"
        f"{obj_text}{'_EU' if suffix else ''}\t{gen_name}{'_EU' if suffix else ''}\t"
        f"{unit_or_source}\t16711680\t1\tDerived\t={expr}\t500\n"
    )

def generate_eu_line(param_name, bus, obj_text, gen_name, unit, resolution):
    eu_expr = f"({resolution}*{param_name})"
    return generate_iads_line(param_name, "float", bus, obj_text, gen_name, unit, eu_expr, suffix="_EU")

