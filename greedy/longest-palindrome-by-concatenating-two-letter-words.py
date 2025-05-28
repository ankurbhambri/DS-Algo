# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words

'''
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.
'''

from collections import Counter


class Solution:
    def longestPalindrome(self, words):
        count = Counter(words)
        total_length = 0
        used_center = False

        for word in list(count.keys()):
            rev = word[::-1]

            if word == rev:
                # It's a self-palindrome like "gg", "cc"
                pairs = count[word] // 2
                total_length += pairs * 4
                count[word] -= pairs * 2
                if not used_center and count[word] > 0:
                    # Use one in the center
                    total_length += 2
                    used_center = True
            else:
                if rev in count:
                    pairs = min(count[word], count[rev])
                    total_length += pairs * 4
                    count[word] -= pairs
                    count[rev] -= pairs

        return total_length


print(Solution().longestPalindrome(["lc", "cl", "gg"]))
print(Solution().longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"]))
print(Solution().longestPalindrome(["cc", "ll", "xx"]))
print(Solution().longestPalindrome(["aba"]))
print(Solution().longestPalindrome(["aa", "aa"]))
