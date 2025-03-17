# Code Generator for x64 Assembly
def generate_assembly(ir):
    assembly = []
    for line in ir:
        if line.startswith("let"):
            parts = line.split("=")
            var_name = parts[0].strip().split()[1]
            value = parts[1].strip().strip(";")
            assembly.append(f"mov rax, {value}")
            assembly.append(f"mov [{var_name}], rax")
    return assembly
