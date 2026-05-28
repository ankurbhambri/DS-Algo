# https://leetcode.com/problems/distinct-subsequences/

# memo + recursion
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        m, n = len(s), len(t)

        memo = {}

        def dfs(i, j):

            # target formed
            if j == n:
                return 1

            # source exhausted
            if i == m:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            ans = 0

            # take + skip
            if s[i] == t[j]:
                ans += dfs(i + 1, j + 1)

            # skip current char from s
            ans += dfs(i + 1, j)

            memo[(i, j)] = ans

            return ans

        return dfs(0, 0)


# 2D DP
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                # skip the character in s
                dp[i][j] = dp[i - 1][j]

                if s[i - 1] == t[j - 1]:
                    # take the character in s
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[m][n]


# space optimised 1D DP
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        m, n = len(s), len(t)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, m + 1):
            for j in range(n, 0, -1):

                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]


print(Solution().numDistinct("babgbag", "bag"))     # Output: 5
print(Solution().numDistinct("rabbbit", "rabbit"))  # Output: 3


# TODO
# https://leetcode.com/problems/distinct-subsequences-ii/

