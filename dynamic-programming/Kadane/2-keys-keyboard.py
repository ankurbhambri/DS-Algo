# https://leetcode.com/problems/2-keys-keyboard/

# Backtracking solution

# TC: O(2^n) in worst case, but generally much less due to pruning
# SC: O(n) for the recursion stack
class Solution:
    def minSteps(self, n: int) -> int:

        if n == 1:
            return 0

        # Memoization dictionary
        memo = {}

        def solve(screen, clipboard):

            # Base Case 1: Agar hum exact target par pahunch gaye
            if screen == n:
                return 0

            # Base Case 2: Agar screen par target se zyada 'A' ho gaye, toh yeh invalid path hai
            if screen > n:
                return float('inf')

            # Check if already calculated
            if (screen, clipboard) in memo:
                return memo[(screen, clipboard)]

            # Choice 1: Sirf Paste karo
            op1 = 1 + solve(screen + clipboard, clipboard)

            # Choice 2: Copy All + Paste karo (Ek saath dono kaam) so two operations
            op2 = 2 + solve(screen * 2, screen)

            # Dono choices mein se jo minimum steps de
            memo[(screen, clipboard)] = min(op1, op2)

            return memo[(screen, clipboard)]

        # Shuruat mein: Screen par 1 'A' hai, aur clipboard khali (1) hai
        return 1 + solve(1, 1)


print(Solution().minSteps(3))  # 3
print(Solution().minSteps(1))  # 0


# We can solve this problem using prime factorization technique more optimimum way.
# TC: O(sqrt(n)) in worst case, but generally much less due to prime factorization
# SC: O(1)
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