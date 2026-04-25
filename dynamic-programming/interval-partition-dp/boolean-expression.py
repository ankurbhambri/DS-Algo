'''
Problem Statement: Given an expression, A, with operands and operators (OR, AND, XOR), in how many ways can you evaluate the expression to be true, by grouping it in different ways?.

Operands are only true and false.

Return the number of ways to evaluate the expression modulo 103 + 3.

Examples:

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

from functools import lru_cache

# Recursive + Memoization (Top-Down DP) approach
# TC: O(n^3) and SC: O(n^2)
class Solution:
    def countWays(self, N, S):

        # Modulo as per standard competitive programming questions
        MOD = 1003

        @lru_cache(None)
        def solve(i, j, isTrue):

            # Base Case 1: Empty string
            if i > j:
                return 0

            # Base Case 2: Single character (T or F)
            if i == j:
                if isTrue:
                    return 1 if S[i] == 'T' else 0
                else:
                    return 1 if S[i] == 'F' else 0

            ways = 0

            # Loop sirf operators par chalega (index 1, 3, 5...)
            for k in range(i + 1, j, 2):

                # Left part ke True aur False ways
                LT = solve(i, k - 1, True)
                LF = solve(i, k - 1, False)

                # Right part ke True aur False ways
                RT = solve(k + 1, j, True)
                RF = solve(k + 1, j, False)

                operator = S[k]

                if operator == '&':
                    if isTrue:
                        ways += (LT * RT)
                    else:
                        ways += (LT * RF) + (LF * RT) + (LF * RF)

                elif operator == '|':
                    if isTrue:
                        ways += (LT * RT) + (LT * RF) + (LF * RT)
                    else:
                        ways += (LF * RF)

                elif operator == '^':
                    if isTrue:
                        ways += (LT * RF) + (LF * RT)
                    else:
                        ways += (LT * RT) + (LF * RF)
                
                # Har step par modulo lena zaroori hai
                ways %= MOD
                
            return ways

        # Pure expression (0 to N-1) ke liye True ways nikaalein
        return solve(0, N - 1, True)


# TC: O(n^3) and SC: O(n^2)
def countWaysTabular(N, S):

    MOD = 1003

    # Do 2D tables: T[i][j] aur F[i][j]
    T = [[0] * N for _ in range(N)]
    F = [[0] * N for _ in range(N)]

    # Gap-based traversal (Interval DP)
    # reason of 2 jump is because operands are at even indices (0,2,4...) and operators are at odd indices (1,3,5...),
    # so we only want to consider subexpressions that start and end at operands, hence the step of 2 in the gap and i loops
    for gap in range(0, N, 2):

        # i loop bhi 2 step ka hai kyunki hum sirf operands ke indices par hi subexpressions consider karna chahte hain
        for i in range(0, N - gap, 2):

            j = i + gap

            # Base Case: Single Character
            if gap == 0:
                T[i][j] = 1 if S[i] == 'T' else 0
                F[i][j] = 1 if S[i] == 'F' else 0

            else:
                # but yha pe hum operator ke indices par hi split kar rahe hain, isliye k ko i+1 se j-1 tak 2 step ke saath loop kar rahe hain
                for k in range(i + 1, j, 2):

                    op = S[k]

                    # k -1 tak ka left subexpression before operator
                    LT, LF = T[i][k - 1], F[i][k - 1]

                    # k + 1 se j tak ka right subexpression after operator
                    RT, RF = T[k + 1][j], F[k + 1][j]

                    if op == '&':
                        T[i][j] += (LT * RT)
                        F[i][j] += (LT * RF) + (LF * RT) + (LF * RF)

                    elif op == '|':
                        T[i][j] += (LT * RT) + (LT * RF) + (LF * RT)
                        F[i][j] += (LF * RF)

                    elif op == '^':
                        T[i][j] += (LT * RF) + (LF * RT)
                        F[i][j] += (LT * RT) + (LF * RF)

                    T[i][j] %= MOD
                    F[i][j] %= MOD

    return T[0][N-1]


print(countWaysTabular(5, "F|T^F")) # 2
print(countWaysTabular(7, "T|T&F^T")) # 4