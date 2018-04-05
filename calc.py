# -*- coding: utf-8 -*-
import ply.lex as lex
import ply.yacc as yacc

###########################################################
# list of token name
# test  JUST MAKE '*','-','*','/','id','(',')'
tokens = [
    'ID',
    'NUMBER'
]
# Reserved words
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'elif': 'ELIF',
    'for': 'FOR',
    'while': 'WHILE',
    'def': 'DEF',
}
tokenokens = tokens+list(reserved.values())
# expression rule for token


literals = ['+', '-', '*', '/', '(', ')']


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_error(t):
    print("Illegal character {0} at {1}").format(t.value[0], t.lineno)
    t.lexer.skip(1)
    return t


t_ignore_INDENT = r'\t'
t_ignore_COMMENT = r'\#.*'
t_ignore_BLANK = r'\s'

################################################################
precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS')
)  # shift/reduce?

ids = {}


def p_statement_assign(p):
    'statement : ID "=" expression'
    ids[p[1]] = p[3]


def p_statement_expr(p):
    'statement : expression'
    print(p[1])


def p_expression_binop(p):
    '''expression : expression '+' expression 
                  | expression '-' expression 
                  | expression '*' expression 
                  | expression '/' expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = -p[2]


def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]


def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]


def p_expression_id(p):
    "expression : ID"
    try:
        p[0] = ids[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


################################################################
lexer = lex.lex(debug=True)
# data = raw_input()
# lexer.input(data)
# for tok in lexer:
#     print tok

yacc.yacc()

while 1:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)



                        ##
                      ##   ##
                 ###     ##
                ##  ##     ##
               ##    ##   ## 
             ####     ## ##
          #########     ##
        #############  
       ###############  
      ##              #
      # ###############
      #               #
       #      ###    #
        #############
         #         #
          #       #
##################################
##################################
      ###           ###    
      ###           ###
      ###           ###
      ###           ###
      ###           ###
      ###           ###
      ###           ###