# https://leetcode.com/problems/expression-add-operators/description/

# Question:
# Given a string num that contains only digits and an integer target, 
# return all possibilities to add binary operators (not unary) +, -, or * between the digits of num 
# so that the resultant expression evaluates to target.

# TC: O(3^n × n)
# SC: O(n) (stack) + O(3^n * n) (output)

class Solution:
    def addOperators(self, num: str, target: int):
        res = []

        def backtrack(index, expr, prev, curr):
            if index == len(num):
                if curr == target:
                    res.append(expr)
                return

            for i in range(index, len(num)):
                if i != index and num[index] == '0':
                    break  # no leading zeros

                val = int(num[index:i + 1])
                if index == 0:
                    backtrack(i + 1, str(val), val, val)
                else:
                    backtrack(i + 1, expr + '+' + str(val), val, curr + val)
                    backtrack(i + 1, expr + '-' + str(val), -val, curr - val)
                    backtrack(i + 1, expr + '*' + str(val), prev * val, curr - prev + (prev * val))

        backtrack(0, "", 0, 0)
        return res


print(Solution().addOperators("123", 6))  # ["1+2+3", "1*2*3"]
print(Solution().addOperators("232", 8))  # ["2*3+2", "2+3*2"]
print(Solution().addOperators("105", 5))  # ["1*0+5","1+0*5"]
print(Solution().addOperators("00", 0))  # ["0+0", "0-0", "0*0"]
