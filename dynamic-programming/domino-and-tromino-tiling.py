# https://leetcode.com/problems/domino-and-tromino-tiling/

class Solution:
    def numTilings(self, n: int) -> int:

        dp = [0] * (1001)

        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5

        mod = 1e9 + 7

        if n <= 3:
            return dp[n]

        for i in range(4, n + 1):
            dp[i] = 2 * dp[i - 1] + dp[i - 3]
            dp[i] %= mod

        return int(dp[n])

print(Solution().numTilings(3))  # 5
print(Solution().numTilings(4))  # 11
print(Solution().numTilings(5))  # 24