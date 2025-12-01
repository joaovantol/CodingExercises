from pytest import raises

from codingexercises.rpn import RPNCalculator


def test_example_1() -> None:
    expression = ["2", "1", "+", "3", "*"]
    calc = RPNCalculator()

    assert calc.evaluate(expression) == 9.0


def test_example_2() -> None:
    expression = ["4", "13", "5", "///", "+"]
    calc = RPNCalculator()

    assert calc.evaluate(expression) == 6.0


def test_example_3() -> None:
    expression = [
        "10",
        "6",
        "9",
        "3",
        "+",
        "-11",
        "*",
        "///",
        "*",
        "17",
        "+",
        "5",
        "+",
    ]
    calc = RPNCalculator()

    assert calc.evaluate(expression) == 22.0


def test_example_3_with_truediv() -> None:
    expression = [
        "10",
        "6",
        "9",
        "3",
        "+",
        "-11",
        "*",
        "/",
        "*",
        "17",
        "+",
        "5",
        "+",
    ]
    calc = RPNCalculator()

    assert calc.evaluate(expression) == 21.545454545454547


def test_example_3_with_floordiv() -> None:
    expression = [
        "10",
        "6",
        "9",
        "3",
        "+",
        "-11",
        "*",
        "//",
        "*",
        "17",
        "+",
        "5",
        "+",
    ]
    calc = RPNCalculator()

    assert calc.evaluate(expression) == 12.0


def test_insufficient_operands() -> None:
    expression = ["2", "+"]
    calc = RPNCalculator()

    with raises(ValueError):
        calc.evaluate(expression)


def test_division_by_zero() -> None:
    expression = ["2", "0", "/"]
    calc = RPNCalculator()

    with raises(ZeroDivisionError):
        calc.evaluate(expression)


def test_invalid_token() -> None:
    expression = ["2", "1", "cos"]
    calc = RPNCalculator()

    with raises(ValueError):
        calc.evaluate(expression)


def test_invalid_expression_with_leftover_number() -> None:
    expression = ["2", "1", "+", "2"]
    calc = RPNCalculator()

    with raises(ValueError):
        calc.evaluate(expression)
