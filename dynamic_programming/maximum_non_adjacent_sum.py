# https://www.codingninjas.com/codestudio/problems/maximum-sum-of-non-adjacent-elements_843261


# memoization
def maximumNonAdjacentSum(nums):
    memo = [-1] * len(nums)

    def helper(i):
        if i == 0:
            return nums[i]
        if i < 0:
            return 0

        if memo[i] != -1:
            return memo[i]
        # if i pick index 1 then cannot pick 2 because it will adjacent to pick i + 2
        # in our case we are running n - 1 thats why i - 1, i - 2
        memo[i] = max(nums[i] + helper(i - 2), helper(i - 1))

        return memo[i]

    return helper(len(nums) - 1)


# tabulation
# take idea from memoization


def maximumNonAdjacentSum(nums):
    n = len(nums)
    dp = [0] * n
    # base case check in memoization
    dp[0] = nums[0]

    for i in range(1, n):
        take = nums[i] + (dp[i - 2] if i > 1 else 0)  # to prevent out of boud cndt
        nontake = dp[i - 1]
        dp[i] = max(take, nontake)
    return dp[n - 1]


# space optimization
def maximumNonAdjacentSum(nums):
    # similar to dp[i - 2], dp[i - 1]
    n1, n2 = 0, 0
    for n in nums:
        n1, n2 = n2, max(n1 + n, n2)
    return n2
