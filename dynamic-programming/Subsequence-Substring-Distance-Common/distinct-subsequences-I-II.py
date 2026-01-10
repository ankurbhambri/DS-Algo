# https://leetcode.com/problems/distinct-subsequences/


class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                dp[i][j] = dp[i - 1][j]

                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[m][n]


print(Solution().numDistinct("babgbag", "bag"))     # Output: 5
print(Solution().numDistinct("rabbbit", "rabbit"))  # Output: 3

# https://leetcode.com/problems/distinct-subsequences-ii/

