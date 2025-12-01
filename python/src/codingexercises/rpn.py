import operator
from typing import Any, List, Union


class RPNCalculator:
    """
    A Reverse Polish Notation (RPN) calculator that evaluates arithmetic expressions.

    Reverse Polish Notation is a mathematical notation where operators follow their operands.
    This eliminates the need for parentheses and follows the stack-based evaluation principle.
    """

    def __init__(self) -> None:
        """Initialize the RPN calculator with supported operators."""
        self._operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
            "//": operator.floordiv,
            "%": operator.mod,
            "**": operator.pow,
        }

    def evaluate(self, expression: Union[str, List[str]]) -> float:
        """
        Evaluate a Reverse Polish Notation expression.

        Args:
            expression: Either a space-separated string or list of tokens in RPN format

        Returns:
            float: The result of the evaluated expression

        Raises:
            ValueError: If the expression is invalid or contains unsupported operators
            ZeroDivisionError: If division by zero occurs

        Examples:
            >>> calc = RPNCalculator()
            >>> calc.evaluate("3 4 +")
            7.0
            >>> calc.evaluate(["2", "3", "*", "4", "+"])
            10.0
        """
        if isinstance(expression, str):
            tokens = expression.split()
        else:
            tokens = expression

        stack: list[float] = []

        for token in tokens:
            if self._is_number(token):
                stack.append(float(token))
            elif token in self._operators or token == "///":
                if len(stack) < 2:
                    raise ValueError(f"Insufficient operands for operator '{token}'")

                operand2 = stack.pop()
                operand1 = stack.pop()

                try:
                    result = self._apply_operator(token, operand1, operand2)
                    stack.append(result)
                except ZeroDivisionError:
                    raise ZeroDivisionError(
                        f"Division by zero in operation {operand1} {token} {operand2}"
                    )
            else:
                raise ValueError(f"Invalid token: '{token}'")

        if len(stack) != 1:
            raise ValueError(
                f"Invalid expression: stack has {len(stack)} elements instead of 1"
            )

        return stack[0]

    def _is_number(self, token: str) -> bool:
        """
        Check if a token represents a valid number.

        Args:
            token: The token to check

        Returns:
            bool: True if the token is a valid number, False otherwise
        """
        try:
            float(token)
            return True
        except ValueError:
            return False

    def divisionTruncToZero(self, operand1: float, operand2: float) -> int:
        return int(operand1 / operand2)

    def _apply_operator(self, operator: str, operand1: float, operand2: float) -> Any:
        """
        Apply an operator to two operands.

        Args:
            operator: The operator to apply (+, -, *, /, etc.)
            operand1: The first operand
            operand2: The second operand

        Returns:
            float: The result of the operation

        Raises:
            ValueError: If the operator is not supported
        """
        if operator == "///":
            return self.divisionTruncToZero(operand1, operand2)

        if operator not in self._operators:
            raise ValueError(f"Unsupported operator: '{operator}'")

        return self._operators[operator](operand1, operand2)

    def get_supported_operators(self) -> List[str]:
        """
        Get the list of supported operators.

        Returns:
            List[str]: List of supported operator symbols
        """
        operators = list(self._operators.keys())
        operators.append("///")

        return operators

    def validate_expression(self, expression: Union[str, List[str]]) -> bool:
        """
        Validate if an RPN expression is syntactically correct.

        Args:
            expression: The RPN expression to validate

        Returns:
            bool: True if the expression is valid, False otherwise
        """
        try:
            self.evaluate(expression)
            return True
        except (ValueError, ZeroDivisionError):
            return False
