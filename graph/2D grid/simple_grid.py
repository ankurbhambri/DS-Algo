# DFS
def traverseGrid_DFS(graph):

    R, C = len(grid), len(grid[0])
    visit = set()

    def dfs(r, c):
        # base cndt

        if r < 0 or c < 0 or r >= R or c >= C or (r, c) in visit:
            return

        print(grid[r][c])

        visit.add((r, c))
        # traversing all four directions
        dfs(r, c + 1)
        dfs(r, c - 1)
        dfs(r + 1, c)
        dfs(r - 1, c)

        return True

    for r in range(R):
        for c in range(C):
            dfs(r, c)


# BFS
def traverseGrid_BFS(grid):
    R, C = len(grid), len(grid[0])
    visit = set()
    q = []

    q.append((0, 0))
    visit.add((0, 0))

    while q:
        x, y = q.pop(0)
        print(grid[x][y])

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dr, dc in dirs:
            r, c = x + dr, y + dc
            if r < 0 or c < 0 or r >= R or c >= C or (r, c) in visit:
                continue
            q.append((r, c))
            visit.add((r, c))


grid = [[3, 1, 5], [7, 8, 2], [14, 11, 9]]

traverseGrid_DFS(grid)
print('\n')
traverseGrid_BFS(grid)
