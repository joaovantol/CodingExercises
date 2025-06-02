def maxEarnings(earnings, k):
    n = len(earnings)
    cumEarnings = [[-1] * (k + 1) for _ in range(n + 1)]
    cumEarnings[0][0] = 0

    for day in range(1, n + 1):
        cumEarnings[day][0] = max(cumEarnings[day - 1])

        for i in range(1, k + 1):
            if cumEarnings[day - 1][i - 1] >= 0:
                cumEarnings[day][i] = cumEarnings[day - 1][i - 1] + earnings[day - 1]

    return max(cumEarnings[n])



maxEarnings([60, 70, 80, 40, 80, 90, 100, 20], 3)
maxEarnings([45, 12, 78, 34, 56, 89, 23, 67, 91], 4)
maxEarnings([12, 45, 56, 34, 78, 89, 23, 67, 91], 4)
