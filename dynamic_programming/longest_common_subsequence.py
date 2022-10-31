# A subsequence is not continuous we can skip some strings but in Substring, we can't do that.

# https://leetcode.com/problems/longest-common-subsequence/

# top down approach
def lcs_recursive_memo(M, N, X, Y):
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
    return helper(M, N)

# bottom up approach
def lcs_tabular(m, n, str1, str2):

    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]



def printlongestCommonSubsequence(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    i, j = m, n
    res = []
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




print(lcs_recursive_memo(3, 2, 'ABC', 'AC'))
print(lcs_tabular(3, 2, 'ABC', 'AC'))
print(printlongestCommonSubsequence('ABC', 'AC'))
