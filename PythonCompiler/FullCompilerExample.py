def compile_skycode(code):
    # Step 1: Tokenize the Skynoble code
    tokens = tokenize(code)
    
    # Step 2: Parse the tokens into an Abstract Syntax Tree (AST)
    ast = parse(tokens)
    
    # Step 3: Generate Intermediate Representation (IR)
    ir = generate_ir(ast)
    
    # Step 4: Generate x64 Assembly from IR
    assembly = generate_assembly(ir)
    
    # Step 5: Assemble and link the code into an executable
    assemble(assembly)

# Example Skynoble Code
skynoble_code = """
let x = 5;
let y = 10;
"""

# Compile the Skynoble code
compile_skycode(skynoble_code)
