import pytest

from codingexercises.staircase import minimumCostDP, optimizedMinimumCostDP

TEST_CASES = [
    ([10, 15, 20], 15, "example_1"),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6, "example_2"),
    ([16, 19, 10, 12, 18], 31, "example_3"),
    ([7], 7, "example_4"),
    ([44, 3], 3, "example_5"),
    ([3, 44], 3, "example_6"),
]


@pytest.mark.parametrize("cost,expected_min_cost,test_name", TEST_CASES)
def test_min_cost_dp(cost: list[int], expected_min_cost: int, test_name: str) -> None:
    """Test minimumCostDP function with all test cases."""
    result = minimumCostDP(cost)
    assert result == expected_min_cost, (
        f"Test {test_name} failed: minimumCostDP({cost}) = {result}, "
        f"expected {expected_min_cost}"
    )


@pytest.mark.parametrize("cost,expected_min_cost,test_name", TEST_CASES)
def test_optimized_min_cost_dp(
    cost: list[int], expected_min_cost: int, test_name: str
) -> None:
    """Test optimizedMinimumCostDP function with all test cases."""
    result = optimizedMinimumCostDP(cost)
    assert result == expected_min_cost, (
        f"Test {test_name} failed: optimizedMinimumCostDP({cost}) = {result}, "
        f"expected {expected_min_cost}"
    )
