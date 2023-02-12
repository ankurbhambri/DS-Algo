'''Counting nos of rooms in an grid where 1 is wall and 0 is room diameter or size'''


def counting_rooms_dfs(graph):

    R, C = len(grid), len(grid[0])
    visit = set()

    def dfs(r, c):

        if (
            r < 0
            or c < 0
            or r >= R
            or c >= C
            or grid[r][c] == 1
            or (r, c) in visit
        ):
            return 0

        visit.add((r, c))
        res = 0
        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            x, y = r + dr, c + dc
            res += dfs(x, y)
        # res += dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)
        return res + 1

    ans = []
    # ans = dfs(0, 0)
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0 and (r, c) not in visit:
                ans.append(dfs(r, c))

    return ans

grid = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 0],
]

print(counting_rooms_dfs(grid))
