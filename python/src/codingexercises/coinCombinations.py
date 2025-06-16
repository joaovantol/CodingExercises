def coinCombinations(target):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    dp = [0] * (target + 1)
    dp[0] = 1

    for coin in coins:
        for amount in range(coin, target + 1):
            dp[amount] += dp[amount - coin]

    return dp[amount]
