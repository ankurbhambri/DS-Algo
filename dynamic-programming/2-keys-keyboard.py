# https://leetcode.com/problems/2-keys-keyboard/

# Backtracking solution

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        memo = {}

        def helper(currA, clipA):

            if currA == n:
                return 0

            if currA > n:
                # if excedded the number of operation limit
                return float("inf")

            if (currA, clipA) in memo:
                return memo[(currA, clipA)]

            # Two operations here, either copy all whatever is on the screen and copy again or paste whatever is copied previously.
            
            # Option - 1: Pasted already present value, copied value previously pasted again.
            paste = 1 + helper(currA + clipA, clipA)

            # Option - 2:  Copy all then paste two times same value on screen.
            copyAllPaste = 2 + helper(currA + currA, currA)

            memo[(currA, clipA)] = min(paste, copyAllPaste)

            return memo[(currA, clipA)]

        return 1 + helper(1, 1)
   


print(Solution().minSteps(3))  # 3
print(Solution().minSteps(1))  # 0
print(Solution().minSteps(6))  # 5
print(Solution().minSteps(18))  # 8
print(Solution().minSteps(315))  # 17


# We can solve this problem using prime factorization technique more optimimum way.
def minSteps_primeFactors(n):

    factors = 0
    divisor = 2

    while n >= 2:
        if n % divisor == 0:
            factors += divisor
            n //= divisor
        else:
            divisor += 1

    return factors


print(minSteps_primeFactors(3))  # 3
print(minSteps_primeFactors(1))  # 0
print(minSteps_primeFactors(6))  # 5
print(minSteps_primeFactors(18))  # 8
print(minSteps_primeFactors(27))  # 9
print(minSteps_primeFactors(315))  # 17
