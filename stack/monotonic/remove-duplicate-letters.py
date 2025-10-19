# https://leetcode.com/problems/remove-duplicate-letters/

from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        st = []
        visit = set() # visit to mark the already used characters
        cnt = Counter(s)

        for c in s:

            cnt[c] -= 1

            if c in visit:
                continue

            while st and st[-1] > c and cnt[st[-1]] > 0:
                val = st.pop()
                visit.remove(val)

            st.append(c)
            visit.add(c)

        return "".join(st)

print(Solution().removeDuplicateLetters("cbacdcbc"))  # "acdb"
print(Solution().removeDuplicateLetters("bcabc"))     # "abc"
print(Solution().removeDuplicateLetters("abacb"))     # "abc"
print(Solution().removeDuplicateLetters("bbcaac"))    # "bac"