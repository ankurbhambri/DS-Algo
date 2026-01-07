# 1 means possible to create subset whose sum ewauls to target and 0 means not possible


def subsetSumRecursive(arr, t):

    def helper(i, target):

        if target == 0:
            return 1

        if i < 0 or target < 0:
            return 0

        take = helper(i - 1, target - arr[i - 1])

        not_take = helper(i - 1, target)

        return take or not_take

    return helper(len(arr), t)


def subsetSumMemo(arr, t):

    memo = {}

    def helper(i, target):

        if target == 0:
            return 1

        if i < 0 or target < 0:
            return 0
        
        state = (i, target)
        if state in memo:
            return memo[state]
        
        take = helper(i - 1, target - arr[i - 1])
        not_take = helper(i - 1, target)

        memo[state] = take or not_take

    return helper(len(arr), t)


def subsetSumTabular(arr, target):

    n = len(arr)

    # dp[n+1][target+1] initialized with 0
    dp = [[0] * (target + 1) for _ in range(n + 1)]

    # Base case: Sum 0 is always possible (empty subset)
    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, target + 1):

            if arr[i-1] <= j:
                # Ya toh pichle step se possible tha, ya current minus karke possible hai
                dp[i][j] = dp[i-1][j] or dp[i-1][j - arr[i-1]]

            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][target]


def subsetSum1DP(arr, target):

    # dp[j] batata hai ki sum 'j' possible hai ya nahi
    dp = [False] * (target + 1)
    dp[0] = True

    for num in arr:
        # Reverse loop taaki ek hi element ko bar-bar use na karein
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target]


print(subsetSumRecursive([3, 34, 4, 12, 5, 2], 9))
print(subsetSumRecursive([3, 34, 4, 12, 5, 2], 9))
print(subsetSumTabular([3, 34, 4, 12, 5, 2], 9))
print(subsetSum1DP([3, 34, 4, 12, 5, 2], 9))

# Variation: If asked to count number of subsets with given sum

# Simple in place of (or) just (+)
def subsetSum1DPWays(arr, target):

    # dp[j] batata hai ki sum 'j' possible hai ya nahi
    dp = [False] * (target + 1)
    dp[0] = True

    for num in arr:
        # Reverse loop taaki ek hi element ko bar-bar use na karein
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] + dp[j - num]

    return dp[target]

print(subsetSum1DPWays([1, 2, 1], 2))