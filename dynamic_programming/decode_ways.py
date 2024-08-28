"""
    Similar questions:
        62. Unique Paths - https://leetcode.com/problems/unique-paths/
        70. Climbing Stairs - https://leetcode.com/problems/climbing-stairs/
        509. Fibonacci Number - https://leetcode.com/problems/fibonacci-number/
"""

# https://leetcode.com/problems/decode-ways/


def numDecodings(s):
    dp = {len(s): 1}
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "0":
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]

        if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] < "7"):
            dp[i] += dp[i + 2]

    return dp[0]


print(numDecodings("12"))  # 2
print(numDecodings("226"))  # 3
print(numDecodings("0"))  # 0
print(numDecodings("06"))  # 0
