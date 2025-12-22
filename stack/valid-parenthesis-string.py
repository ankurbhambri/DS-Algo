# https://leetcode.com/problems/valid-parenthesis-string/description/

class Solution:
    def checkValidString(self, s: str) -> bool:

        # store the indices of '('
        stk = []

        # store the indices of '*'
        star = []

        for idx, char in enumerate(s):

            if char == '(':
                stk.append( idx )

            elif char == ')':

                if stk:
                    stk.pop()

                elif star:
                    star.pop()

                else:
                    return False

            else:
                star.append( idx )

        # cancel ( and * with valid positions, i.e., '(' must be on the left hand side of '*'
        while stk and star:

            if stk[-1] > star[-1]:
                return False

            stk.pop()
            star.pop()

        # Accept when stack is empty, which means all braces are paired
        # Reject, otherwise.
        return len(stk) == 0


# Variant 

# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

class Solution:
    def canBeValid(self, s, locked):
        length = len(s)

        # If length of string is odd, return false.
        if length % 2 == 1:
            return False

        open_brackets = []
        unlocked = []

        # Iterate through the string to handle '(' and ')'
        for i in range(length):
            if locked[i] == "0":
                unlocked.append(i)
            elif s[i] == "(":
                open_brackets.append(i)
            elif s[i] == ")":
                if open_brackets:
                    open_brackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        # Match remaining open brackets and the unlocked characters
        while open_brackets and unlocked:

            # open brackets '(' must be on the left hand side of 'unlocked brackets'
            if open_brackets[-1] > unlocked[-1]:
                return False

            open_brackets.pop()
            unlocked.pop()

        return len(open_brackets) == 0


print(Solution().canBeValid("()()", "0000"))
print(Solution().canBeValid("))()))", "010100"))