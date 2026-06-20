"""
    Similar questions:
        62. Unique Paths - https://leetcode.com/problems/unique-paths/
        70. Climbing Stairs - https://leetcode.com/problems/climbing-stairs/
        509. Fibonacci Number - https://leetcode.com/problems/fibonacci-number/
"""

# https://leetcode.com/problems/decode-ways/


# TC: O(n) time complexity, O(n) space complexity
class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {}

        def helper(i, s):

            if i == len(s):
                return 1

            if i in memo:
                return memo[i]

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


# TC: O(n) time complexity, O(1) space complexity
class Solution:
    def numDecodings(self, s: str) -> int:

        if not s or s[0] == '0':
            return 0

        # prev2 represents dp[i-2], prev1 represents dp[i-1]
        prev2 = 1
        prev1 = 1

        for i in range(1, len(s)):

            curr = 0

            # Check if single-digit decode is possible
            if s[i] != '0':
                curr += prev1

            # Check if two-digit decode is possible
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                curr += prev2

            # If both choices yield 0, the string cannot be decoded
            if curr == 0:
                return 0

            # Shift our lookback variables forward
            prev2 = prev1
            prev1 = curr

        return prev1


print(Solution().numDecodings("12"))  # Output: 2
print(Solution().numDecodings("226"))  # Output: 3

# https://leetcode.com/problems/decode-ways-ii/


# TC: O(n) time complexity, O(1) space complexity
class Solution:
    def numDecodings(self, s: str) -> int:

        MOD = 10**9 + 7

        if not s:
            return 0

        if s[0] == '0':
            return 0

        # prev2 represents dp[i - 2], prev1 represents dp[i - 1]

        prev2 = 1

        prev1 = 9 if s[0] == '*' else 1

        for i in range(1, len(s)):

            curr = 0

            # --- 1. Single-Digit Decode ---
            if s[i] == '*':
                curr += 9 * prev1

            elif s[i] != '0':
                curr += prev1

            # --- 2. Two-Digit Decode ---
            prev_char = s[i-1]
            curr_char = s[i]

            if prev_char == '*' and curr_char == '*':
                curr += 15 * prev2

            elif prev_char == '*':

                # Wildcard followed by a digit
                if curr_char <= '6': # curr less than 6
                    curr += 2 * prev2  # '*' can be '1' or '2'

                else: # curr greater than '6'
                    curr += 1 * prev2  # '*' can only be '1'

            elif curr_char == '*':

                # Digit followed by a wildcard
                if prev_char == '1':
                    curr += 9 * prev2  # 11 to 19

                elif prev_char == '2':
                    curr += 6 * prev2  # 21 to 26

            else:
                # Both are regular digits
                if 10 <= int(prev_char + curr_char) <= 26:
                    curr += prev2

            # Apply modulo to avoid large integer performance issues
            curr %= MOD

            # Shift states forward
            prev2 = prev1
            prev1 = curr

        return prev1


print(Solution().numDecodings("12"))  # Output: 2
print(Solution().numDecodings("**"))  # Output: 96