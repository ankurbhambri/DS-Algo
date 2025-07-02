from collections import deque

# Walls and Gates leetcode problem


def walls_and_gates(rooms):

    r, c = len(rooms), len(rooms[0])
    q = deque()
    visit = set()

    # starting with gates and filling rest of rooms with shortest distance
    for i in range(r):
        for j in range(c):
            if rooms[i][j] == 0:
                q.append([i, j])
                visit.add((i, j))

    def helper(x, y):  # checking whether things are out of bounce or not wall etc
        if x < 0 or x == r or y < 0 or y == c or rooms[x][y] == -1 or (x, y) in visit:
            return
        q.append([x, y])
        visit.add((x, y))

    depth = 0

    while q:
        for i in range(len(q)):  # layer by layer
            a, b = q.popleft()
            rooms[a][b] = depth  # changing in rooms array
            # all four directions checking
            helper(a + 1, b)
            helper(a - 1, b)
            helper(a, b + 1)
            helper(a, b - 1)

        depth += 1  # once done incremet the depth of queue


# https://cses.fi/problemset/task/1194

from collections import deque


def solve_labyrinth(n, m, grid):

    directions = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}

    # Initialize variables
    start = None
    monsters = []
    monster_time = [[float("inf")] * m for _ in range(n)]

    # Parse the grid
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "A":
                start = (i, j)
            elif grid[i][j] == "M":
                monsters.append((i, j))

    # BFS from monsters
    queue = deque(monsters)
    for x, y in monsters:
        monster_time[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions.values():
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < n
                and 0 <= ny < m
                and grid[nx][ny] == "."
                and monster_time[nx][ny] == float("inf")
            ):
                monster_time[nx][ny] = monster_time[x][y] + 1
                queue.append((nx, ny))

    # BFS from start
    queue = deque([(start[0], start[1], 0, "")])
    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True

    while queue:
        x, y, time, path = queue.popleft()

        # Check if we're at the boundary
        if x == 0 or x == n - 1 or y == 0 or y == m - 1:
            print("YES")
            print(len(path))
            print(path)
            return

        for d, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < n
                and 0 <= ny < m
                and not visited[nx][ny]
                and grid[nx][ny] == "."
            ):
                # Only move if we reach before the monsters
                if time + 1 < monster_time[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, time + 1, path + d))

    # If no valid path found
    print("NO")


# Input reading
# n, m = map(int, input().split())
# grid = [input().strip() for _ in range(n)]

# solve_labyrinth(n, m, grid)


# https://leetcode.com/problems/escape-the-spreading-fire/description/



"""
Problem: Best Place to Install a Well

You are given a grid representing a village. Each cell in the grid can be:
- '_' : empty land (can place a well here)
- 'H' : a house
- 'T' : a tree (cannot be passed through or built on)

People can move up, down, left, or right, but cannot walk through trees or houses.
Your task is to find the empty cell where placing a well minimizes the total sum of distances from all houses to the well.
Return the minimum total distance, or -1 if no such cell exists.

Example:
Input grid:
_ _ H T
_ _ T _
_ _ H _

Output: 3
"""

from collections import deque
from typing import List

class Solution:
    def findBestWellPosition(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        m, n = len(grid), len(grid[0])
        total_distance = [[0] * n for _ in range(m)]
        reachable_count = [[0] * n for _ in range(m)]
        house_count = 0
        
        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Start BFS from each house
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'H':
                    house_count += 1
                    visited = [[False]*n for _ in range(m)]
                    queue = deque()
                    queue.append((i, j, 0))
                    visited[i][j] = True

                    while queue:
                        x, y, dist = queue.popleft()


                        for dx, dy in directions:

                            nx, ny = x + dx, y + dy

                            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:

                                if grid[nx][ny] == '_':

                                    total_distance[nx][ny] += dist + 1

                                    reachable_count[nx][ny] += 1

                                    queue.append((nx, ny, dist + 1))

                                # Visitable only if empty land; skip trees or houses
                                visited[nx][ny] = True

        # Find the minimum distance where all houses can reach
        min_dist = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '_' and reachable_count[i][j] == house_count:
                    min_dist = min(min_dist, total_distance[i][j])

        return min_dist if min_dist != float('inf') else -1


print(Solution().findBestWellPosition([
    ['_', '_', 'H', 'T'],
    ['_', '_', 'T', '_'],
    ['_', '_', 'H', '_']
]))  # Output: 3
