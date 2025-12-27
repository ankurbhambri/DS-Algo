# https://leetcode.com/problems/substring-matching-pattern/

# TC: O(n * m) where n is the length of s and m is the length of p
# SC: O(1)

class Solution:
    def hasMatch(self, s: str, p: str) -> bool:

        idx = -1
        a, b = p.split("*")

        for i in range(len(s) - len(a) + 1):
            w = s[i: i + len(a)]
            if w == a:
                idx = i + len(a)
                break
        
        if idx == -1:
            return False

        if b == "":
            return True

        for j in range(idx, len(s) - len(b) + 1):
            w = s[j : j + len(b)]
            if w == b:
                return True
        
        return False

print(Solution().hasMatch("abdefg", "a*g"))  # Output: True
print(Solution().hasMatch("xyz", "x*z"))      # Output: True
print(Solution().hasMatch("hello", "h*v"))    # Output: False
print(Solution().hasMatch("abcdef", "a*d"))   # Output: True


# Using KMP for improved efficiency

class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        a, b = p.split("*")

        def kmp_search(text: str, pattern: str, start: int = 0) -> int:

            if not pattern:
                return start

            # Build LPS array
            lps = [0] * len(pattern)
            j = 0
            for i in range(1, len(pattern)):
                while j > 0 and pattern[i] != pattern[j]:
                    j = lps[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                    lps[i] = j

            # KMP search
            j = 0
            for i in range(start, len(text)):
                while j > 0 and text[i] != pattern[j]:
                    j = lps[j - 1]
                if text[i] == pattern[j]:
                    j += 1
                if j == len(pattern):
                    return i - len(pattern) + 1

            return -1

        # Find a
        i = kmp_search(s, a)
        if i == -1:
            return False

        # If b is empty, match is valid
        if not b:
            return True

        # Find b after a ends
        j = kmp_search(s, b, i + len(a))
        return j != -1
