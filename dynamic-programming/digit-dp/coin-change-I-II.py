# unlimited supply of coins similar to unbounded knapsack

# https://leetcode.com/problems/coin-change/


class Solution:
    def coinChange(self, coins, amount):

        memo = {}
        coins.sort(reverse=True)

        def helper(n, amt):

            if amt == 0:
                return 0

            if n == 0:
                return float("inf")

            elif (n, amt) in memo:
                return memo[(n, amt)]

            else:

                val = coins[n - 1]

                c = float("inf")

                if val <= amt:

                    c1 = 1 + helper(n, amt - val) # we can use the same coin again, so n is not reduced
                    c2 = helper(n - 1, amt) # we can skip the coin and move to the next coin, so n is reduced
                    c = min(c1, c2)                

                memo[(n, amt)] = c
                return c

        res = helper(len(coins), amount)

        return -1 if res == float("inf") else res

# Iterative Tabular Solution
def minCoin_tabular(coins, amount):

    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for amt in range(coin, amount + 1):
            dp[amt] = min(dp[amt], 1 + dp[amt - coin])

    return dp[amount] if dp[amount] != float("inf") else -1


print(Solution().coinChange([1, 2, 5], 11))
print(minCoin_tabular([1, 2, 5], 11))


# https://leetcode.com/problems/coin-change-ii/
# Similar: https://practice.geeksforgeeks.org/problems/coin-change2448/1
# https://cses.fi/problemset/task/1636/

class Solution:
    def change(self, amount, coins):

        # Initialize dp array
        dp = [0] * (amount + 1)
        dp[0] = 1

        # Update dp array
        for coin in coins:
            for amt in range(coin, amount + 1):
                dp[amt] += dp[amt - coin]

        return dp[amount]

print(Solution().change(5, [1, 2, 3]))