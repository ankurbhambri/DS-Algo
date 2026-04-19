# https://atcoder.jp/contests/dp/tasks/dp_h

# similar to leetcode unique paths problem, but here we have some blocked cells as well '#'.

def solve(grid):

    m, n = len(grid), len(grid[0])

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    if grid[0][0] != '.':
        return 0

    dp[0][0] = 1

    for i in range(1, m + 1):
        if grid[i - 1][0] == '.':
            dp[i][0] = dp[i - 1][0]

    for j in range(1, n + 1):
        if grid[0][j - 1] == '.':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if grid[i - 1][j - 1] == '.':
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % (10**9 + 7)

    return dp[m][n]