import re

# Token definitions
token_specification = [
    ("NUMBER", r'\d+'),
    ("LET", r'let'),
    ("MUT", r'@mut'),
    ("FUNC", r'func'),
    ("IF", r'if'),
    ("ELSE", r'else'),
    ("WHILE", r'while'),
    ("RETURN", r'return'),
    ("IDENTIFIER", r'[A-Za-z_][A-Za-z0-9_]*'),
    ("ASSIGN", r'='),
    ("OPERATOR", r'[+\-*/]'),
    ("LPAREN", r'\('),
    ("RPAREN", r'\)'),
    ("LBRACE", r'\{'),
    ("RBRACE", r'\}'),
    ("COMMA", r','),
    ("SEMICOLON", r';'),
    ("EQUALS", r'=='),
    ("LT", r'<'),
    ("GT", r'>'),
    ("WHITESPACE", r'\s+'),
    ("MISMATCH", r'.'),
]

# Tokenizer function
def tokenize(code):
    line_num = 1
    line_start = 0
    tokens = []
    
    # Compile regex
    token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup
        value = mo.group(kind)
        if kind == "WHITESPACE":
            continue
        elif kind == "MISMATCH":
            raise RuntimeError(f"Unexpected character '{value}' at line {line_num}")
        else:
            tokens.append((kind, value))
    return tokens

# Lexer update: Add token for @mut
token_specification = [
    # existing tokens...
    ("MUT", r'@mut')
]
