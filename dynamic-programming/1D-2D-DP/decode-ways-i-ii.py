"""
    Similar questions:
        62. Unique Paths - https://leetcode.com/problems/unique-paths/
        70. Climbing Stairs - https://leetcode.com/problems/climbing-stairs/
        509. Fibonacci Number - https://leetcode.com/problems/fibonacci-number/
"""

# https://leetcode.com/problems/decode-ways/


# Recursive solution - TLE

# TC: O(2^n) time complexity, O(n) space complexity
def numDecodings(s):
    def helper(i, s):

        if i == len(s):
            return 1

        if s[i] == '0':
            return 0

        # take 1 digit
        ways = helper(i + 1, s)

        # take 2 digits
        if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
            ways += helper(i + 2, s)

        return ways

    return helper(0, s)


# Memoization recursive solution
# TC: O(n) time complexity, O(n) space complexity
def numDecodings(s):

    memo = {}

    def helper(i, s):

        if i in memo:
            return memo[i]

        if i == len(s):
            return 1

        if s[i] == '0':
            return 0

        # take 1 digit
        ways = helper(i + 1, s)

        # take 2 digits
        if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
            ways += helper(i + 2, s)

        memo[i] = ways
        return ways

    return helper(0, s)


# iterative solution
# TC: O(n) time complexity, O(n) space complexity
def numDecodings(s):

    if not s:
        return 0

    n = len(s)

    dp = [0] * (n + 1)

    # base case initialization
    dp[0] = 1
    dp[1] = 0 if s[0] == "0" else 1  # (1)

    for i in range(2, n + 1):

        # One step jump
        if 0 < int(s[i - 1 : i]) <= 9:  # (2)
            dp[i] += dp[i - 1]

        # Two step jump
        if 10 <= int(s[i - 2 : i]) <= 26:  # (3)
            dp[i] += dp[i - 2]

    return dp[n]


print(numDecodings("12"))  # 2
print(numDecodings("226"))  # 3
print(numDecodings("0"))  # 0
print(numDecodings("06"))  # 0




# https://leetcode.com/problems/decode-ways-ii/

# TC: O(n) time complexity, O(n) space complexity
def numDecodings(s):

    memo = {}
    MOD = 10**9 + 7

    def helper(i):

        if i == len(s):
            return 1

        if i in memo:
            return memo[i]

        ways = 0

        # -------- single char --------
        if s[i] == '*':
            ways += 9 * helper(i+1)

        elif s[i] != '0':
            ways += helper(i+1)

        # -------- two char --------
        if i + 1 < len(s):

            if s[i] == '*' and s[i+1] == '*':
                ways += 15 * helper(i+2)

            elif s[i] == '*':

                if '0' <= s[i+1] <= '6':
                    ways += 2 * helper(i+2)

                else:
                    ways += helper(i+2)

            elif s[i+1] == '*':

                if s[i] == '1':
                    ways += 9 * helper(i+2)

                elif s[i] == '2':
                    ways += 6 * helper(i+2)

            else:

                if 10 <= int(s[i:i+2]) <= 26:
                    ways += helper(i+2)

        memo[i] = ways % MOD
        return memo[i]

    return helper(0)


# Iterative solution
# TC: O(n) time complexity, O(n) space complexity
def numDecodings(s):

    MOD = 10**9 + 7

    n = len(s)
    dp = [0] * (n + 1)
    
    dp[n] = 1  # base case

    for i in range(n - 1, -1, -1):

        # ---------- single ----------
        if s[i] == '*':
            dp[i] = 9 * dp[i+1]
        elif s[i] != '0':
            dp[i] = dp[i+1]
        else:
            dp[i] = 0

        # ---------- double ----------
        if i + 1 < n:
            if s[i] == '*' and s[i+1] == '*':
                dp[i] += 15 * dp[i+2]

            elif s[i] == '*':
                if '0' <= s[i+1] <= '6':
                    dp[i] += 2 * dp[i+2]
                else:
                    dp[i] += dp[i+2]

            elif s[i+1] == '*':
                if s[i] == '1':
                    dp[i] += 9 * dp[i+2]
                elif s[i] == '2':
                    dp[i] += 6 * dp[i+2]

            else:
                if 10 <= int(s[i:i+2]) <= 26:
                    dp[i] += dp[i+2]

        dp[i] %= MOD

    return dp[0]