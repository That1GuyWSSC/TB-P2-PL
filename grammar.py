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

    def p_command_escrever(self, p):
        """ command : ESCREVER args"""
        p[0] = {
            "operator": "escrever",
            "args": p[2]
        }
    def p_command_assign(self, p):
        """ command : VAR var_list """
        p[0] = {"operator" : "declare", "args": p[2]}

    def p_command_assign_2(self, p):
        """ command : var assign arg """
        p[0] = {"operator" : "assign", "args" : [p[3]], "data": p[1]}

    def p_var_list(self, p):
        """ var_list : var
                     | var_list ',' var"""
        if len(p) == 2:
            p[0] = [{"operator" : "assign_declare", "args": [None], "data": p[1]}]
        else:
            p[0] = p[1]
            p[0].append({"operator" : "assign_declare", "args": [None], "data": p[3]})

    def p_var_list_2(self, p):
        """ var_list : var assign arg
                     | var_list ',' var assign arg """
        if len(p) == 4:
            p[0] = [{"operator" : "assign_declare", "args" : [p[3]], "data": p[1]}]
        else:
            p[0] = p[1]
            p[0].append({"operator" : "assign_declare", "args" : [p[5]], "data": p[3]})

    def p_args(self, p):
        """ args : args ',' arg"""
        p[0] = p[1] + [p[3]]

    def p_args2(self, p):
        """ args : arg"""
        p[0] = [p[1]]

    def p_arg_var(self, p):
        """ arg : var """
        p[0] = {"var": p[1]}

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
        """ expr : var
                 | num """
        p[0] = p[1]

    def p_expr3(self, p):
        """ expr : '(' expr ')'"""
        p[0] = p[2]

    """
    # Método com mensagens de controlo de erros inesperados
    def p_error(self, p):
        if p:
            raise Exception(f"Error: Unexpected token '{p.type}'")
        else:
            raise Exception("Error: Expecting token")
    """
    def p_error(self, p):
        if p:
            print(f"Syntax error: unexpected '{p.type}'")
        else:
            print("Syntax error: unexpected end of file")
        exit(1)
