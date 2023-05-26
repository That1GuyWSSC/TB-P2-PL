class EvalInterpreter:
    symbols = {}
    operators = {
        "escrever": lambda args: EvalInterpreter._escreve(args),
        "+": lambda args: args[0] + args[1],
        "-": lambda args: args[0] - args[1],
        "*": lambda args: args[0] * args[1],
        "/": lambda args: args[0] / args[1],
    }

    @staticmethod
    def _escreve(args):
        print("".join([str(arg) for arg in args]))

    @staticmethod
    def _evaluate(ast):
        if type(ast) in (bool, float):
            return ast
        if type(ast) is dict:
            return EvalInterpreter._eval_operator(ast)
        if type(ast) is str:
            var = ast
            if var in EvalInterpreter.symbols:
                return EvalInterpreter.symbols[ast]
            else:
                return ast

        raise Exception("Unknown AST type")

    @staticmethod
    def _eval_operator(ast):
        """ast = {'operator': '...', 'args: [...]}"""

        if 'operator' in ast:
            op = ast["operator"]
            args = [EvalInterpreter._evaluate(a) for a in ast['args']]
            if op in EvalInterpreter.operators:
                func = EvalInterpreter.operators[op]
                return func(args)
            else:
                raise Exception(f"Unknown operator {op}")

        if 'var' in ast:
            return ast['var']

        raise Exception('Undefined AST')