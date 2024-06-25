# https://leetcode.com/problems/unique-binary-search-trees/


# Idea behind the solution is to use dynamic programming.
# Using DP we are calculating the number of unique binary search trees that can be formed with n nodes.


def numTrees(n):

    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1

    for i in range(2, n + 1):
        for j in range(1, i + 1):

            dp[i] += dp[j - 1] * dp[i - j]

    return dp[n]


print(numTrees(3))
print(numTrees(1))
