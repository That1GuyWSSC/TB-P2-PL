import ply.lex as plex


class Lexer:
    start_end = ("start", "end")
    operators = ("ESCREVER", "PRINT")
    variaveis = ("VAR", "VARS")

    keywords = start_end + operators + variaveis

    tokens = keywords + ("var", "string", "assign", "num", "comment")

    literals = "()+-<>!=/*;[],:'"
    t_ignore = " \t\n"


    # Método com expressão regular do comentário
    def t_comment(self, t):
        r"""\#.*"""
        pass

    # Método com expressão regular capaz de ler um valor de string
    def t_string(self, t):
        r'"[^"]*"'
        t.value = t.value[1:-1]
        return t

    # Método com expressão regular capaz de ler um valor de número inteiro ou real
    def t_num(self, t):
        r"""[0-9]+(\.[0-9]+)?"""
        t.value = float(t.value)
        return t

    # Método com expressão regular capaz de ler o sinal de atruibuição de valores a variaveis em
    def t_assign(self, t):
        r""":"""
        return t

    # Método com expressão regular capaz de ler todos os tipos de keywords presentes no lexer
    def t_keywords(self, t):
        r"""[a-zA-Z]+"""
        # No caso da palavra não estar nas keywords, então assume-se como o nome de uma variável
        t.type = t.value if t.value in self.keywords else "var"
        return t

    # Método de controlo de erros no lexer
    def t_error(self, t):
        raise Exception(f"Unexpected token {t}")

    # Método inicializador da classe com o seu atributo lex inicializado
    def __init__(self):
        self.lex = plex.lex(module=self)

    # Método de execução do lexer no documento
    def token(self):
        t = self.lex.token()
        return t if t is None else t.type

    def input(self, string):
        self.lex.input(string)