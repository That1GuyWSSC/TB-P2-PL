from grammar import Grammar
from eval_interpreter import EvalInterpreter

content = """
start
ESCREVER "maria ",  "ana", "=", 9+2;
ESCREVER "maria", "joaquim", "=", 0;
ESCREVER "soma de ", 9, "com ", 3*4, "=", 2+2*3;
end
"""


if __name__ == "__main__":
    g = Grammar()
    g.build()
    ops = g.parse(content)
    for op in ops:
        EvalInterpreter._eval_operator(op)