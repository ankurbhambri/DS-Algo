from tokenize import group


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

            dirc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in dirc:

                row, col = dr + r, dc + c
                if (
                    row < 0
                    or col < 0
                    or row == R
                    or col == C
                    or grid[row][col] != 1
                ):
                    continue

                grid[row][col] = 2

                q.append([row, col])

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
