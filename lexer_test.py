from lexer import Lexer

al = Lexer()
al.input("""
start
ESCREVER "maria ",  "ana", "=", 9+2;
ESCREVER "maria", "joaquim", "=", 0;
ESCREVER "soma de ", 9, " com ", 3*4, " = ", 21;

VAR nome : "ates";
ESCREVER nome;
VAR tmp, a, b;
tmp : 7 + 3;
a : 10 * (30 + tmp);
b : tmp * (a + 10);
ESCREVER "A: ", a, "B: ", b, "TMP: ", tmp;
end
""")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end=" ")
