from typing import Literal

import pytest
from pytest import raises

from codingexercises.catalanNumber import findCatalan

TEST_CASES = [
    (2, "recursion", 2, "test_1"),
    (3, "recursion", 5, "test_2"),
    (4, "recursion", 14, "test_3"),
    (5, "recursion", 42, "test_4"),
    (6, "dp", 132, "test_5"),
    (7, "dp", 429, "test_6"),
    (8, "dp", 1430, "test_7"),
    (9, "dp", 4862, "test_8"),
]

TEST_ERROR_CASES = [
    (-1, "recursion", "n must be non-negative", "test_9"),
    (-1, "dp", "n must be non-negative", "test_10"),
    (4, "recursão", "invalid method", "test_11"),
    (5, "DP", "invalid method", "test_12"),
    (6, "", "invalid method", "test_13"),
]


@pytest.mark.parametrize("n,method,expected_nth_catalan,test_name", TEST_CASES)
def test_nth_catalan(
    n: int,
    method: Literal["recursion", "dp"],
    expected_nth_catalan: int,
    test_name: str,
) -> None:
    """Test findCatalan function with test cases."""
    result = findCatalan(n, method)
    assert result == expected_nth_catalan, (
        f"Test {test_name} failed: findCatalan({n,method}) = {result}, "
        f"expected {expected_nth_catalan}"
    )


@pytest.mark.parametrize("n,method,expected_error,test_name", TEST_ERROR_CASES)
def test_nth_catalan_error(
    n: int, method: Literal["recursion", "dp"], expected_error: int, test_name: str
) -> None:
    """Test findCatalan function with error test cases."""
    with raises(ValueError, match=expected_error):
        findCatalan(n, method)
