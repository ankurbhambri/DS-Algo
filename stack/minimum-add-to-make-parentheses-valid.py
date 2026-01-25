# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

# Tc: O(n)
# Sc: O(1)
class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        open_brackets = 0
        min_adds_required = 0

        for c in s:
            if c == "(":
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    min_adds_required += 1

        return min_adds_required + open_brackets


print(Solution().minAddToMakeValid("()"))  # Output: 0
print(Solution().minAddToMakeValid("())"))  # Output: 1
print(Solution().minAddToMakeValid("((("))  # Output: 3
print(Solution().minAddToMakeValid("()))(("))  # Output: 4


# Variant: Return the string after adding the minimum number of parentheses to make it valid. There can be multiple valid answers. You can return any of them.

class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        res = ""
        open_brackets = 0

        for c in s:

            if c == "(":
                open_brackets += 1

            else:

                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    res += "()"
                    continue

            res += c

        res += ")" * open_brackets

        return res

print(Solution().minAddToMakeValid("()"))  # Output: "()"
print(Solution().minAddToMakeValid("())"))  # Output: "(())"
print(Solution().minAddToMakeValid("((("))  # Output: "((()))"
print(Solution().minAddToMakeValid("()))(("))  # Output: "()()()()"