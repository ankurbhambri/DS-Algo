# Leetcode 1249


# TC: O(N)
# SC: O(N)


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        chars = list(s)
        balance = 0

        # remove invalid ')'
        for i in range(len(chars)):
            if chars[i] == '(':
                balance += 1
            elif chars[i] == ')':
                if balance == 0:
                    chars[i] = ''
                else:
                    balance -= 1

        # remove extra '(' from right
        for i in range(len(chars) - 1, -1, -1):
            if balance > 0 and chars[i] == '(':
                chars[i] = ''
                balance -= 1

        return ''.join(chars)


# Variant

'''
Given a string that consists of various types of parentheses and alphanumeric characters,
delete the least number of parentheses (any of them) to make the string balanced and return any result.

A balanced string is defined as a string where every type of opening parentheses has a matching closing parentheses.

For example, for "()())[]" return either "(())[]"  or "() () []"

'''

class Solution:
    def minRemoveToMakeValidVariousParentheses(self, s: str) -> str:

        stack = []
        remove = set()
        mapping = {')': '(', '}': '{', ']': '['}

        for i, ch in enumerate(s):

            if ch in mapping.values():  # opening
                stack.append((ch, i))

            elif ch in mapping:  # closing

                if stack and stack[-1][0] == mapping[ch]:
                    stack.pop()

                else:
                    remove.add(i)

        # leftover opening parentheses
        for _, idx in stack:
            remove.add(idx)

        return ''.join(ch for i, ch in enumerate(s) if i not in remove)
    

print(Solution.minRemoveToMakeValidVariousParentheses(Solution, "((a{bc]d)e}f)g)"))
print(Solution.minRemoveToMakeValidVariousParentheses(Solution, "a)b(c)d[e{f}g]h)i}j{k]l"))
