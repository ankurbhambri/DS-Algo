''' In this problem we have to find shortest path from start -> S to end -> E in a jungle '''

# Using BFS
def jungleRun(grid):

    R, C = len(grid), len(grid[0])
    # dis = [[-1] * C] * R  # Having  problem of shallow copy
    dist = []
    # Finding where is S -> Start and E -> End in the grid
    for i in range(R):
        a = []
        for j in range(C):
            a.append(0)
        dist.append(a)

    start = None
    end = None

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'S':
                start = (i, j)
            if grid[i][j] == "E":
                end = (i, j)

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
                or grid[r][c] == 'N'
            ):
                continue

            visit.add((r, c))
            q.append((r, c))
            dist[r][c] = dist[x][y] + 1

    return dist[end[0]][end[1]], dist


grid = [
    ['S', 'N', 'P', 'P', 'P'],
    ['P', 'P', 'P', 'N', 'P'],
    ['P', 'N', 'N', 'N', 'P'],
    ['p', 'N', 'E', 'P', 'P'],
]
print(jungleRun(grid))
