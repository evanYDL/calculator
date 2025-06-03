import ast
import operator
import sys

operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
}

def eval_expr(expr):
    """Safely evaluate a math expression."""
    def _eval(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            left = _eval(node.left)
            right = _eval(node.right)
            op_type = type(node.op)
            if op_type in operators:
                return operators[op_type](left, right)
            else:
                raise TypeError(f"Unsupported operator: {op_type}")
        elif isinstance(node, ast.UnaryOp):
            operand = _eval(node.operand)
            op_type = type(node.op)
            if op_type in operators:
                return operators[op_type](operand)
            else:
                raise TypeError(f"Unsupported operator: {op_type}")
        else:
            raise TypeError(f"Unsupported expression: {node}")

    tree = ast.parse(expr, mode='eval')
    return _eval(tree.body)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python calculator.py '<expression>'")
        sys.exit(1)
    expression = " ".join(sys.argv[1:])
    try:
        result = eval_expr(expression)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

