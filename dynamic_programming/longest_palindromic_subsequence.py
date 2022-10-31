def longestPalinSubseq(S):
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

print(longestPalinSubseq('bbabcbcab'))
