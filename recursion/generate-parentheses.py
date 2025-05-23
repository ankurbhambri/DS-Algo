# https://leetcode.com/problems/generate-parentheses

def generateParenthesis(n):

    res = []
    def helper(s, open, close):
        if len(s) == 2 * n:
            res.append(s)
            return

        if open < n:
            helper(s + '(', open + 1, close)
        if close < open:
            helper(s + ')', open, close + 1)
    
    helper("", 0, 0)
    return res

print(generateParenthesis(3))  # Output: ['((()))', '(()())', '(())()', '()(())', '()()()']
print(generateParenthesis(1))  # Output: ['()']
print(generateParenthesis(2))  # Output: ['(())', '()()']
print(generateParenthesis(4))  # Output: ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())(())', '(())()()', '()()()()']