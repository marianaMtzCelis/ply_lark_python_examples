# Mariana Martínez Celis Gonzalez A01194953
# littleDDuckLex.py

import ply.lex as lex
import re

reserved = {
    'program': 'PROGRAM',
    'var': 'VAR',
    'int': 'INT',
    'float': 'FLOAT',
    'print': 'PRINT',
    'ctestring': 'CTESTRING',
    'if': 'IF',
    'else': 'ELSE',
    'ctel': 'CTEL',
    'ctef': 'CTEF',
}

# List of token names.
tokens = [
    'ID',
    'PUNTOYCOMA',
    'COMA',
    'DOSPUNTOS',
    'LLAVEABRE',
    'LLAVECIERRA',
    'IGUAL',
    'MAYORQUE',
    'MENORQUE',
    'NOIGUAL',
    'PARENTESISABRE',
    'PARENTESISCIERRA',
    'MAS',
    'MENOS',
    'MULTIPLICACION',
    'DIVISION',
] + list(reserved.values())

# Regular expression rules for simple tokens
t_PUNTOYCOMA = r'\;'
t_COMA = r'\,'
t_DOSPUNTOS = r'\:'
t_LLAVEABRE = r'\{'
t_LLAVECIERRA = r'\}'
t_IGUAL = r'\='
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_NOIGUAL = r'<>'
t_PARENTESISABRE = r'\('
t_PARENTESISCIERRA = r'\)'
t_MAS = r'\+'
t_MENOS = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'\/'


# Regular expression rules for complex tokens
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


lexer = lex.lex()


data = '< <>'

# data = '''
# program mariana123;
# var a, b, c;
# if (a < b) {
#     print(ctestring);
# } else {
#     print(a);
# }
# '''

# lexer.input(data)

# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)
