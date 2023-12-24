# https://leetcode.com/problems/walls-and-gates/
import collections


class Solution:
    def wallsAndGates(self, rooms):
        m, n = len(rooms), len(rooms[0])
        q = collections.deque()
        paths = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        empty = 2147483647

        # Adding gates co-ordinates to the Queue for peforming BFS
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))

        # Computing BFS for all gates
        step = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                print(r, c)
                for x, y in paths:
                    nr, nc = r + x, c + y
                    print(nr, nc)
                    # skipping out of bounds, obstacles and already updated cells
                    if not (0 <= nr < m and 0 <= nc < n) or rooms[nr][nc] != empty:
                        continue
                    rooms[nr][nc] = step
                    q.append((nr, nc))
            # Incrememting step by 1 after all cells belonging to specific level in the queue are covered.
            step += 1

        return rooms


obj = Solution()
print(
    obj.wallsAndGates(
        [
            [2147483647, -1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647],
        ]
    )
)
