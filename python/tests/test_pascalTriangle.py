from pytest import raises

from codingexercises.pascalTriangle import (
    pascal_row_bincoef,
    pascal_row_dp,
    pascal_row_iterative,
    pascal_row_recursive,
    pascal_row_reduce,
)


def test_bincoef_row_4() -> None:
    expected = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
    ]

    assert expected == pascal_row_bincoef(4)


def test_iterative_row_4() -> None:
    expected = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
    ]

    assert expected == pascal_row_iterative(4)


def test_reduce_row_4() -> None:
    expected = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
    ]

    assert expected == pascal_row_reduce(4)


def test_recursive_row_4() -> None:
    expected = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
    ]

    assert expected == pascal_row_recursive(4)


def test_dp_row_4() -> None:
    expected = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
    ]

    assert expected == pascal_row_dp(4)


def test_expansion_row_10() -> None:
    expected = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
    ]

    assert expected == pascal_row_bincoef(10)


def test_iterative_row_10() -> None:
    expected = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
    ]

    assert expected == pascal_row_iterative(10)


def test_reduce_row_10() -> None:
    expected = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
    ]

    assert expected == pascal_row_reduce(10)


def test_recursive_row_10() -> None:
    expected = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
    ]

    assert expected == pascal_row_recursive(10)


def test_dp_row_10() -> None:
    expected = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
    ]

    assert expected == pascal_row_dp(10)


def test_expansion_row_error() -> None:
    with raises(ValueError, match="n must be a positive integer"):
        pascal_row_bincoef(0)


def test_iterative_row_error() -> None:
    with raises(ValueError, match="n must be a positive integer"):
        pascal_row_iterative(0)


def test_reduce_row_error() -> None:
    with raises(ValueError, match="n must be a positive integer"):
        pascal_row_reduce(0)


def test_recursive_row_error() -> None:
    with raises(ValueError, match="n must be a positive integer"):
        pascal_row_recursive(0)


def test_dp_row_error() -> None:
    with raises(ValueError, match="n must be a positive integer"):
        pascal_row_dp(0)
