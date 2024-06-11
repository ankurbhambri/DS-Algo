# https://leetcode.com/problems/valid-anagram/

from collections import Counter


def isAnagram(s, t):

    a = [0] * 26
    b = [0] * 26

    for i in s:
        a[ord(i) - ord("a")] += 1

    for j in t:
        b[ord(j) - ord("a")] += 1

    if a == b:
        return True

    return False


def isAnagram(s, t):
    # We can use proper dictionary code as well idea is same
    return Counter(s) == Counter(t)


print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
print(isAnagram("a", "ab"))
print(isAnagram("ab", "ba"))



