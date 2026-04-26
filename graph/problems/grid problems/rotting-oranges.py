# https://leetcode.com/problems/rotting-oranges/

from collections import deque

class Solution:
    def orangesRotting(self, grid):

        R = len(grid)
        C = len(grid[0])

        q = deque()
        fresh, time = 0, 0

        for i in range(R):
            for j in range(C):

                if grid[i][j] == 1:
                    fresh += 1

                if grid[i][j] == 2:
                    q.append([i, j])

        dirc = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q and fresh > 0:

            for i in range(len(q)):

                r, c = q.popleft()

                for dr, dc in dirc:

                    nr, nc = dr + r, dc + c

                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:

                        grid[nr][nc] = 2
                        q.append([nr, nc])
                        fresh -= 1

            time += 1

        return time if fresh == 0 else -1


# Follow up

# What if each rotten orange infects its neighbors only after k minutes, where k is the value of its cell?

# For example, if one orange spreads in 2 minutes and another in 5 minutes, a farther but faster-spreading orange might infect cells earlier than a closer slow one. 
# So instead of level-order BFS, we need a min-heap to always process the earliest infection.

import heapq

def min_time_to_rot_all(grid):

    heap = []

    rows, cols = len(grid), len(grid[0])

    dist = [[float('inf')] * cols for _ in range(rows)]

    # Step 1: Add all rotten oranges
    for r in range(rows):
        for c in range(cols):

            if grid[r][c] == 2:
                dist[r][c] = 0
                heapq.heappush(heap, (0, r, c))

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    # Step 2: Dijkstra
    while heap:

        time, r, c = heapq.heappop(heap)

        if time > dist[r][c]:
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 0:

                new_time = time + grid[r][c]

                # relaxation
                if new_time < dist[nr][nc]:
                    dist[nr][nc] = new_time
                    heapq.heappush(heap, (new_time, nr, nc))

    # Step 3: Compute result
    max_time = 0

    for r in range(rows):
        for c in range(cols):

            if grid[r][c] == 1:

                if dist[r][c] == float('inf'):
                    return -1

                max_time = max(max_time, dist[r][c])

    return max_time


# Simlar: https://www.codechef.com/SNCKPB17/problems/SNSOCIAL/

def bfs_maximum_weath(n, m, a):
    # Directions for 8 neighbors (left, right, up, down, 4 diagonals)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    # Find the maximum wealth in the grid
    max_wealth = max(max(row) for row in a)

    # Create a queue for BFS and a visited matrix
    queue = deque()
    visited = [[False] * m for _ in range(n)]

    # Initialize the queue with cells that have the maximum wealth
    for i in range(n):
        for j in range(m):
            if a[i][j] == max_wealth:
                queue.append((i, j, 0))  # (row, col, hour)
                visited[i][j] = True

    # Perform BFS
    max_hours = 0
    while queue:
        i, j, hour = queue.popleft()

        # Explore all 8 neighbors
        for di, dj in directions:
            ni, nj = i + di, j + dj

            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                # Update the wealth to the maximum wealth of the neighbors
                visited[ni][nj] = True
                a[ni][nj] = max_wealth
                queue.append((ni, nj, hour + 1))
                max_hours = max(max_hours, hour + 1)

    return max_hours


# Hard
# https://cses.fi/problemset/task/1194

