# https://leetcode.com/problems/distinct-subsequences/

# memo + recursion

# TC: O(m*n)
# SC: O(m*n) for memo + O(m) for recursion stack
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        memo = {}

        m, n = len(s), len(t)

        def dfs(i, j):

            # target formed
            if j == n:
                return 1

            # source exhausted
            if i == m:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            ans = dfs(i + 1, j)

            # take + skip
            if s[i] == t[j]:
                ans += dfs(i + 1, j + 1)

            memo[(i, j)] = ans

            return ans

        return dfs(0, 0)


# 2D DP
# TC: O(m*n)
# SC: O(m*n)
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
# TC: O(m*n)
# SC: O(n)
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


# https://leetcode.com/problems/distinct-subsequences-ii/


# TC: O(n ^ 2)
# SC: O(n)
class Solution:
    def distinctSubseqII(self, s: str) -> int:

        res = 0

        n = len(s)

        dp = [1] * (n)

        mod = 10 ** 9 + 7

        for i in range(n):
            for j in range(i):

                if s[i] != s[j]:

                    dp[i] = (dp[i] + dp[j]) % mod

            res += dp[i]

        return res % mod


print(Solution().distinctSubseqII("abc"))  # Output: 7
print(Solution().distinctSubseqII("aba"))  # Output: 6


# TC: O(n)
# SC: O(n)
class Solution:
    def distinctSubseqII(self, s: str) -> int:

        last = {}
        total = 1   # empty subsequence

        MOD = 10**9 + 7

        for ch in s:

            new_total = (total * 2 - last.get(ch, 0)) % MOD

            last[ch] = total

            total = new_total

        return (total - 1) % MOD


print(Solution().distinctSubseqII("abc"))  # Output: 7
print(Solution().distinctSubseqII("aba"))  # Output: 6