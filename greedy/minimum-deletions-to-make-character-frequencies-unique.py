# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        res = 0
        seen = set()
        c = Counter(s)
        for freq in c.values():
            while freq > 0 and freq in seen:
                freq -= 1
                res += 1
            seen.add(freq)
        return res

print(Solution().minDeletions("aabbcc"))  # Example usage
print(Solution().minDeletions("aaabbbcc"))  # Example usage