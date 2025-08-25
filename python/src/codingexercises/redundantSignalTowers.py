def redundant_towers(x: list[int], k: list[int]) -> int:
    """
    Find the maximum number of towers that can be shut down such that
    the minimum value of S_i(x) = |x - x_i| + k_i remains unchanged for all x.

    Based on the insight: Si(j) >= Sj(j) <=> for all x, Si(x) >= Sj(x)

    A tower j is redundant if there exists another tower i such that:
    Si(j) <= Sj(j), which means Si(x) <= Sj(x) for all x.

    Args:
        x: List of integers representing tower positions
        k: List of integers representing coefficients

    Returns:
        int: Maximum number of towers that can be shut down
    """
    n = len(x)
    if n <= 1:
        return 0

    redundant_count = 0
    for j in range(n):
        if is_tower_redundant(j, x, k):
            redundant_count += 1

    return redundant_count


def is_tower_redundant(j: int, x: list[int], k: list[int]) -> bool:
    """
    Check if tower j is redundant (dominated by another tower).

    Tower j is redundant if there exists another tower i such that:
    S_i(j) = |x_j - x_i| + k_i <= k_j = S_j(j)

    This means tower i provides equal or better service everywhere than tower j.

    Args:
        j: Index of tower to check
        x: List of tower positions
        k: List of coefficients

    Returns:
        bool: True if tower j is redundant, False otherwise
    """
    x_j, k_j = x[j], k[j]

    for i in range(len(x)):
        if i == j:
            continue

        x_i, k_i = x[i], k[i]

        s_i_at_j = abs(x_j - x_i) + k_i

        if s_i_at_j <= k_j:
            return True

    return False
