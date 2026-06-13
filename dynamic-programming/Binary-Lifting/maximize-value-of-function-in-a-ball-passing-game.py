# https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/


class Solution:
    def getMaxFunctionValue(self, receiver, k: int) -> int:

        n = len(receiver)
        LOG = k.bit_length() + 1

        # up[i][j] = node reached after 2^j jumps from i
        up = [[0] * LOG for _ in range(n)]

        # sm[i][j] = sum collected during those 2^j jumps
        sm = [[0] * LOG for _ in range(n)]

        # Base case
        for i in range(n):
            up[i][0] = receiver[i]
            sm[i][0] = receiver[i]

        # Build binary lifting tables
        for j in range(1, LOG):

            for i in range(n):

                up[i][j] = up[up[i][j - 1]][j - 1]

                sm[i][j] = sm[i][j - 1] + sm[up[i][j - 1]][j - 1]

        ans = 0

        # Try every starting node
        for start in range(n):

            curr = start
            total = start

            for bit in range(LOG):

                if k & (1 << bit):

                    total += sm[curr][bit]

                    curr = up[curr][bit]

            ans = max(ans, total)

        return ans