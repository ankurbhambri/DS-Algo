# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(i.lower() for i in s if i.isalnum())
        
        def helper(s):
            l, r = 0, len(s) - 1
            while l <= r:
                
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
                
            return True

        return helper(s)


print(Solution().isPalindrome("abca"))
print(Solution().isPalindrome("aba"))
print(Solution().isPalindrome("abc"))


# or

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(i.lower() for i in s if i.isalnum())
        
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - i - 1]:
                return False
        return True

print(Solution().isPalindrome("abca"))
print(Solution().isPalindrome("aba"))
print(Solution().isPalindrome("abc"))


# Variant :What if you could only consider a limited set of characters as a part of a potential palindrome?

'''

A phrase is a palindrome if, after excluding any characters outside of a given vector of characters include, it reads the same forward and backward.
Given a string (s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "racecarX", include = [r,X]
Output: false
Explanation: "rrX" is not a palindrome.

Example 2:
Input: s = "Yo, banana boY!", include =
[Y, o, b, a, n]
Output: true
Explanation: "YobananaboY" is a palindrome.

'''

class Solution:
    def isPalindrome(self, s: str, include: list) -> bool:

        s = ''.join(i.lower() for i in s if i.isalnum() and i.lower() in set(include))

        n = len(s)

        for i in range(n // 2):
            if s[i] != s[n - i - 1]:
                return False

        return True

print(Solution().isPalindrome("racecarX", ['r','X'])) # False
print(Solution().isPalindrome("Yo, banana boY!", ['Y', 'o', 'b', 'a', 'n'])) # True
print(Solution().isPalindrome("a b c d e d c b a", ['a', 'b', 'c', 'd', 'e'])) # False