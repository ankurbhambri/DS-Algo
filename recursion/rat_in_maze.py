def rat_in_maze(maze):

    n = len(maze)
    result = []
    visited = [[False]*n for _ in range(n)]

    def is_safe(x, y):
        return 0 <= x < n and 0 <= y < n and maze[x][y] == 1 and not visited[x][y]

    def solve(x, y, path):
        if x == n-1 and y == n-1:
            result.append(path)
            return

        # Mark the cell visited
        visited[x][y] = True

        # Move Down
        if is_safe(x+1, y):
            solve(x+1, y, path + "D")

        # Move Left
        if is_safe(x, y-1):
            solve(x, y-1, path + "L")

        # Move Right
        if is_safe(x, y+1):
            solve(x, y+1, path + "R")

        # Move Up
        if is_safe(x-1, y):
            solve(x-1, y, path + "U")

        # Backtrack
        visited[x][y] = False

    if maze[0][0] == 1:
        solve(0, 0, "")
        result.sort()

    return result

print(
    rat_in_maze(
        [[1, 0, 0, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 0],
        [1, 1, 1, 1]]
    )
)  # ['DDDRRR']