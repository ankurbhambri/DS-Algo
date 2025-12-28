class Solution:
    def pieTable(self, pattern: str) -> list[int]:

        m = len(pattern)
        lps = [0] * m
        j = 0

        for i in range(1, m):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j

        return lps
    
    def kmpSearch(self, text: str, pattern: str, start: int = 0) -> int:

        if not pattern:
            return start

        j = 0
        lps = self.pieTable(pattern)

        for i in range(start, len(text)):

            while j > 0 and text[i] != pattern[j]:
                j = lps[j - 1]

            if text[i] == pattern[j]:
                j += 1

            if j == len(pattern):
                return i - len(pattern) + 1

        return -1


print(Solution().kmpSearch("abdefg", "a"))  # Output: 0
print(Solution().kmpSearch("xyz", "z"))      # Output: 2
print(Solution().kmpSearch("hello", "ll"))    # Output: 2
print(Solution().kmpSearch("abcabcabcd", "abcd"))   # Output: 6