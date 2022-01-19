def knight_moves(grid):
    R, C = len(grid), len(grid[0])

    # dis = [[-1] * C] * R  # Havinf  problem of shallow copy
    dis = []
    # Finding where is S -> Start and E -> End in the grid
    for i in range(R):
        a = []
        for j in range(C):
            a.append(0)
        dis.append(a)

    start = end = None

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'A':
                start = (i, j)
            if grid[i][j] == 'B':
                end = (i, j)

    q = []
    visit = set()
    q.append(start)
    visit.add(start)

    while q:
        r, c = q.pop(0)
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for dr, dc in dirs:
            x = r + dr
            y = c + dc
            if x < 0 or y < 0 or x >= R or y >= C or (x, y) in visit:
                continue

            q.append((x, y))
            visit.add((x, y))
            dis[x][y] = dis[r][c] + 1

    return dis[end[0]][end[1]]


grid = [
    ['', 'B', '', ''],
    ['', '', '', ''],
    ['', 'A', '', ''],
    ['', '', '', ''],
    ['', '', '', ''],
]

print(knight_moves(grid))
