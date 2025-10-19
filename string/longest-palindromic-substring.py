# https://leetcode.com/problems/longest-palindromic-substring/description/

# Given a string s, return the longest palindromic substring in s.

# Similar to palindromic substrings problem - https://leetcode.com/problems/palindromic-substrings/description/


def longestPalindrome(s):

    def helper(l, r):

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return s[l + 1 : r]

    res = ""
    for i in range(len(s)):

        # odd string
        test = helper(i, i)
        res = test if len(test) > len(res) else res

        # even string
        test = helper(i, i + 1)
        res = test if len(test) > len(res) else res

    return res


print(longestPalindrome("babad"))
print(longestPalindrome("racecar"))


# DP Approach
class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) <= 1:
            return s

        max_len = 1
        res = s[0]

        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):

            dp[i][i] = True

            for j in range(i):

                if s[j] == s[i] and (i - j <= 2 or dp[j + 1][i - 1]):

                    dp[j][i] = True

                    if i - j + 1 > max_len:
                        max_len = i - j + 1
                        res = s[j:i + 1]

        return res

print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("racecar"))
