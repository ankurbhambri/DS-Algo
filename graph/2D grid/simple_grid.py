# Classical Method


def classicTraverse(grid):

    R, C = len(grid), len(grid[0])
    visit = set()
    res = 0

    def isValid(r, c):
        if r < 0 or c < 0 or r >= R or c >= C or (r, c) in visit:
            return False
        return True

    def dfs(r, c):
        print(grid[r][c])
        visit.add((r, c))
        if isValid(r, c + 1):
            dfs(r, c + 1)
        if isValid(r, c - 1):
            dfs(r, c - 1)
        if isValid(r + 1, c):
            dfs(r + 1, c)
        if isValid(r - 1, c):
            dfs(r - 1, c)

    for r in range(R):
        for c in range(C):
            if dfs(r, c):
                res += 1

    return res, visit


# Clean Method
def traverseGrid(graph):

    R, C = len(grid), len(grid[0])
    visit = set()
    res = 0

    def dfs(r, c):
        # base cndt

        if r < 0 or c < 0 or r >= R or c >= C or (r, c) in visit:
            return

        print(grid[r][c])

        visit.add((r, c))

        dfs(r, c + 1)
        dfs(r, c - 1)
        dfs(r + 1, c)
        dfs(r - 1, c)

        return True

    for r in range(R):
        for c in range(C):
            if dfs(r, c):
                res += 1

    return res, visit


grid = [[3, 1, 5], [7, 8, 2], [14, 11, 9]]

print(classicTraverse(grid))

print(traverseGrid(grid))
