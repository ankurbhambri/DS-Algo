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
