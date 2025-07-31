- General DP Grid Template (Bottom-Up)
```
def solve(grid):
    m, n = len(grid), len(grid[0])
    
    dp = [[0] * n for _ in range(m)]

    # Step 1: Base case
    dp[0][0] = grid[0][0]  # or 1 for counting paths

    # Step 2: Fill first row
    for j in range(1, n):
        if is_blocked(grid[0][j]):  # optional
            dp[0][j] = 0
        else:
            dp[0][j] = dp[0][j - 1] + grid[0][j]  # or just dp[0][j - 1] for path counting

    # Step 3: Fill first column
    for i in range(1, m):
        if is_blocked(grid[i][0]):
            dp[i][0] = 0
        else:
            dp[i][0] = dp[i - 1][0] + grid[i][0]

    # Step 4: Fill the rest
    for i in range(1, m):
        for j in range(1, n):
            if is_blocked(grid[i][j]):
                dp[i][j] = 0
            else:
                dp[i][j] = grid[i][j] + min_or_max_or_count(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]

```