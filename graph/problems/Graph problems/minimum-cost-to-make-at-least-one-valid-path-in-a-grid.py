# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

from collections import deque

class Solution:
    def minCost(self, grid):

        m, n = len(grid), len(grid[0])

        directions = {
            1: (0, 1),   # Right
            2: (0, -1),  # Left
            3: (1, 0),   # Down
            4: (-1, 0)   # Up
        }

        cost = [[float('inf')] * n for _ in range(m)]
        cost[0][0] = 0

        dq = deque([(0, 0)])

        while dq:

            r, c = dq.popleft()

            for direction, (dr, dc) in directions.items():

                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:

                    move_cost = 0 if grid[r][c] == direction else 1
                    new_cost = cost[r][c] + move_cost

                    if new_cost < cost[nr][nc]:

                        cost[nr][nc] = new_cost

                        # 0-1 BFS trick:
                        if move_cost == 0:
                            dq.appendleft((nr, nc))  # Add to front

                        else:
                            dq.append((nr, nc))      # Add to back

        return cost[m-1][n-1]


print(Solution().minCost([[1,1,3],[3,2,2],[1,1,4]]))  # Output: 0
print(Solution().minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]))  # Output: 1