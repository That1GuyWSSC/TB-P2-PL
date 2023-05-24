from lexer import Lexer
from eval_interpreter import EvalInterpreter

import ply.yacc as pyacc


class Grammar:
    precedence = ()

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
        op = self.yacc.parse(lexer=self.lexer.lex)
        return EvalInterpreter.operators[op["operator"]](op["args"])

    def p_program(self, p):
        """ program : start command end"""
        p[0] = p[2]

    def p_command(self, p):
        """ command : ESCREVER args"""
        p[0] = {
            "operator": "escrever",
            "args": p[2]
        }

    def p_args(self, p):
        """ args : args ',' arg"""
        p[0] = p[1] + [p[2]]

    def p_args2(self, p):
        """ args : arg"""
        p[0] = [p[1]]

    def p_arg(self, p):
        """ arg : string"""
        p[0] = str(p[1])


    # Método com mensagens de controlo de erros inesperados
    def p_error(self, p):
        if p:
            raise Exception(f"Error: Unexpected token '{p.type}'")
        else:
            raise Exception("Error: Expecting token")
