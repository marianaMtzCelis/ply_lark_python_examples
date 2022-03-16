# Mariana Martínez Celis Gonzalez A01194953
# littleDDuckyacc.py

import ply.yacc as yacc

from littleDuckLex import tokens


def p_programa(p):
    '''programa : PROGRAM ID PUNTOYCOMA programap bloque'''
    pass


def p_programap(p):
    '''programap    : vars
                    | epsilon'''
    pass


def p_vars(p):
    '''vars : VAR varsp'''
    pass


def p_varsp(p):
    '''varsp        : ID varp DOSPUNTOS tipo PUNTOYCOMA varspp'''
    pass


def p_varspp(p):
    '''varspp       : varsp
                    | epsilon'''
    pass


def p_varp(p):
    '''varp         : COMA ID varp
                    | epsilon'''
    pass


def p_tipo(p):
    '''tipo         : INT
                    | FLOAT'''
    pass


def p_bloque(p):
    '''bloque : LLAVEABRE bloquep LLAVECIERRA'''
    pass


def p_bloquep(p):
    '''bloquep      : estatuto bloquep
                    | epsilon'''
    pass


def p_epsilon(p):
    '''epsilon : '''
    pass


def p_estatuto(p):
    '''estatuto     : asignacion
                    | condicion
                    | escritura'''
    pass


def p_asignacion(p):
    '''asignacion : ID IGUAL expresion PUNTOYCOMA'''
    pass


def p_expresion(p):
    '''expresion : exp expresionp'''
    pass


def p_expresionp(p):
    '''expresionp   : MAYORQUE exp
                    | MENORQUE exp
                    | NOIGUAL exp
                    | epsilon'''
    pass


def p_escritura(p):
    '''escritura : PRINT PARENTESISABRE escriturap PARENTESISCIERRA PUNTOYCOMA'''
    pass


def p_escriturap(p):
    '''escriturap   : expresion escriturapp
                    | CTESTRING escriturapp'''
    pass


def p_escriturapp(p):
    '''escriturapp  : escriturap
                    | epsilon'''
    pass


def p_condicion(p):
    '''condicion : IF PARENTESISABRE expresion PARENTESISCIERRA bloque condicionp PUNTOYCOMA'''
    pass


def p_condicionp(p):
    '''condicionp   : ELSE bloque
                    | epsilon'''
    pass


def p_exp(p):
    '''exp : termino expp'''
    pass


def p_expp(p):
    '''expp         : MAS exp
                    | MENOS exp
                    | epsilon'''
    pass


def p_termino(p):
    '''termino : factor terminop'''
    pass


def p_terminop(p):
    '''terminop     : MULTIPLICACION termino
                    | DIVISION termino
                    | epsilon'''
    pass


def p_factor(p):
    '''factor       : PARENTESISABRE expresion PARENTESISCIERRA
                    | factorp varcte'''
    pass


def p_factorp(p):
    '''factorp      : MAS
                    | MENOS
                    | epsilon'''
    pass


def p_varcte(p):
    '''varcte       : ID
                    | CTEL
                    | CTEF'''
    pass


# Error rule for syntax errors


def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc(debug=True)

while True:
    try:
        s = input('littleDuck > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
