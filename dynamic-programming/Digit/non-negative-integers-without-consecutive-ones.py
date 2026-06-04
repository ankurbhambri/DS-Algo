# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/

from functools import cache

class Solution:
    def findIntegers(self, n: int) -> int:

        bits = bin(n)[2:]

        @cache
        def dp(pos, tight, prev):

            if pos == len(bits):
                return 1

            limit = int(bits[pos]) if tight else 1

            ans = 0

            for bit in range(limit + 1):

                if prev == 1 and bit == 1:
                    continue

                ans += dp(pos + 1, tight and bit == limit, bit)

            return ans

        return dp(0, True, 0)


print(Solution().findIntegers(5)) # 5