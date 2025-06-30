def maximum_value(maximum_weight, items):
    # Initialize a 1D DP array where dp[w] represents the maximum value for weight w
    dp = [0] * (maximum_weight + 1)

    for item in items:
        weight = item["weight"]
        value = item["value"]
        # Iterate from maximum_weight down to weight to avoid using the same item multiple times
        for w in range(maximum_weight, weight - 1, -1):
            if dp[w - weight] + value > dp[w]:
                dp[w] = dp[w - weight] + value

    return dp[maximum_weight]

# items = [
#     {"weight": 5, "value": 10},
#     {"weight": 4, "value": 40},
#     {"weight": 6, "value": 30},
#     {"weight": 4, "value": 50}
# ]
# print(maximum_value(10, items))  # Output: 90 (items 2 and 4)