def findCatalan(n: int, method: str) -> int:
    """
    This function calculates the nth Catalan number.

    Args:
    n: The n-th Catalan number to be calculated. Must be a non-negative
    integer.
    method: String indicating which method to be used ("recursion" or "dp")

    Returns:
    The n-th Catalan number.
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    res = 0

    if method == "recursion":
        res = catalanRecursion(n)

    if method == "dp":
        res = catalanDP(n)

    if not res:
        raise ValueError("invalid method")

    return res


def catalanRecursion(n: int) -> int:
    """
    This function uses recursion to calculate the n-th Catalan number.

    Args:
    n: The n-th Catalan number to be calculated. Must be a non-negative
    integer.

    Returns:
    The n-th Catalan number.
    """
    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += catalanRecursion(i) * catalanRecursion(n - i - 1)

    return res


def catalanDP(n: int) -> int:
    """
    This function uses a bottom-up dynamic programming approach to calculate the
    n-th Catalan number.

    Args:
    n: The n-th Catalan number to be calculated. Must be a non-negative integer.

    Returns:
    The n-th Catalan number.
    """
    dp = [1, 1] + [0] * (n - 1)

    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]

    return dp[n]
