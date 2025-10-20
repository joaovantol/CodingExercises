from pytest import raises

from codingexercises.pascalTriangle import (
    dp_pascal_row,
    expansion_pascal_row,
    iterative_pascal_row,
    recursive_pascal_row,
)


def test_expansion_row_4() -> None:
    expected = [1, 3, 3, 1]

    assert expected == expansion_pascal_row(4)


def test_iterative_row_4() -> None:
    expected = [1, 3, 3, 1]

    assert expected == iterative_pascal_row(4)


def test_recursive_row_4() -> None:
    expected = [1, 3, 3, 1]

    assert expected == recursive_pascal_row(4)


def test_dp_row_4() -> None:
    expected = [1, 3, 3, 1]

    assert expected == dp_pascal_row(4)


def test_expansion_row_10() -> None:
    expected = [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

    assert expected == expansion_pascal_row(10)


def test_iterative_row_10() -> None:
    expected = [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

    assert expected == iterative_pascal_row(10)


def test_recursive_row_10() -> None:
    expected = [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

    assert expected == recursive_pascal_row(10)


def test_dp_row_10() -> None:
    expected = [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

    assert expected == dp_pascal_row(10)


def test_expansion_row_error() -> None:
    with raises(ValueError, match="n must be a positive integer"):
        expansion_pascal_row(0)


def test_iterative_row_error() -> None:
    with raises(ValueError, match="n must be a positive integer"):
        iterative_pascal_row(0)


def test_recursive_row_error() -> None:
    with raises(ValueError, match="n must be a positive integer"):
        recursive_pascal_row(0)


def test_dp_row_error() -> None:
    with raises(ValueError, match="n must be a positive integer"):
        dp_pascal_row(0)
