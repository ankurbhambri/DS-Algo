# https://leetcode.com/problems/minimum-jumps-to-reach-home/

from collections import deque

class Solution:
    def minimumJumps(self, forbidden, a, b, x):

        forbidden = set(forbidden)

        limit = 6000

        q = deque([(0, 1, 0)])
        visited = {(0, 1)}

        while q:

            pos, back, steps = q.popleft()

            if pos == x:
                return steps

            # forward
            nxt = pos + a

            if (
                0 <= nxt <= limit and
                nxt not in forbidden and
                (nxt, 1) not in visited
            ):
                visited.add((nxt, 1))
                q.append((nxt, 1, steps + 1))

            # backward
            if back:

                nxt = pos - b

                if (
                    0 <= nxt and
                    nxt not in forbidden and
                    (nxt, 0) not in visited
                ):
                    visited.add((nxt, 0))
                    q.append((nxt, 0, steps + 1))

        return -1