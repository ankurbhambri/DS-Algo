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
