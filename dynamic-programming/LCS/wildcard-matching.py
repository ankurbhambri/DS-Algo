# https://leetcode.com/problems/wildcard-matching/


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Base case: Empty string and empty pattern match
        dp[0][0] = True

        # Base case: Handle '*' at the beginning of pattern
        # Pattern like "***" can match an empty string
        for j in range(1, n + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]
            else:
                break

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if p[j-1] == s[i-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]

                elif p[j-1] == '*':
                    # dp[i][j-1] means '*' matches nothing
                    # dp[i-1][j] means '*' matches one or more chars
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]

        return dp[m][n]


print(Solution().isMatch("adceb", "*a*b"))  # True
print(Solution().isMatch("acdcb", "a*c?b"))  # False