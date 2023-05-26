from lexer import Lexer

import ply.yacc as pyacc


class Grammar:
    precedence = (
        ("left", "+", "-"),
        ("left", "*", "/")
    )

    def __init__(self):
        self.lexer = None
        self.tokens = None
        self.yacc = None

    def build(self):
        self.lexer = Lexer()
        self.tokens = self.lexer.tokens
        self.yacc = pyacc.yacc(module=self)


    def parse(self, string):
        self.lexer.input(string)
        return self.yacc.parse(lexer=self.lexer.lex)

    def p_program(self, p):
        """ program : start commands end"""
        p[0] = p[2]

    def p_commands(self, p):
        """ commands : commands command ';'"""
        p[0] = p[1] + [p[2]]

    def p_commands2(self, p):
        """ commands : command ';'"""
        p[0] = [p[1]]

    def p_command(self, p):
        """ command : ESCREVER args"""
        p[0] = {
            "operator": "escrever",
            "args": p[2]
        }

    def p_args(self, p):
        """ args : args ',' arg"""
        p[0] = p[1] + [p[3]]

    def p_args2(self, p):
        """ args : arg"""
        p[0] = [p[1]]

    def p_arg_str(self, p):
        """ arg : string"""
        p[0] = str(p[1])

    def p_arg_expr(self, p):
        """ arg : expr"""
        p[0] = p[1]

    def p_expr(self, p):
        """ expr : expr '+' expr
                 | expr '-' expr
                 | expr '*' expr
                 | expr '/' expr"""
        p[0] = {"operator": p[2], "args": [p[1], p[3]]}

    def p_expr2(self, p):
        """ expr : num"""
        p[0] = p[1]

    def p_expr3(self, p):
        """ expr : '(' num ')'"""
        p[0] = p[2]

    def p_expr3(self, p):
        """ expr : '(' num ')'"""
        p[0] = p[2]

    # Método com mensagens de controlo de erros inesperados
    def p_error(self, p):
        if p:
            raise Exception(f"Error: Unexpected token '{p.type}'")
        else:
            raise Exception("Error: Expecting token")
