# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:

        dp = [0] * 32
        dp[0] = 1

        for i in range(1, 32):
            dp[i] = 2 * dp[i - 1] + 1

        res = 0
        sign = 1

        for i in range(31, -1, -1):

            ibit = n & (1 << i) # Check if the i-th bit is set (1)

            if ibit == 0: # Skip if the bit is 0
                continue

            if sign > 0: # Add cost if sign is positive
                res += dp[i]

            else:
                res -= dp[i] # Subtract cost if sign is negative

            sign *= -1 # Flip the sign for the next encountered '1' bit

        return res


print(Solution().minimumOneBitOperations(3)) # Output: 2
print(Solution().minimumOneBitOperations(6)) # Output: 4