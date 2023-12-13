# unlimited supply of coins similar to unbounded knapsack

# https://practice.geeksforgeeks.org/problems/coin-change2448/1


def coin_change_memo(coins, N, amount):
    memo = {}

    def helper(n, amt):
        if amt == 0:
            return 1
        elif n == 0:
            return 0
        elif (n, amt) in memo:
            return memo[(n, amt)]
        else:
            val = coins[n - 1]
            if val <= amt:
                c1 = helper(n, amt - val)
                c2 = helper(n - 1, amt)
                c = c1 + c2
            else:
                c = helper(n - 1, amt)

            memo[(n, amt)] = c
            return c

    return helper(N, amount)


def coin_change_tabular(coins, N, amount):
    dp = [[0] * (amount + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        for amt in range(amount + 1):
            if amt == 0:
                dp[i][amt] = 1
            elif i == 0:
                dp[i][amt] = 0
            else:
                val = coins[i - 1]
                if val <= amt:
                    c1 = dp[i][amt - val]
                    c2 = dp[i - 1][amt]
                    dp[i][amt] = c1 + c2
                else:
                    dp[i][amt] = dp[i - 1][amt]

    return dp[N][amount]


amount = 10
N = 4
coins = [2, 5, 3, 6]

print(coin_change_memo(coins, N, amount))
print(coin_change_tabular(coins, N, amount))
