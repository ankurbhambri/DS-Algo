# https://leetcode.com/problems/dungeon-game/description/


# TC: O(M * N)
# SC: O(M * N) + Stack Space
class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        
        memo = {}
        m, n = len(dungeon), len(dungeon[0])
    
        def dfs(i, j):

            if i >= m or j >= n:
                return float('inf')

            if (i, j) == (m-1, n-1):
                return max(1, 1 - dungeon[i][j])

            if (i, j) in memo:
                return memo[(i, j)]

            min_health_on_exit = min(dfs(i + 1, j), dfs(i, j + 1))

            memo[(i, j)] = max(1, min_health_on_exit - dungeon[i][j])

            return memo[(i, j)]

        return dfs(0, 0)


# TC: O(M * N)
# SC: O(M * N) + Stack Space
class Solution:
    def calculateMinimumHP(self, dungeon):

        m, n = len(dungeon), len(dungeon[0])

        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

        dp[m][n - 1] = 1
        dp[m - 1][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                # next_required -> min(dp[i + 1][j], dp[i][j + 1])
                # dungeon[i][j] -> current_cell_gain_loss

                need = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]

                dp[i][j] = max(1, need)

        return dp[0][0]