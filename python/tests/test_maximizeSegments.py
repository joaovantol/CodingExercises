import pytest

from codingexercises.maximizeSegments import maximizeSegments

TEST_CASES = [
    (4, 2, 1, 1, 4, "example_1"),
    (5, 5, 3, 2, 2, "example_2"),
    (7, 8, 9, 10, 0, "example_3"),
    (11, 2, 3, 5, 5, "example_4"),
]


@pytest.mark.parametrize("n,x,y,z,expected_max_segments,test_name", TEST_CASES)
def test_max_segments(
    n: int, x: int, y: int, z: int, expected_max_segments: int, test_name: str
) -> None:
    """Test maximizeSegments function with all test cases."""
    result = maximizeSegments(n, x, y, z)
    assert result == expected_max_segments, (
        f"Test {test_name} failed: maximizeSegments({n,x,y,z}) = {result}, "
        f"expected {expected_max_segments}"
    )
