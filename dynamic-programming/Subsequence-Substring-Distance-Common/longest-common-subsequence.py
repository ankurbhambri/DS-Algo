# https://leetcode.com/problems/longest-common-subsequence/

'''

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

'''


# top down approach
def lcs_recursive_memo(X, Y):
    memo = {}

    def helper(m, n):
        if m == 0 or n == 0:
            return 0
        elif (m, n) in memo:
            return memo[(m, n)]
        else:
            if X[m - 1] == Y[n - 1]:
                c = 1 + helper(m - 1, n - 1)
            else:
                c = max(helper(m - 1, n), helper(m, n - 1))
            memo[(m, n)] = c
            return c

    return helper(len(X), len(Y))


# Bottom up approach
def lcs_tabular(str1, str2):

    m = len(str1)
    n = len(str2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if str1[i - 1] == str2[j - 1]:

                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:

                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


print(lcs_recursive_memo("ABCBDAB", "BDCABA"))
print(lcs_tabular("ABCBDAB", "BDCABA"))


# Printing the longest common subsequence
# Time = O(m × n) and Space = O(m × n) for this version

def printlongestCommonSubsequence(str1, str2):

    m = len(str1)
    n = len(str2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    res = []
    i, j = m, n

    while i > 0 and j > 0:

        if str1[i - 1] == str2[j - 1]:
            res.append(str1[i - 1])
            i -= 1
            j -= 1

        else:
            if dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    return "".join(res[::-1])


print(printlongestCommonSubsequence("ABCBDAB", "BDCABA")) # BCBA

# Similar problem - https://leetcode.com/problems/shortest-common-supersequence/

# Shortest Common Supersequence
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        ans = ""
        m = len(str1)
        n = len(str2)

        # initialising DP
        dp = [[0] * (n + 1) for i in range(m + 1)]

        # filling DP table by finding LCS
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]

                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Printing Shortest Common Supersequence
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                ans = str1[i - 1] + ans
                i -= 1
                j -= 1
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    ans = str1[i - 1] + ans
                    i -= 1
                else:
                    ans = str2[j - 1] + ans
                    j -= 1

        # if length of both string is different
        while i > 0:
            ans = str1[i - 1] + ans
            i -= 1

        while j > 0:
            ans = str2[j - 1] + ans
            j -= 1

        return ans

print(Solution().shortestCommonSupersequence("abc", "def"))  # Output: "abcdef"
print(Solution().shortestCommonSupersequence("AGGTAB", "GXTXAYB"))  # Output: "AGGXTXAYB"