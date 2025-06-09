def maxEarnings(earnings, k):
    n = len(earnings)
    cumEarnings = [[-1] * (k + 1) for _ in range(n + 1)]
    cumEarnings[0][0] = 0

    for day in range(1, n + 1):
        for consecutive in range(k + 1):
            if consecutive == 0:
                bestPrevious = max(cumEarnings[day - 1])
                cumEarnings[day][0] = bestPrevious
            else:
                if cumEarnings[day - 1][consecutive - 1] > -1:
                    val = cumEarnings[day - 1][consecutive - 1] + earnings[day - 1]
                    cumEarnings[day][consecutive] = val

    maxEarning = max(cumEarnings[n])

    return maxEarning

maxEarnings([60, 70, 80, 40, 80, 90, 100, 20], 3)
maxEarnings([45, 12, 78, 34, 56, 89, 23, 67, 91], 4)
maxEarnings([12, 45, 56, 34, 78, 89, 23, 67, 91], 4)

