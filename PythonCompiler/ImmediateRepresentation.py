# Example IR Generator
def generate_ir(ast):
    ir = []
    for stmt in ast:
        if isinstance(stmt, LetStatement):
            ir.append(f"let {stmt.identifier} = {stmt.value};")
    return ir
