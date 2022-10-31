def shortestCommonSupersequence(str1, str2, m, n):

    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # till this lcs solution
    val = dp[m][n] 

    # just subracted matching sequence from both string
    a = len(str1) - val 
    b = len(str2) - val
    
    # atlast added matching sequence in both string 
    return a + b + val

print(shortestCommonSupersequence("abcd", "xycd", 4, 4))
