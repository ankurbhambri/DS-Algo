# https://leetcode.com/problems/find-all-good-strings/

class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:

        MOD = 10**9 + 7
        m = len(evil)

        # LPS
        j = 0
        lps = [0] * m

        # pie table construction
        for i in range(1, m):

            while j > 0 and evil[i] != evil[j]:
                j = lps[j - 1]

            if evil[i] == evil[j]:
                j += 1
                lps[i] = j

        memo = {}

        def dp(pos, tight_low, tight_high, matched):

            # evil found
            if matched == m:
                return 0

            # built a valid string
            if pos == n:
                return 1
            
            if (pos, tight_low, tight_high, matched) in memo:
                return memo[(pos, tight_low, tight_high, matched)]

            low = s1[pos] if tight_low else 'a'
            high = s2[pos] if tight_high else 'z'

            ans = 0

            for c in range(ord(low), ord(high) + 1):

                ch = chr(c)

                # KMP
                nxt = matched

                while nxt > 0 and evil[nxt] != ch:
                    nxt = lps[nxt - 1]

                if evil[nxt] == ch:
                    nxt += 1

                ntight_low = tight_low and ch == low
                htight_high = tight_high and ch == high

                ans += dp(pos + 1, ntight_low, htight_high, nxt)

            memo[(pos, tight_low, tight_high, matched)] = ans % MOD

            return ans % MOD

        return dp(0, True, True, 0)