# https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings

'''
You are given a string s and a positive integer k.

Select a set of non-overlapping substrings from the string s that satisfy the following conditions:

The length of each substring is at least k.
Each substring is a palindrome.
Return the maximum number of substrings in an optimal selection.

A substring is a contiguous sequence of characters within a string.

'''

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:

        n = len(s)
        dp = [0] * (n + 1)

        def is_palindrome(l: int, r: int) -> bool:

            while l < r:

                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1

            return True

        for i in range(k, n + 1):

            dp[i] = dp[i - 1]

            if is_palindrome(i - k, i - 1):
                dp[i] = max(dp[i], dp[i - k] + 1)

            if i - k - 1 >= 0 and is_palindrome(i - k - 1, i - 1):
                dp[i] = max(dp[i], dp[i - k - 1] + 1)

        return dp[n]


print(Solution().maxPalindromes("abaccdbbd", 3))
print(Solution().maxPalindromes("adbcda", 2))
print(Solution().maxPalindromes("bbabab", 2))
print(Solution().maxPalindromes("aa", 1))
