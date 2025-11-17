import math
from functools import reduce


def pascal_row_bincoef(n: int) -> list[list[int]]:
    """
    Calculates the nth row of Pascal's triangle using binomial coefficients.

    Args:
        n (int): The number of the row to calculate

    Returns:
        A list containing the Pascal triangle up to nth row.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    triangle = [[1]]

    for row_num in range(2, n + 1):
        triangle.append([math.comb(row_num - 1, k) for k in range(row_num)])

    return triangle


def pascal_row_iterative(n: int) -> list[list[int]]:
    """
    Calculates the nth row of Pascal's triangle using iteration.

    Args:
        n (int): The number of the row to calculate

    Returns:
        A list containing the Pascal triangle up to nth row.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    triangle = [[1]]

    for _ in range(n - 1):
        triangle.append(
            [x + y for x, y in zip([0] + triangle[-1], triangle[-1] + [0])],
        )

    return triangle


def pascal_row_reduce(n: int) -> list[list[int]]:
    """
    Calculates the nth row of Pascal's triangle using reduce and a lambda
    function.

    Args:
        n (int): The number of the row to calculate

    Returns:
        A list containing the Pascal triangle up to nth row.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    triangle = [[1]]

    for row_num in range(2, n + 1):
        triangle.append(
            reduce(
                lambda row, _: [x + y for x, y in zip([0] + row, row + [0])],
                range(row_num - 1),
                [1],
            )
        )

    return triangle


def pascal_row_recursive(
    n: int,
    row: list[int] = [1],
) -> list[list[int]]:
    """
    Calculates the nth row of Pascal's triangle using recursion.

    Args:
        n (int): The number of the row to calculate

    Returns:
        A list containing the Pascal triangle up to nth row.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    if n == 1:
        return [[1]]

    else:
        result = pascal_row_recursive(
            n - 1,
            [x + y for x, y in zip([0] + row, row + [0])],
        )
        last_row: list[int] = result[-1]
        new_row: list[int] = (
            [1]
            + [last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1)]
            + [1]
        )
        result.append(new_row)
        return result


def pascal_row_dp(n: int) -> list[list[int]]:
    """
    Calculates the nth row of Pascal's triangle using dynamic programming.

    Args:
        n (int): The number of the row to calculate

    Returns:
        A list containing the Pascal triangle up to nth row.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    triangle = [[1] * i for i in range(1, n + 1)]

    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle
