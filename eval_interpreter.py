class EvalInterpreter:
    symbols = {}
    operators = {
        "escrever": lambda args: EvalInterpreter._escreve(args),
        "+": lambda args: args[0] + args[1],
        "-": lambda args: args[0] - args[1],
        "*": lambda args: args[0] * args[1],
        "/": lambda args: args[0] / args[1],

        "assign": lambda args: EvalInterpreter._assign_var(args),
        "declare": lambda args: EvalInterpreter._declare_var(args),
        "assign_declare": lambda args: EvalInterpreter._assign_declare_var(args),
    }

    @staticmethod
    def _assign_declare_var(args):
        if args[1] in EvalInterpreter.symbols:
            raise Exception(f"Variavel {args[1]} ja em uso.")
        return args

    @staticmethod
    def _declare_var(args):
        for arg in args:
            EvalInterpreter.symbols[arg[1]] = arg[0]

    @staticmethod
    def _assign_var(args):
        if args[1] in EvalInterpreter.symbols:
            EvalInterpreter.symbols[args[1]] = args[0]
        else:
            raise Exception(f"Varivel {args[1]} nao existe.")

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

        if ast is None:
            return None

        raise Exception("Unknown AST type")

    @staticmethod
    def _eval_operator(ast):
        """ast = {'operator': '...', 'args: [...]}"""

        if 'operator' in ast:
            op = ast["operator"]
            args = [EvalInterpreter._evaluate(a) for a in ast['args']]
            if op in EvalInterpreter.operators:
                func = EvalInterpreter.operators[op]
                if "data" in ast:
                    args.append(ast["data"])
                return func(args)
            else:
                raise Exception(f"Unknown operator {op}")

        if 'var' in ast:
            if ast['var'] in EvalInterpreter.symbols:
                return EvalInterpreter.symbols[ast['var']]
            raise Exception(f"Nao existe a variavel {ast['var']}")

        raise Exception('Undefined AST')