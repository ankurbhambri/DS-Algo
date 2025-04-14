# https://leetcode.com/problems/counting-bits/

# Idea here is to use dynamic programming to solve this problem.

# We can use the formula: dp[i] = dp[i // 2] + 1 if i is odd else dp[i // 2]

# Even number active bit is equal to half of the number of active bits of the number divided by 2.
# Odd number active bit is equal to the number of active bits of the number divided by 2 plus 1.


def countBits(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i % 2 != 0:
            dp[i] = dp[i // 2] + 1
        else:
            dp[i] = dp[i // 2]
    return dp


print(countBits(2))  # [0, 1, 1]
print(countBits(5))  # [0, 1, 1, 2, 1, 2]
print(countBits(6))  # [0, 1, 1, 2, 1, 2, 2]
print(countBits(7))  # [0, 1, 1, 2, 1, 2, 2, 3]
print(countBits(8))  # [0, 1, 1, 2, 1, 2, 2, 3, 1]
