# https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

from functools import cache

class Solution:
    def atMostNGivenDigitSet(self, digits: list[str], n: int) -> int:

        digits = [int(x) for x in digits]
        s = str(n)

        @cache
        def dp(pos, tight, started):

            if pos == len(s):
                return 1 if started else 0

            limit = int(s[pos]) if tight else 9

            ans = 0

            # leading zero, for 007, 003, 035...
            if not started:
                ans += dp(pos + 1, False, False)

            for d in digits:
                
                # case when pos 0 we are trying to greater value then n's 0 position
                # like n = 100 and at pos 0 we are trying to put 3__ or 2__ not possible.
                if d > limit:
                    break

                ntight = tight and d == limit

                ans += dp(pos + 1, ntight, True)

            return ans

        return dp(0, True, False)


print(Solution().atMostNGivenDigitSet(["1","3","5","7"], 100)) # 20