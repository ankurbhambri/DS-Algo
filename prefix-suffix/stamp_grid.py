# https://leetcode.com/problems/stamping-the-grid/


def possibleToStamp(grid, stampHeight, stampWidth):
    m, n = len(grid), len(grid[0])

    # Step 1: Prefix sum to determine if a stamp can be placed
    prefix = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            prefix[i + 1][j + 1] = (
                grid[i][j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j]
            )

    def can_place_stamp(x1, y1, x2, y2):
        return (
            prefix[x2 + 1][y2 + 1]
            - prefix[x1][y2 + 1]
            - prefix[x2 + 1][y1]
            + prefix[x1][y1]
            == 0
        )

    valid = [[0] * n for _ in range(m)]
    for i in range(m - stampHeight + 1):
        for j in range(n - stampWidth + 1):
            if can_place_stamp(i, j, i + stampHeight - 1, j + stampWidth - 1):
                valid[i][j] = 1

    # Step 2: Use a difference array to track coverage
    diff = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if valid[i][j]:
                diff[i][j] += 1
                diff[i + stampHeight][j] -= 1
                diff[i][j + stampWidth] -= 1
                diff[i + stampHeight][j + stampWidth] += 1

    # Step 3: Accumulate the difference array
    coverage = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            diff[i][j] += (
                (diff[i - 1][j] if i > 0 else 0)
                + (diff[i][j - 1] if j > 0 else 0)
                - (diff[i - 1][j - 1] if i > 0 and j > 0 else 0)
            )
            coverage[i][j] = diff[i][j] > 0

    # Step 4: Check if all empty cells are covered
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0 and coverage[i][j] == 0:
                return False

    return True


print(
    possibleToStamp(
        [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], 2, 2
    )
)
print(
    possibleToStamp(
        [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
        2,
        2,
    )
)
