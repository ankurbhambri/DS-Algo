# https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:

        def validPalindromeUtil(s, l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            
            return True

        i, j = 0, len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return validPalindromeUtil(s, i + 1, j) or validPalindromeUtil(s, i, j - 1)

        return True

print(Solution().validPalindrome("abca")) # True
print(Solution().validPalindrome("aba")) # True
print(Solution().validPalindrome("abc")) # False