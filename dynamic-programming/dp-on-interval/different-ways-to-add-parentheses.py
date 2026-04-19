# https://leetcode.com/problems/different-ways-to-add-parentheses/description/

class Solution:
    def diffWaysToCompute(self, expression: str):
        res = []

        for i in range(len(expression)):

            if expression[i] in "*+-":

                left = self.diffWaysToCompute(expression[:i])

                right = self.diffWaysToCompute(expression[i + 1 :])

                for a in left:
                    for b in right:

                        if expression[i] == "+":
                            res.append(a + b)

                        elif expression[i] == "-":
                            res.append(a - b)

                        elif expression[i] == "*":
                            res.append(a * b)
        if not res:
            res.append(int(expression))

        return res



# TC - O(2 ^ N)
# SC - O(2 ^ N)
print(Solution().diffWaysToCompute("2-1-1"))
print(Solution().diffWaysToCompute("2*3-4*5"))
