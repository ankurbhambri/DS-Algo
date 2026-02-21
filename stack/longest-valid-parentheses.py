# https://leetcode.com/problems/longest-valid-parentheses/description/


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]   # base index
        ans = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)   # reset base
                else:
                    ans = max(ans, i - stack[-1])

        return ans


print(Solution().longestValidParentheses("(()")) # 2
print(Solution().longestValidParentheses(")()())")) # 4