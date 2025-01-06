# Medium
# https://leetcode.com/problems/rotting-oranges/

from collections import deque


def orangesRotting(grid):

    R = len(grid)
    C = len(grid[0])

    fresh, time = 0, 0
    q = deque()
    visit = set()

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                fresh += 1
            if grid[i][j] == 2:
                q.append([i, j])
                visit.add((i, j))

    dirc = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    while q and fresh > 0:

        for i in range(len(q)):

            r, c = q.popleft()

            for dr, dc in dirc:
                row, col = dr + r, dc + c

                # if in bound and fresh make rotten
                if (
                    row < 0 or col < 0 or row == R or col == C or grid[row][col] != 1
                ) or (row, col) in visit:
                    continue

                grid[row][col] = 2

                q.append([row, col])
                visit.add((row, col))

                fresh -= 1

        time += 1

    return time if fresh == 0 else -1


grid = [
    [2, 1, 2, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 2, 1, 1],
    [2, 0, 1, 0, 1],
    [1, 1, 1, 2, 0],
]

print(orangesRotting(grid))


# Medium
# https://www.codechef.com/SNCKPB17/problems/SNSOCIAL/


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

