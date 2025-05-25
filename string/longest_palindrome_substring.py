# https://leetcode.com/problems/longest-palindromic-substring/description/

# Given a string s, return the longest palindromic substring in s.

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



# https://leetcode.com/problems/palindromic-substrings/description/

'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
'''

def countSubstrings(s):
    res = 0

    def compare(l, r):

        cnt = 0

        while l >= 0 and r < len(s) and s[l] == s[r]:

            cnt += 1
            l -= 1
            r += 1

        return cnt

    for i in range(len(s)):

        res += compare(i, i)

        res += compare(i, i + 1)

    return res


print(countSubstrings("abc"))
print(countSubstrings("aaa"))
