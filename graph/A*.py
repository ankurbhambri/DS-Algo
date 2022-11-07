''' A* is based on using heuristic methods to achieve optimality and completeness, and is a variant of the best-first algorithm.
When a search algorithm has the property of optimality, it means it is guaranteed to find the best possible solution, 
in our case the shortest path to the finish state. When a search algorithm has the property of completeness, 
it means that if a solution to a given problem exists, the algorithm is guaranteed to find it.

Each time A* enters a state, it calculates the cost, f(n) (n being the neighboring node), to travel to 
all of the neighboring nodes, and then enters the node with the lowest value of f(n).

These values are calculated with the following formula: f(n) = g(n) + h(n)  '''

from heapq import heappop, heappush


def shortestPathBinaryMatrix(grid):
    shortest_path = a_star_graph_search(
        start = (0, 0), 
        successor_function_obj = get_successor_function(grid),
        heuristic_function_obj = get_heuristic(grid)
    )
    if shortest_path is None or grid[0][0] == 1:
        return -1
    else:
        return len(shortest_path)


def a_star_graph_search(start, successor_function_obj, heuristic_function_obj):

    M, N = len(grid), len(grid[0])
    visited = set()
    came_from = dict()
    distance = {start: 0}
    frontier = PriorityQueue()
    frontier.add(start)

    while frontier:

        node = frontier.pop()

        if node in visited:
            continue
        # !! if coordinates reaches bottom right corner we got the answer hurray !!

        if node == (M-1, N-1):
            return reconstruct_path(came_from, start, node)
        visited.add(node)

        for successor in successor_function_obj(node):
            frontier.add(
                successor,
                priority = distance[node] + 1 + heuristic_function_obj(successor)
            )

            if (successor not in distance
                or distance[node] + 1 < distance[successor]):
                distance[successor] = distance[node] + 1
                came_from[successor] = node

    return None


def reconstruct_path(came_from, start, end):
    """
    >>> came_from = {'b': 'a', 'c': 'a', 'd': 'c', 'e': 'd', 'f': 'd'}
    >>> reconstruct_path(came_from, 'a', 'e')
    ['a', 'c', 'd', 'e']
    """
    reverse_path = [end]
    while end != start:
        end = came_from[end]
        reverse_path.append(end)
    return list(reversed(reverse_path))


def get_successor_function(grid):
    """
    grid =  [[0, 0, 0],
             [0, 1, 0],
             [1, 0, 0]]
    >>> f = get_successor_function(grid)
    >>> sorted(f((1, 2)))
    [(0, 1), (0, 2), (2, 1), (2, 2)]
    >>> sorted(f((2, 1)))
    [(1, 0), (1, 2), (2, 2)]
    """
    def get_clear_adjacent_cells(cell):
        i, j = cell
        return (
            (i + a, j + b)
            for a in (-1, 0, 1)
            for b in (-1, 0, 1)
            if a != 0 or b != 0
            if 0 <= i + a < len(grid)
            if 0 <= j + b < len(grid[0])
            if grid[i + a][j + b] == 0
        )
    return get_clear_adjacent_cells


def get_heuristic(grid):
    """
    >>> f = get_heuristic([[0, 0], [0, 0]])
    >>> f((0, 0))
    1
    >>> f((0, 1))
    1
    >>> f((1, 1))
    0
    """
    M, N = len(grid), len(grid[0])
    (a, b) = goal_cell = (M - 1, N - 1)
    def get_clear_path_distance_from_goal(cell):
        (i, j) = cell
        return max(abs(a - i), abs(b - j))
    return get_clear_path_distance_from_goal

class PriorityQueue:
    
    def __init__(self, iterable = []):
        self.heap = []
        for value in iterable:
            heappush(self.heap, (0, value))
    
    def add(self, value, priority = 0):
        heappush(self.heap, (priority, value))
    
    def pop(self):
        priority, value = heappop(self.heap)
        return value
    
    def __len__(self):
        return len(self.heap)


############################################# USing BFS #######################


from collections import deque


def breadth_first_search(grid):
    N = len(grid)

    def is_clear(cell):
        return grid[cell[0]][cell[1]] == 0

    def get_neighbors(cell):
        (i, j) = cell
        return (
            (i + a, j + b)
            for a in (-1, 0, 1)
            for b in (-1, 0, 1)
            if a != 0 or b != 0
            if 0 <= i + a < N
            if 0 <= j + b < N
            if is_clear( (i + a, j + b) )
        )

    start = (0, 0)
    goal = (N - 1, N - 1)

    queue = deque()
    if is_clear(start):
        queue.append(start)
    visited = set()
    path_len = {start: 1}

    while queue:
        cell = queue.popleft()
        if cell in visited:
            continue
        if cell == goal:
            return path_len[cell]
        visited.add(cell)
        for neighbor in get_neighbors(cell):
            if neighbor not in path_len:
                path_len[neighbor] = path_len[cell] + 1
            queue.append(neighbor)

    return -1


grid = [
	[0,0,0,1,0,0,1,0],
	[0,0,0,0,0,0,0,0],
	[1,0,0,1,1,0,1,0],
	[0,1,1,1,0,0,0,0],
	[0,0,0,0,0,1,1,1],
	[1,0,1,0,0,0,0,0],
	[1,1,0,0,0,1,0,0],
	[0,0,0,0,0,1,0,0]
]

print(breadth_first_search(grid))

print(shortestPathBinaryMatrix(grid))
