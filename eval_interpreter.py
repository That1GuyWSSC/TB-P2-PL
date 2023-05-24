class EvalInterpreter:
     operators = {
        "escrever": lambda args: [print(arg) for arg in args]
    }
