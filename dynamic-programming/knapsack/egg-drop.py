# https://leetcode.com/problems/super-egg-drop/description/

"""

Here,

- dp[i - 1][j - 1] means that the egg breaks, so we have one less egg and one less move to check the floors below.
- dp[i - 1][j] means that the egg doesn't break, so we have the same number of eggs and one less move to check the floors above.

The loop continues until we find the minimum number of moves (i) such that dp[i][j] is greater than or equal to N, which means we can check all N floors with j eggs and i moves.

"""


def superEggDrop(K, N):
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, K + 1):
            dp[i][j] = 1 + dp[i - 1][j - 1] + dp[i - 1][j]
        if dp[i][j] >= N:
            return i


k = 3
n = 14
print(superEggDrop(k, n))
