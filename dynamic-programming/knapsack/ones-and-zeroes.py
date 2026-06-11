# https://leetcode.com/problems/ones-and-zeroes/


# TC: O(m * n * L) where m is the number of strings, n and m are the limits for zeros and ones, 
# and L is the average length of the strings (for counting zeros and ones).

# SC: O(m*n) for the DP table.
class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:

            z = s.count('0')

            o = len(s) - z

            for i in range(m, z - 1, -1):

                for j in range(n, o - 1 , -1):

                    dp[i][j] = max(dp[i][j], 1 + dp[i - z][j - o])

        return dp[m][n]


print(Solution().findMaxForm(strs=["10", "0", "1"], m=1, n=1))  # 2
print(Solution().findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3))  # 4