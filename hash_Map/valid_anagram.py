# https://leetcode.com/problems/valid-anagram/

from collections import Counter


def isAnagram(s, t):
    # We can use proper dictionary code as well idea is same
    return Counter(s) == Counter(t)


print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
print(isAnagram("a", "ab"))
print(isAnagram("ab", "ba"))
