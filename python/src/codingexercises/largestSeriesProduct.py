import numpy as np


def largest_product(series: str, size: int) -> int:
    """
    Calculate the largest product of a contiguous substring of digits of given
    length.

    Args:
        series: A string of digits (0-9).
        size: The length of the contiguous substring to consider.

    Returns:
        The largest product of all digits in any contiguous substring of the
        given length.

    Raises:
        ValueError: If the input contains non-digit characters or if size is
        invalid.
    """
    if not size:
        raise ValueError("span must not be zero")
    if 0 > size:
        raise ValueError("span must not be negative")
    if size > len(series):
        raise ValueError("span must not exceed string length")
    if not series.isdigit():
        raise ValueError("digits input must only contain digits")

    nums = [int(digit) for digit in series]
    slices: list[list[int]] = [nums[i : i + size] for i in range(len(nums) - size + 1)]
    products = np.prod(slices, axis=1)

    return int(max(products))
