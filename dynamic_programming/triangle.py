# memoization (top down)
# TC = O(N * N)
# SC = O(N * N) + Stack Space
def triangle(triangle, n):
    memo = [[-1 for _ in range(n)] for _ in range(n)]
    def helper(i, j):
        if memo[i][j] != -1:
            return memo[i][j]

        if i == n - 1:
            memo[i][j] = triangle[i][j]
            return memo[i][j]
        
        down = triangle[i][j] + helper(i + 1, j)
        dig = triangle[i][j] + helper(i + 1, j + 1)
        memo[i][j] = min(down, dig)
        return memo[i][j]
    helper(0, 0)
    return memo[0][0]
  
# tabulation (bottom up)
# TC = O(N * N)
# SC = O(N * N)
def minimumPathSum(triangle, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    dp[n - 1] = triangle[n - 1] # copy last row no way to compute down from it
    for i in range(n - 2, -1, -1):
        col = triangle[i] # col size in changing
        for j in range(len(col) - 1, -1, -1):
            dp[i][j] = min(triangle[i][j] + dp[i + 1][j], triangle[i][j] + dp[i + 1][j + 1])
    return dp[0][0]


# space optimization
# TC = O(N * N)
# SC = O(N)

def minimumPathSum(triangle, n):
    prev = triangle[n - 1] # copy last row no way to compute down from it

    for i in range(n - 2, -1, -1):

        col = triangle[i]
        tmp = [0] * (n)

        for j in range(len(col) - 1, -1, -1):

            tmp[j] = min(triangle[i][j] + prev[j], triangle[i][j] + prev[j + 1])

        prev = tmp

    return prev[0]
