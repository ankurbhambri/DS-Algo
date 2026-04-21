'''
Problem Statement: Given an expression, A, with operands and operators (OR, AND, XOR), in how many ways can you evaluate the expression to be true, by grouping it in different ways?.

Operands are only true and false.

Return the number of ways to evaluate the expression modulo 103 + 3.

Examples

Example 1:
Input: expression = “T|T&F”
Output: 1
Explanation: The only way to get the result as true is:
(T) | (T&F) = T|F = T 

Example 2:
Input: expression = “F|T^F”
Output: 2
Explanation: There are 2 possible ways to get the result as true:
        i. (F|T) ^ F = T ^ F = T
        ii. F | (T^F) = F | T = T

'''

# TC: O(n^3) and SC: O(n^2)
def countWays(expr):

    MOD = 1003

    # Separate operands and operators
    operands = []
    operators = []

    for i, ch in enumerate(expr):
        if i % 2 == 0:
            operands.append(ch)   # T or F
        else:
            operators.append(ch)  # |, &, ^

    n = len(operands)

    # dp[i][j][0] = false ways, dp[i][j][1] = true ways
    dp = [[[0, 0] for _ in range(n)] for _ in range(n)]

    # Base case: single operands
    for i in range(n):
        if operands[i] == 'T':
            dp[i][i][1] = 1
            dp[i][i][0] = 0
        else:
            dp[i][i][1] = 0
            dp[i][i][0] = 1

    # Fill for lengths 2 to n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # Split at each operator between i and j
            for k in range(i, j):
                op = operators[k]

                lt = dp[i][k][1]  # left true
                lf = dp[i][k][0]  # left false
                rt = dp[k+1][j][1]  # right true
                rf = dp[k+1][j][0]  # right false

                if op == '|':
                    dp[i][j][1] += lt*rt + lt*rf + lf*rt
                    dp[i][j][0] += lf*rf

                elif op == '&':
                    dp[i][j][1] += lt*rt
                    dp[i][j][0] += lf*rf + lf*rt + lt*rf

                elif op == '^':
                    dp[i][j][1] += lt*rf + lf*rt
                    dp[i][j][0] += lt*rt + lf*rf

                # Apply modulo
                dp[i][j][1] %= MOD
                dp[i][j][0] %= MOD

    return dp[0][n-1][1]


print(countWays("T|T&F"))   # Output: 1
print(countWays("T|T&F"))   # Output: 1
print(countWays("F|T^F"))   # Output: 2
print(countWays("T^F|F"))   # Output: 2