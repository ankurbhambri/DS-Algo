# https://cp-algorithms.com/graph/01_bfs.html

from collections import deque


def zero_one_bfs(graph, source, n):

    dist = [float("inf")] * n

    dist[source] = 0

    dq = deque([source])

    while dq:

        node = dq.popleft()

        for neighbor, weight in graph[node]:

            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight

                if weight == 0:
                    dq.appendleft(neighbor)
                else:
                    dq.append(neighbor)

    return dist


graph = {0: [(1, 1), (2, 0)], 1: [(2, 1), (3, 0)], 2: [(3, 1)], 3: []}
print(zero_one_bfs(graph, 0, 4))  # [0, 1, 0, 1]
print(zero_one_bfs(graph, 1, 4))  # [inf, 0, 1, 1]
print(zero_one_bfs(graph, 2, 4))  # [inf, inf, 0, 1]


# similar questions


# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

from collections import deque


def minCost(grid):

    r, c = len(grid), len(grid[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Track minimum cost to reach each cell
    min_cost = [[float("inf")] * c for _ in range(r)]
    min_cost[0][0] = 0

    # Use deque for 0-1 BFS - add zero cost moves to front, cost=1 to back
    deque = deque([(0, 0)])

    def is_valid(row, col, r, c):
        return 0 <= row < r and 0 <= col < c

    while deque:
        row, col = deque.popleft()

        # Try all four directions
        [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]
        for dir_idx, (dx, dy) in enumerate(dirs):

            new_row, new_col = row + dx, col + dy

            cost = 0 if grid[row][col] == dir_idx + 1 else 1

            # If position is valid and we found a better path
            if (
                is_valid(new_row, new_col, r, c)
                and min_cost[row][col] + cost < min_cost[new_row][new_col]
            ):

                min_cost[new_row][new_col] = min_cost[row][col] + cost

                # Add to back if cost=1, front if cost=0
                if cost == 1:
                    deque.append((new_row, new_col))
                else:
                    deque.appendleft((new_row, new_col))

    return min_cost[r - 1][c - 1]


# https://codeforces.com/contest/1063/problem/B


from collections import deque


def labyrinth_solver():

    # Input reading
    n, m = map(int, input().split())  # Rows and columns
    r, c = map(int, input().split())  # Starting position (1-based)
    x, y = map(int, input().split())  # Maximum left and right moves

    # Convert starting position to 0-based index
    r -= 1
    c -= 1

    # Read the labyrinth
    labyrinth = [input().strip() for _ in range(n)]

    # Directions: up, down, left, right (row change, col change, cost left, cost right)
    directions = [(-1, 0, 0, 0), (1, 0, 0, 0), (0, -1, 1, 0), (0, 1, 0, 1)]

    # Visited array: visited[row][col] tracks (min_left_moves, min_right_moves)
    visited = [[(-1, -1) for _ in range(m)] for _ in range(n)]
    visited[r][c] = (0, 0)

    # Deque for 0-1 BFS
    deque_ = deque([(r, c, 0, 0)])  # (row, col, left_moves, right_moves)

    reachable_cells = 0

    while deque_:

        cr, cc, left_used, right_used = deque_.popleft()

        reachable_cells += 1  # Count this cell as reachable

        for dr, dc, cost_left, cost_right in directions:

            nr, nc = cr + dr, cc + dc

            if 0 <= nr < n and 0 <= nc < m and labyrinth[nr][nc] == ".":

                new_left_used = left_used + cost_left
                new_right_used = right_used + cost_right

                # Check if within constraints
                if new_left_used <= x and new_right_used <= y:
                    # Update visited if this path is better
                    if (
                        visited[nr][nc] == (-1, -1)
                        or new_left_used < visited[nr][nc][0]
                        or new_right_used < visited[nr][nc][1]
                    ):
                        visited[nr][nc] = (new_left_used, new_right_used)
                        if cost_left + cost_right == 0:
                            deque_.appendleft((nr, nc, new_left_used, new_right_used))
                        else:
                            deque_.append((nr, nc, new_left_used, new_right_used))

    print(reachable_cells)


labyrinth_solver()


# https://codeforces.com/problemset/problem/173/B
# https://codeforces.com/problemset/problem/590/C
# https://codeforces.com/problemset/problem/877/D
# https://codeforces.com/problemset/problem/173/C
