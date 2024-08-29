# Longest common substring is like matching longest common suffix of two strings such as abcdef,
# xyzdef (def) suffix is matching in both and can be called as LC-Substring.


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


# Similar question - Maximum Length of Repeated Subarray
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/


def findLength(a, b):

    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    res = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                res = max(res, dp[i][j])
    return res


print(findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))  # 3
print(findLength([0, 1, 1, 1, 1], [1, 0, 1, 0, 1]))  # 2
print(findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))  # 3
