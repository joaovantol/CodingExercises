def maximumValue(maximumWeight: int, items: list[dict]) -> int:
    """
    Calculates the maximum value a mountain guide can be paid.

    Args:
        maximumWeight (int): The maximum weight the sherpa can carry
        items (list[dict]): A list containing items and their values

    Returns:
        int: The maximum value the sherpa will be paid
    """
    # Initialize a 1D DP array where dp[w] represents the maximum value
    # for weight w
    dp = [0] * (maximumWeight + 1)

    for item in items:
        print(item)
        weight = item["weight"]
        value = item["value"]
        # Iterate from maximum_weight down to weight to avoid using the same
        # item multiple times
        for w in range(maximumWeight, weight - 1, -1):
            print("w=",w)
            if dp[w - weight] + value > dp[w]:
                dp[w] = dp[w - weight] + value
            print(dp)

    return dp[maximumWeight]

def maximumValueComb(maximumWeight: int, items: list[dict]) -> int:
    """
    Calculates all possible items combinations and gets the maximum value a
    mountain guide can be paid.

    Args:
        maximumWeight (int): The maximum weight the sherpa can carry
        items (list[dict]): A list containing items and their values

    Returns:
        int: The maximum value the sherpa will be paid
    """
    combinations = [[0, 0]]
    for item in items:
        combinations += [[w + item["weight"], v + item["value"]]
                         for w, v in combinations]

    return max(v for w, v in combinations if w <= maximumWeight)