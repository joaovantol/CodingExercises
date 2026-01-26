def maximizeSegments(n: int, x: int, y: int, z: int) -> int:
    """
    Given the task to cut a rod of length n, calculates the maximum number of
    segments of length x, y or z. This function uses a bottom-up dynamic
    programming approach.

    Args:
    n: rod length
    x: segment length
    y: segment length
    z: segment length

    Returns:
    The maximum number of segments.
    """

    dp = [0] * (n + 1)

    for i in range(1, n + 1):

        if i >= x and dp[i - x] != -1:
            dp[i] = max(dp[i], dp[i - x] + 1)

        if i >= y and dp[i - y] != -1:
            dp[i] = max(dp[i], dp[i - y] + 1)

        if i >= z and dp[i - z] != -1:
            dp[i] = max(dp[i], dp[i - z] + 1)

        if dp[i] == 0:
            dp[i] = -1

    if dp[n] == -1:
        return 0

    return dp[n]
