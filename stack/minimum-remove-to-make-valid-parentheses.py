# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        balance = 0
        chars = list(s)

        # remove invalid ')'
        for i in range(len(chars)):

            if chars[i] == '(':
                balance += 1

            elif chars[i] == ')':

                if balance > 0:
                    balance -= 1
                else:
                    chars[i] = ''

        # remove extra '(' from right
        for i in range(len(chars) - 1, -1, -1):
            if balance > 0 and chars[i] == '(':
                chars[i] = ''
                balance -= 1

        return ''.join(chars)

print(Solution().minRemoveToMakeValid("))(()))"))  # Output: "(())"
print(Solution().minRemoveToMakeValid("()))(()("))  # Output: "()()"