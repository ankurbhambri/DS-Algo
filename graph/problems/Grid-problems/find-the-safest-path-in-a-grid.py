# https://leetcode.com/problems/find-the-safest-path-in-a-grid/

from collections import deque
from heapq import heappop, heappush

# Using Multi source BFS to find the distance of each cell and then using Dijkstra's algorithm to find the maximum safeness factor path from (0, 0) to (R-1, C-1)
class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:

        if grid[0][0] == 1:
            return 0

        R, C = len(grid), len(grid[0])
        thief_dist = [[float("inf")] * C for _ in range(R)]

        thief = deque()

        for i in range(R * C):
            if grid[i // C][i % C] == 1:
                thief.append((i // C, i % C))
                thief_dist[i // C][i % C] = 0
        
        # Multi-source BFS to find the distance of each cell from the nearest thief
        while thief:

            r, c = thief.popleft()

            for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:

                a, b = r + x, c + y

                if 0 <= a < R and 0 <= b < C and thief_dist[a][b] == float("inf"):

                    thief_dist[a][b] = thief_dist[r][c] + 1

                    thief.append((a, b))


        # Dijikstra's algorithm to find the maximum safeness factor path from (0, 0) to (R-1, C-1)
        visit = {}

        q = [(-thief_dist[0][0], 0, 0)]

        while q:

            safety, r, c = heappop(q)

            safety = -safety

            if (r, c) == (R - 1, C - 1):
                return safety

            if (r, c) in visit and visit[(r, c)] >= safety:
                continue

            visit[(r, c)] = safety

            for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:

                a, b = r + x, c + y

                if 0 <= a < R and 0 <= b < C and (a, b) not in visit:

                    # yha pe minimum distance to thief ko check karna hoga, kyunki hume maximum safeness chahiye
                    new_dist = min(safety, thief_dist[a][b])

                    heappush(q, (-new_dist, a, b))

        return -1


print(Solution().maximumSafenessFactor([[0, 0, 1], [0, 0, 0], [0, 0, 0]])) # 2
print(Solution().maximumSafenessFactor([[0, 0, 0, 0, 0], [1, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]])) # 1