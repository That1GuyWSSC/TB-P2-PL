from lexer import Lexer

al = Lexer()
al.input("""
start
ESCREVER "maria", "ana";
ESCREVER "maria", "joaquim";

VAR teste : 224, adsada : "asdadAa" ;
end
""")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end=" ")
