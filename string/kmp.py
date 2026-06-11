class Solution:
    def pieTable(self, pattern: str) -> list[int]:

        j = 0
        m = len(pattern)
        lps = [0] * m

        for i in range(1, m):

            # yha pe hum pattern ke prefix aur suffix ko compare kar rahe hai, agar match nahi karta to hum lps array ke last value pe jate hai, 
            # aur waha se fir se compare karte hai, jab tak match nahi milta ya j 0 nahi ho jata.
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]

            # yha pe hum pattern ke current character ko prefix ke next character se compare kar rahe hai, 
            # agar match karta hai to hum j ko increment kar dete hai, aur lps[i] me j ki value store kar dete hai.
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


print(Solution().kmpSearch("abababd", "ababd"))   # Output: 2
print(Solution().kmpSearch("aaacaaaa", "aaacaaa"))   # Output: 1