from lexer import Lexer

al = Lexer()
al.input("""ESCREVER "maria" """)

while True:
    tk = al.token()
    if not tk:
        break
    print(tk,end="")
