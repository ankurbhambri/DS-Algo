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
        odd = helper(i, i)
        res = odd if len(odd) > len(res) else res

        # even string
        even = helper(i, i + 1)
        res = even if len(even) > len(res) else res

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
                    # A string is a palindrome if the first and last characters are the same and the remaining string is also a palindrome
                    # Lekin problem tab aati hai jab substring bahut chhoti ho. Agar substring length ≤ 3 ho toh middle part check karne ki zarurat nahi hoti.
                    if s[j] == s[i] and (i - j <= 2 or dp[j + 1][i - 1]):

                        dp[j][i] = True

                        if i - j + 1 > max_len:
                            max_len = i - j + 1
                            res = s[j:i + 1]

        return res

print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("racecar"))


# Manacher's Algorithm (doubt)

class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) <= 1:
            return s
        
        Max_Len = 1
        Max_Str = s[0]

        right = 0
        center = 0

        s = '#' + '#'.join(s) + '#'
        dp = [0 for _ in range(len(s))]

        for i in range(len(s)):

            if i < right:
                dp[i] = min(right - i, dp[2 * center - i])

            while i - dp[i] - 1 >= 0 and i + dp[i] + 1 < len(s) and s[i - dp[i ]- 1] == s[i + dp[i] + 1]:
                dp[i] += 1

            if i + dp[i] > right:
                center = i
                right = i + dp[i]

            if dp[i] > Max_Len:
                Max_Len = dp[i]
                Max_Str = s[i - dp[i]:i + dp[i] + 1].replace('#','')

        return Max_Str