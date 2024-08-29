"""
    Similar questions:
        62. Unique Paths - https://leetcode.com/problems/unique-paths/
        70. Climbing Stairs - https://leetcode.com/problems/climbing-stairs/
        509. Fibonacci Number - https://leetcode.com/problems/fibonacci-number/
"""

# https://leetcode.com/problems/decode-ways/


def numDecodings(s):

    if not s:
        return 0

    dp = [0 for x in range(len(s) + 1)]

    # base case initialization
    dp[0] = 1
    dp[1] = 0 if s[0] == "0" else 1  # (1)

    for i in range(2, len(s) + 1):
        # One step jump
        if 0 < int(s[i - 1 : i]) <= 9:  # (2)
            dp[i] += dp[i - 1]
        # Two step jump
        if 10 <= int(s[i - 2 : i]) <= 26:  # (3)
            dp[i] += dp[i - 2]
    return dp[len(s)]


print(numDecodings("12"))  # 2
print(numDecodings("226"))  # 3
print(numDecodings("0"))  # 0
print(numDecodings("06"))  # 0
