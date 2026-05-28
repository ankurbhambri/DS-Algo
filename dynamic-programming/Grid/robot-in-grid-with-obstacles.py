# Robot in a Grid with Obstacles: Like II, but ask for the actual path not just count. It is available on Cracking the Coding Interview (CTCI) not on leetcode.


'''
Imagine a robot sitting on the upper left corner of grid with r rows and c columns. 

The robot can only move in two directions, right and down, but certain cells are “off limits” such that the robot cannot step on them.

'''

# Backtracking with Memoization (Top-down DP)

# TC: O(m × n)
# SC: O(m × n) + recursion stack
class Solution:

    def pathWithObstacles(self, obstacleGrid):

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        path = []
        memo = set()  # memoize failed cells to avoid recomputation

        def backtrack(i, j):
            # Out of bounds or obstacle
            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                return False

            # If we've already visited this and found it fails
            if (i, j) in memo:
                return False

            # Destination reached
            if i == m - 1 and j == n - 1:
                path.append([i, j])
                return True

            # Explore right and down
            if backtrack(i, j + 1) or backtrack(i + 1, j):
                path.append([i, j])
                return True

            # Mark this cell as failed
            memo.add((i, j))

            return False

        if backtrack(0, 0):
            return path[::-1]  # reverse because we built path from end to start

        return []
    
print(Solution().pathWithObstacles([[0, 0, 0], [1, 1, 0], [0, 0, 0]]))  # Output: [[0, 0], [0, 1], [1, 2], [2, 2]]
print(Solution().pathWithObstacles([[0, 1], [0, 0]]))  # Output: [[0, 0], [1, 0], [1, 1]]


from collections import deque

# BFS Approach

# TC: O(m × n)
# SC: O(m × n) for the queue and parent map
class Solution:
    def pathWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return []

        queue = deque()
        queue.append((0, 0))
        parent = {}  # maps child → parent

        directions = [(0, 1), (1, 0)]  # right and down

        visited = set()
        visited.add((0, 0))

        while queue:
            i, j = queue.popleft()

            if (i, j) == (m - 1, n - 1):
                break  # reached destination

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and obstacleGrid[ni][nj] == 0 and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    parent[(ni, nj)] = (i, j)
                    queue.append((ni, nj))

        # If destination was never reached
        if (m - 1, n - 1) not in parent and (m - 1, n - 1) != (0, 0):
            return []

        # Reconstruct path
        path = []
        curr = (m - 1, n - 1)
        while curr != (0, 0):
            path.append([curr[0], curr[1]])
            curr = parent[curr]
        path.append([0, 0])

        return path[::-1]

print(Solution().pathWithObstacles([[0, 0, 0], [1, 1, 0], [0, 0, 0]]))  # Output: [[0, 0], [0, 1], [1, 2], [2, 2]]
print(Solution().pathWithObstacles([[0, 1], [0, 0]]))  # Output: [[0, 0], [1, 0], [1, 1]]
