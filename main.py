import sys

from grammar import Grammar
from eval_interpreter import EvalInterpreter


if __name__ == "__main__":
    filename = sys.argv[1]
    g = Grammar()
    g.build()

    with open(filename, "r") as file:
        content = file.read()

    ops = g.parse(content)
    try :
        for op in ops:
            EvalInterpreter._eval_operator(op)
    except Exception as e:
        print(f"Error: {e}")