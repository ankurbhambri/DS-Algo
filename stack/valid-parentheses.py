# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:

        hm = {")": "(", "}": "{", "]": "["}
        st = []

        for ch in s:
            if st and (ch in hm and st[-1] == hm[ch]):
                st.pop()
                continue

            st.append(ch)

        return len(st) == 0

print(Solution().isValid("()")) # True
print(Solution().isValid("()[]{}")) # True