import math
from functools import reduce


def pascal_row_bincoef(n: int) -> list[int]:
    """
    Calculates the nth row of Pascal's triangle using binomial coefficients.

    Args:
        n (int): The number of the row to calculate

    Returns:
        A list containing the nth row.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    return [math.comb(n - 1, k) for k in range(n)]


def pascal_row_iterative(n: int) -> list[int]:
    """
    Calculates the nth row of Pascal's triangle using iteration.

    Args:
        n (int): The number of the row to calculate

    Returns:
        A list containing the nth row.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    row = [1]
    for _ in range(n - 1):
        row = [x + y for x, y in zip([0] + row, row + [0])]

    return row


def pascal_row_reduce(n: int) -> list[int]:
    """
    Calculates the nth row of Pascal's triangle using reduce and a lambda
    function.

    Args:
        n (int): The number of the row to calculate

    Returns:
        A list containing the nth row.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    return reduce(
        lambda row, _: [x + y for x, y in zip([0] + row, row + [0])],
        range(n - 1),
        [1],
    )


def pascal_row_recursive(
    n: int,
    row: list[int] = [1],
) -> list[int]:
    """
    Calculates the nth row of Pascal's triangle using recursion.

    Args:
        n (int): The number of the row to calculate

    Returns:
        A list containing the nth row.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    if n == 1:
        return row

    return pascal_row_recursive(
        n - 1,
        [x + y for x, y in zip([0] + row, row + [0])],
    )


def pascal_row_dp(n: int) -> list[int]:
    """
    Calculates the nth row of Pascal's triangle using dynamic programming.

    Args:
        n (int): The number of the row to calculate

    Returns:
        A list containing the nth row.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    triangle = [[1] * i for i in range(1, n + 1)]

    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle[-1]
