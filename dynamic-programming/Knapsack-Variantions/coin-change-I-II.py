# unlimited supply of coins similar to unbounded knapsack

# https://leetcode.com/problems/coin-change/description/

# https://leetcode.com/problems/coin-change/

from typing import List


def minCoin_memo(nums, amount):
    memo = {}
    nums.sort(reverse=True)

    def helper(n, amt):
        if amt == 0:
            return 0
        if n == 0:
            return float("inf")
        elif (n, amt) in memo:
            return memo[(n, amt)]
        else:
            val = nums[n - 1]
            if val <= amt:
                c1 = 1 + helper(n, amt - val)
                c2 = helper(n - 1, amt)
                c = min(c1, c2)
            else:
                c = float("inf")
            memo[(n, amt)] = c
            return c

    res = helper(len(nums), amount)

    if res >= 10**7:
        return -1
    else:
        return res


def minCoin_tabular(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for each_amo in range(1, amount + 1):
        for coin in coins:
            if each_amo - coin >= 0:
                dp[each_amo] = min(dp[each_amo], 1 + dp[each_amo - coin])

    return dp[amount] if dp[amount] != amount + 1 else -1


print(minCoin_memo([1, 2, 5], 11))
print(minCoin_tabular([1, 2, 5], 11))


# https://leetcode.com/problems/coin-change-ii/


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Initialize dp array
        dp = [0] * (amount + 1)
        dp[0] = 1

        # Update dp array
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]


# Variant - https://practice.geeksforgeeks.org/problems/coin-change2448/1

'''

Given an integer array coins[ ] representing different denominations of currency and an integer sum, find the number of ways you can make sum by using different combinations from coins[ ]. 

Note: Assume that you have an infinite supply of each type of coin. Therefore, you can use any coin as many times as you want.

Answers are guaranteed to fit into a 32-bit integer. 

Examples:

Input: coins[] = [1, 2, 3], sum = 4

Output: 4

Explanation: Four Possible ways are: [1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3].

Input: coins[] = [2, 5, 3, 6], sum = 10

Output: 5

Explanation: Five Possible ways are: [2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 2, 6], [2, 3, 5] and [5, 5].

Input: coins[] = [5, 10], sum = 3

Output: 0

Explanation: Since all coin denominations are greater than sum, no combination can make the target sum.

Constraints:
    1 <= sum <= 103
    1 <= coins[i] <= 104
    1 <= coins.size() <= 103

''' 


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