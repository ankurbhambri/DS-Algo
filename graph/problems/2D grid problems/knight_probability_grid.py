# https://leetcode.com/problems/knight-probability-in-chessboard/


def knightProbability(n, k, row, column):
    dp = {}

    def dfs(r, c, moves):
        if r < 0 or c < 0 or r >= n or c >= n:
            return 0
        if moves == 0:
            return 1
        if (r, c, moves) in dp:
            return dp[(r, c, moves)]
        # all 8 possible way for knight to travel in grid if it's placed in middle
        x1 = dfs(r - 2, c - 1, moves - 1)
        x2 = dfs(r - 1, c - 2, moves - 1)
        x3 = dfs(r + 1, c - 2, moves - 1)
        x4 = dfs(r + 2, c - 1, moves - 1)
        x5 = dfs(r + 2, c + 1, moves - 1)
        x6 = dfs(r + 1, c + 2, moves - 1)
        x7 = dfs(r - 1, c + 2, moves - 1)
        x8 = dfs(r - 2, c + 1, moves - 1)
        # in decimal value
        dp[(r, c, moves)] = (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8) / 8
        return dp[(r, c, moves)]

    return dfs(row, column, k)


print(knightProbability(n=3, k=2, row=0, column=0))
