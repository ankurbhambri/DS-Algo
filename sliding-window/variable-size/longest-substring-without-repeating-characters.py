"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Note: r - l + 1 is used to get the window size
"""


def lengthOfLongestSubstring(s):

    l = 0
    res = 0
    charSet = set()

    for r in range(len(s)):

        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1

        charSet.add(s[r])
        res = max(res, r - l + 1)

    return res


# Same for array [] as well
# https://leetcode.com/problems/maximum-erasure-value/


print(lengthOfLongestSubstring("abcabcbb"))  # 3
print(lengthOfLongestSubstring("bbbbb"))  # 1
print(lengthOfLongestSubstring("pwwkew"))  # 3
print(lengthOfLongestSubstring(""))  # 0


def maximumUniqueSubarray(s):
    charSet = set()

    l = 0
    res = 0
    sm = 0

    for r in range(len(s)):

        sm += s[r]

        while s[r] in charSet:
            sm -= s[l]
            charSet.remove(s[l])
            l += 1

        charSet.add(s[r])
        res = max(res, sm)

    return res


print(maximumUniqueSubarray([4, 2, 4, 5, 6]))  # 17
print(maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]))  # 8
print(maximumUniqueSubarray([10000]))  # 10000
