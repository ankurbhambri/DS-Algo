# https://leetcode.com/problems/rotting-oranges/


def rotten_oranges(grid):
    R, C = len(grid), len(grid[0])
    fresh = time = 0
    q = []
    for i in range(R):
        for j in range(C):
            # Fresh Oranges
            if grid[i][j] == 1:
                fresh += 1
            # Rotten Oranges
            if grid[i][j] == 2:
                q.append([i, j])

    while q and fresh > 0:

        for i in range(len(q)):

            r, c = q.pop(0)

            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in dirs:

                x, y = dr + r, dc + c

                if x < 0 or y < 0 or x == R or y == C or grid[x][y] != 1:
                    continue

                # Convert oranges into rotten 2 means rotten and 1 means fresh
                grid[x][y] = 2

                q.append([x, y])

                fresh -= 1

        time += 1

    return time if fresh == 0 else -1


grid = [
    [2, 1, 2, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 2, 1, 1],
    [2, 0, 1, 0, 1],
    [1, 1, 1, 2, 0],
]

print(rotten_oranges(grid))
