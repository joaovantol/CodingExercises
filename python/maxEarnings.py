def max_earnings(earnings, k):
    n = len(earnings)
    if n == 0:
        return 0

    dp = [0] * n

    for i in range(n):
        # Option 1: skip today, so dp[i] = dp[i - 1]
        max_val = dp[i - 1] if i > 0 else 0
        total = 0

        # Option 2: work for d days ending today (d from 1 to k)
        for d in range(1, k + 1):
            if i - d + 1 < 0:
                break
            total += earnings[i - d + 1]
            prev = dp[i - d - 1] if i - d - 1 >= 0 else 0
            max_val = max(max_val, total + prev)

        dp[i] = max_val

    return dp[-1]

def max_earnings(earnings, k):
    n = len(earnings)
    dp = [[float('-inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # Base case: before first day, we rest

    for i in range(1, n + 1):  # Day i corresponds to earnings[i-1]
        # If we rest today
        dp[i][0] = max(dp[i - 1])

        # If we work today with j consecutive days
        for j in range(1, k + 1):
            if dp[i - 1][j - 1] != float('-inf'):
                dp[i][j] = dp[i - 1][j - 1] + earnings[i - 1]

    return dp

def maxEarnings(earnings, k):
    n = len(earnings)
    cumEarnings = [[-1] * (k + 1) for _ in range(n + 1)]
    cumEarnings[0][0] = 0

    for day in range(1, n + 1):  # Day i corresponds to earnings[i-1]
        # If we rest today
        cumEarnings[day][0] = max(cumEarnings[day - 1])

        # If we work today with j consecutive days
        for j in range(1, k + 1):
            if cumEarnings[day - 1][j - 1] != -1:
                cumEarnings[day][j] = cumEarnings[day - 1][j - 1] + earnings[day - 1]

    return cumEarnings

earnings = [60, 70, 80, 40, 80, 90, 100, 20]
k = 3

earnings = [45, 12, 78, 34, 56, 89, 23, 67, 91]
k = 4