''' In this problem we have to find shortest path from start -> S to end -> E in a jungle '''

# Using BFS
def jungleRun(grid):

    R, C = len(grid), len(grid[0])
    # intially 0 distance from every node
    dist = [[0] * C for _ in range(R)]
    # first find the cordinates for start and end of grid
    start = None
    end = None

    # Finding where is S -> Start and E -> End in the grid
    for i in range(R):
        for j in range(C):
            if grid[i][j] == "S":
                start = (i, j)
            if grid[i][j] == "E":
                end = (i, j)
            if start and end:
                break

    visit = set()
    q = []
    q.append(start)
    visit.add(start)

    while q:
        x, y = q.pop(0)

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for dr, dc in dirs:
            r, c = x + dr, y + dc
            if (
                r < 0
                or c < 0
                or r >= R
                or c >= C
                or (r, c) in visit
                or grid[r][c] == 'T'
            ):  # N means we can't go further way block
                continue

            visit.add((r, c))
            q.append((r, c))
            dist[r][c] = 1 + dist[x][y]

    return dist[end[0]][end[1]]


grid = [
    ['S', 'N', 'P', 'P', 'P'],
    ['P', 'P', 'P', 'N', 'P'],
    ['P', 'N', 'N', 'N', 'P'],
    ['p', 'N', 'E', 'P', 'P'],
]

grid2 = [
    ["S", "P", "P", "P", "P", "P", "P", "T", "P", "T", "P", "P", "P", "P"],
    ["P", "P", "T", "P", "T", "P", "T", "P", "P", "E", "P", "T", "T", "P"],
    ["T", "T", "P", "P", "P", "T", "P", "T", "P", "T", "T", "P", "P", "T"],
    ["P", "P", "P", "T", "P", "T", "T", "P", "P", "P", "P", "P", "T", "P"],
    ["P", "P", "T", "P", "P", "P", "P", "T", "P", "T", "T", "P", "P", "T"],
    ["T", "T", "P", "T", "P", "T", "P", "P", "T", "P", "T", "P", "T", "P"],
    ["P", "P", "P", "P", "P", "T", "P", "T", "P", "P", "P", "P", "P", "P"],
    ["T", "P", "T", "P", "T", "P", "P", "P", "T", "P", "T", "P", "T", "T"],
    ["T", "T", "P", "T", "T", "P", "T", "T", "P", "P", "P", "T", "P", "T"],
    ["P", "P", "T", "P", "P", "P", "T", "P", "T", "P", "T", "P", "P", "P"],
    ["P", "T", "P", "P", "T", "T", "P", "T", "T", "P", "T", "P", "P", "T"],
    ["T", "P", "T", "P", "T", "P", "P", "P", "P", "P", "P", "P", "T", "P"],
    ["P", "T", "P", "P", "P", "P", "T", "P", "P", "T", "P", "T", "P", "T"],
    ["P", "P", "T", "P", "T", "P", "P", "T", "T", "P", "P", "P", "T", "P"],
]
print(jungleRun(grid2))
