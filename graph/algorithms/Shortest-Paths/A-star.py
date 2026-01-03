""" A* is based on using heuristic methods to achieve optimality and completeness, and is a variant of the best-first algorithm.
When a search algorithm has the property of optimality, it means it is guaranteed to find the best possible solution, 
in our case the shortest path to the finish state. When a search algorithm has the property of completeness, 
it means that if a solution to a given problem exists, the algorithm is guaranteed to find it.

Each time A* enters a state, it calculates the cost, f(n) (n being the neighboring node), to travel to 
all of the neighboring nodes, and then enters the node with the lowest value of f(n).

These values are calculated with the following formula: f(n) = g(n) + h(n)  """


import heapq
from collections import deque


def a_star(grid, start, goal):

    rows, cols = len(grid), len(grid[0])

    # Manhattan distance
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_cost = {start: 0}

    while open_list:

        _, current = heapq.heappop(open_list)

        if current == goal:
            # Path reconstruct
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:

            neighbor = (current[0] + dx, current[1] + dy)

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == "#":
                    continue

                new_g = g_cost[current] + 1

                if neighbor not in g_cost or new_g < g_cost[neighbor]:
                    g_cost[neighbor] = new_g
                    f_cost = new_g + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_cost, neighbor))
                    came_from[neighbor] = current

    return None


grid = [
    ["S", ".", ".", "."],
    ["#", "#", ".", "#"],
    [".", ".", ".", "G"]
]

start = (0, 0)
goal = (2, 3)
print("Shortest Path:", a_star(grid, start, goal))


############################################# USing BFS #######################


def breadth_first_search(grid):

    N = len(grid)

    def is_clear(cell):
        return grid[cell[0]][cell[1]] == 0

    def get_neighbors(cell):
        i, j = cell
        for a in (-1, 0, 1):
            for b in (-1, 0, 1):
                if a == 0 and b == 0:
                    continue
                ni, nj = i + a, j + b
                if 0 <= ni < N and 0 <= nj < N and is_clear((ni, nj)):
                    yield (ni, nj)

    start = (0, 0)
    goal = (N - 1, N - 1)

    queue = deque()
    if is_clear(start):
        queue.append(start)

    dist = {start: 1}

    visited = set((start))

    while queue:

        cell = queue.popleft()

        if cell in visited:
            continue

        if cell == goal:
            return dist[cell]

        visited.add(cell)

        for neighbor in get_neighbors(cell):

            if neighbor not in dist:
                dist[neighbor] = dist[cell] + 1

            queue.append(neighbor)

    return -1


grid = [
    [0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
]

print(breadth_first_search(grid))
