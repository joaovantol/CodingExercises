def minimumCostDP(cost: list[int]) -> int:
    """
    Calculates the minimum cost to climb a staircase. This function uses a
    bottom-up dynamic programming approach.

    Args:
    cost: List containing the cost for each step on the staircase.

    Returns:
    The minimum cost to climb the staircase.
    """
    n = len(cost)

    if n == 1:
        return cost[0]

    if n == 2:
        return min(cost[0], cost[1])

    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

    return min(dp[n - 1], dp[n - 2])


def optimizedMinimumCostDP(cost: list[int]) -> int:
    """
    Calculates the minimum cost to climb a staircase. This function uses an
    optimized dynamic programming approach.

    Args:
    cost: List containing the cost for each step on the staircase.

    Returns:
    The minimum cost to climb the staircase.
    """
    n = len(cost)

    if n == 1:
        return cost[0]

    if n == 2:
        return min(cost[0], cost[1])

    prev2 = cost[0]
    prev1 = cost[1]

    for i in range(2, n):
        curr = cost[i] + min(prev1, prev2)
        prev2 = prev1
        prev1 = curr

    return min(prev1, prev2)
