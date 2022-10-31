def longestCommonSubstr(s1, s2, n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    res = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                res = max(res, dp[i][j])
    return res

print(longestCommonSubstr("ABC", "ACB", 3, 3))
print(longestCommonSubstr("ABCDGH", "ACDGHR", 6, 6))
