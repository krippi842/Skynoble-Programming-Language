# Example AST Nodes
class LetStatement:
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value

class FuncDeclaration:
    def __init__(self, name, params, return_type, body):
        self.name = name
        self.params = params
        self.return_type = return_type
        self.body = body

# Parser
def parse(tokens):
    i = 0
    def parse_expression():
        nonlocal i
        if tokens[i][0] == "NUMBER":
            val = tokens[i][1]
            i += 1
            return int(val)
        elif tokens[i][0] == "IDENTIFIER":
            val = tokens[i][1]
            i += 1
            return val
        return None
    
    def parse_let_statement():
        nonlocal i
        if tokens[i][0] == "LET":
            i += 1
            identifier = tokens[i][1]
            i += 1
            if tokens[i][0] == "ASSIGN":
                i += 1
                value = parse_expression()
                return LetStatement(identifier, value)
        return None
    
    # Main loop to parse the tokens into an AST
    statements = []
    while i < len(tokens):
        stmt = parse_let_statement()
        if stmt:
            statements.append(stmt)
        i += 1
    return statements

# Parser update: Handle mutable variables
def parse_let_statement():
    nonlocal i
    if tokens[i][0] == "LET":
        i += 1
        is_mutable = False
        if tokens[i][0] == "MUT":
            is_mutable = True
            i += 1
        identifier = tokens[i][1]
        i += 1
        if tokens[i][0] == "ASSIGN":
            i += 1
            value = parse_expression()
            return LetStatement(identifier, value, is_mutable)
    return None
