# calculator/pkg/calculator.py

class Calculator:
    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

    def evaluate(self, expression):
        if not expression or expression.isspace():
            return None
        tokens = expression.strip().split()
        return self._evaluate_infix(tokens)

    def _evaluate_infix(self, tokens):
        values = []
        operators = []
        expect_number = True  # Start by expecting a number

        for token in tokens:
            if token in self.operators:
                if expect_number:
                    raise ValueError(f"invalid expression: unexpected operator '{token}'")
                while (
                    operators
                    and operators[-1] in self.operators
                    and self.precedence[operators[-1]] >= self.precedence[token]
                ):
                    self._apply_operator(operators, values)
                operators.append(token)
                expect_number = True  # After an operator, expect a number
            else:
                if not expect_number:
                    raise ValueError(f"invalid expression: unexpected number '{token}'")
                try:
                    values.append(float(token))
                except ValueError:
                    raise ValueError(f"invalid token: {token}")
                expect_number = False  # After a number, expect an operator

        # After processing all tokens, if we are still expecting a number,
        # it means the expression ended with an operator or was empty.
        # If it ended with an operator, it's an error.
        if expect_number and tokens:
            raise ValueError("invalid expression: ends with an operator")

        while operators:
            self._apply_operator(operators, values)

        if len(values) != 1:
            raise ValueError("invalid expression")

        return values[0]

    def _apply_operator(self, operators, values):
        if not operators:
            return

        operator = operators.pop()
        if len(values) < 2:
            raise ValueError(f"not enough operands for operator {operator}")

        b = values.pop()
        a = values.pop()
        if operator == "/" and b == 0:
            raise ValueError("float division by zero")
        values.append(self.operators[operator](a, b))