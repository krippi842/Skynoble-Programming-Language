import subprocess

def assemble(assembly_code):
    # Save assembly code to a file
    with open("output.asm", "w") as f:
        for line in assembly_code:
            f.write(line + "\n")
    
    # Assemble using NASM (for Linux or similar systems)
    subprocess.run(["nasm", "-f", "elf64", "output.asm", "-o", "output.o"])
    
    # Link the object file using GCC to create an executable
    subprocess.run(["gcc", "-o", "program", "output.o"])
