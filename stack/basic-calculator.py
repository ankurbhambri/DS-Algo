# https://leetcode.com/problems/basic-calculator-ii/


def solution(s):

    st = []
    curr = 0
    ope = "+"

    for i in range(len(s)):

        if s[i].isdigit():
            curr = curr * 10 + int(s[i])

        if s[i] in "+-*/" or i == len(s) - 1:

            # these operaitions will be performed on the last number in the stack.
            if ope == "-":
                st.append(-curr)

            elif ope == "*":
                st.append(st.pop() * curr)

            elif ope == "/":
                st.append(int(st.pop() / curr))

            else:
                st.append(curr)

            curr = 0 # reset current number, bcoz just processed it.
            ope = s[i]

    return sum(st)


print(solution("3+2*2"))  # 7
print(solution("0-213456789"))  # -213456789
print(solution("3/2"))  # 1
print(solution("3+5/2"))  # 5
print(solution("3+5/2*2"))  # 8
print(solution("3+5/2*2-1"))  # 7


# https://leetcode.com/problems/basic-calculator/description/

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0   # current result
        number = 0   # current number being formed
        sign = 1     # +1 for positive, -1 for negative

        for ch in s:
            if ch.isdigit():
                # Build the number (could be more than 1 digit)
                number = number * 10 + int(ch)

            elif ch in '+-':
                # Add the previous number with its sign to result
                result += sign * number
                number = 0  # reset number

                # Update sign for next number
                sign = 1 if ch == '+' else -1

            elif ch == '(':
                # Push current result and sign to stack
                stack.append(result)
                stack.append(sign)

                # Reset for new bracket scope
                result = 0
                sign = 1

            elif ch == ')':
                # Add last number before closing parenthesis
                result += sign * number
                number = 0

                # Pop sign and result from stack and apply
                prev_sign = stack.pop()
                prev_result = stack.pop()

                result = prev_result + prev_sign * result

        # Add any number left at the end
        result += sign * number
        return result

print(Solution().calculate("1 + 1"))  # Output: 2
print(Solution().calculate(" 2-1 + 2 "))  # Output: 3
print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))  # Output: 23
print(Solution().calculate("2-(5-6)"))  # Output: 3
