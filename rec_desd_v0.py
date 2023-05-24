"""
    Aula de Processamento de Linguagens
    8.maio.2023

    exemplo implementação algoritmo recursivo descendente
"""
import ply.lex as plex

class Lexer:
    tokens= ("num", )
    literals = ['a', 'b', 'c', '$']
    t_ignore = " "

    def __init__(self):
        self.lexer = None

    def build(self, string, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)
        self.lexer.input(string)

    def t_num(self, t):
        r"[0-9]+"
        t.value = int (t.value)
        return t

    def token(self):
        token = self.lexer.token()
        return token if token is None else token.type # num, None

    def t_error(self, t):
        print(f"Unexpected token: [{t.value[:10]}]")
        exit(1)


# ---------------------------------------------
#
#
#
class Grammar:

    def __init__(self, expr):
        self.lexer = Lexer()
        self.lexer.build(expr + "$")  #
        self.symb = self.lexer.token()

    # Z -> S $           { a, b, c }

    def rec_Z(self):
        print(self.symb)
        if self.symb in ["a", "b", "c"]:
            return self.rec_S() and self.rec_terminal("$")
        else:
            return False

    def rec_S(self):
        if self.symb in ["a"]:
            return self.rec_terminal("$")
        else:
            return False

    # ... Completar

    def rec_terminal(self, s):
        if self.symb == s:
            self.symb = self.lexer.token()
            return True
        else:
            return False


frase = "a"
ag = Grammar(frase)
if ag.rec_Z():
    print("Expressão Válida")
else:
    print("Expressão Inválida")
