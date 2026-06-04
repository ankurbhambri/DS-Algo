# https://leetcode.com/problems/numbers-with-repeated-digits/

from functools import cache

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:

        s = str(n)

        memo = {}
        def dp(pos, tight, started, mask):

            if pos == len(s):
                return 1 if started else 0
            
            if (pos, tight, started, mask) in memo:
                return memo[(pos, tight, started, mask)]

            limit = int(s[pos]) if tight else 9

            cnt = 0

            for d in range(limit + 1):

                ntight = tight and (d == limit)

                if not started and d == 0:

                    cnt += dp(pos + 1, ntight, False, mask)

                else:

                    # skip if digit already used
                    if mask & (1 << d):
                        continue

                    cnt += dp(pos + 1, ntight, True, mask | (1 << d))

            memo[(pos, tight, started, mask)] = cnt

            return cnt

        unique = dp(0, True, False, 0)

        return n - unique

print(Solution().numDupDigitsAtMostN(25)) # 2