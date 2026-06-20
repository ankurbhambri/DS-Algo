# https://leetcode.com/problems/last-day-where-you-can-still-cross/


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:

        def lastDay(day):

            dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

            grid = [[0] * col for _ in range(row)]

            # simple dfs to find whether we are able to reach the last row or not?
            def dfs(r, c):

                if 0 > r or r >= row or 0 > c or c >= col or grid[r][c] != 0:
                    return False

                if r == row - 1:
                    return True

                grid[r][c] = 1

                for dr, dc in dirs:

                    x, y = dr + r, dc + c

                    if dfs(x, y):
                        return True

                return False

            # first block all the cells in the grid based on the ith day
            for j in range(day):
                r, c = cells[j]
                grid[r - 1][c - 1] = 1

            # then run dfs on the grid to find that is it possible to hit the last row with water
            for i in range(col):
                if grid[0][i] == 0:
                    if dfs(0, i):
                        return True

            return False

        # binary search
        l, r = 0, len(cells) - 1
        while l <= r:
            m = (r + l) // 2
            if lastDay(m):
                l = m + 1
            else:
                r = m - 1
        return l - 1


print(Solution().latestDayToCross(2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]])) # 2
print(Solution().latestDayToCross(2, 2, [[1, 1], [1, 2], [2, 1], [2, 2]])) # 1