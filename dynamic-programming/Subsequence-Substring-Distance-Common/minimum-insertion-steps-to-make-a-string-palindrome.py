# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/

class Solution:
    def minInsertions(self, s: str) -> int:

        n = len(s)
        s_rev = s[::-1]
        
        # Standard LCS DP table
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i-1] == s_rev[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        lps_length = dp[n][n]
        return n - lps_length

print(Solution().minInsertions("g"))  # 0
print(Solution().minInsertions("zzazz"))  # 0
print(Solution().minInsertions("mbadm"))  # 2
print(Solution().minInsertions("leetcode"))  # 5