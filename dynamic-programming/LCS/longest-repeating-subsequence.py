# https://www.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1


# TC: O(m^2) - We fill a 2D DP table of size m x m.
# SC: O(m^2) - The DP table takes O(m^2) space
class Solution:
    def LongestRepeatingSubsequence(self, s1):

        s2 = s1

        m = len(s1)

        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):

            for j in range(1, m + 1):

                if s1[i - 1] == s2[j - 1] and i != j:
                    dp[i][j] = 1 + dp[i - 1][j - 1]

                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][m]


print(Solution().LongestRepeatingSubsequence("aab"))    # Output: 1 (The longest repeating subsequence is "a")
print(Solution().LongestRepeatingSubsequence("axxxy"))  # Output: 2 (The longest repeating subsequence is "xx")