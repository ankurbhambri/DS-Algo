# https://leetcode.com/problems/numbers-with-repeated-digits/


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:

        s = str(n)

        memo = {}

        def dp(pos, tight, mask):

            if pos == len(s):
                return 1 if mask else 0

            if (pos, tight, mask) in memo:
                return memo[(pos, tight, mask)]

            limit = int(s[pos]) if tight else 9

            cnt = 0

            for d in range(limit + 1):

                ntight = tight and (d == limit)

                if mask == 0 and d == 0:

                    cnt += dp(pos + 1, ntight, mask)

                else:

                    # skip if digit already used
                    if mask & (1 << d):
                        continue

                    cnt += dp(pos + 1, ntight, mask | (1 << d))

            memo[(pos, tight, mask)] = cnt

            return cnt

        unique = dp(0, True, 0)

        return n - unique

print(Solution().numDupDigitsAtMostN(25)) # 2