# One way is to leverage LCS and pass the string and its reverse to the LCS function. The length of the LCS will be the length of the longest palindromic subsequence.


def longestPalindromeSubseq(s):

    def longestCommonSubsequence(X, Y):
        M = len(X)
        N = len(Y)
        memo = {}

        def helper(m, n):
            if m == 0 or n == 0:
                return 0
            elif (m, n) in memo:
                return memo[(m, n)]
            else:
                if X[m - 1] == Y[n - 1]:
                    # accepting value
                    c = 1 + helper(m - 1, n - 1)
                else:
                    # if not equal lets go ahead
                    c = max(helper(m - 1, n), helper(m, n - 1))

                memo[(m, n)] = c
                return c

        return helper(M, N)

    return longestCommonSubsequence(s, s[::-1])


# TC - O(N^2) - N is the length of the string
print(longestPalindromeSubseq("bbabcbcab"))


# Another way is to use the LCS tabular approach to solve this problem.


def longestPalinSubseqTabular(S):
    # similar to lcs code only string reverse added
    P = S[::-1]
    m = len(S)

    dp = [[0] * (m + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, m + 1):
            if S[i - 1] == P[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][m]


# Time complexity - O(
print(longestPalinSubseqTabular("bbabcbcab"))
