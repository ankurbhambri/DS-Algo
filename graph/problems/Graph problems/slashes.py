# https://leetcode.com/problems/regions-cut-by-slashes/description/


# Similar to https://leetcode.com/problems/number-of-islands/submissions/

from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:

        temp = [[0] * (len(grid[0]) * 3) for _ in range(len(grid) * 3)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                r, c = i * 3, j * 3

                if grid[i][j] == "/":
                    temp[r][c + 2] = 1
                    temp[r + 1][c + 1] = 1
                    temp[r + 2][c] = 1

                elif grid[i][j] == "\\":
                    temp[r][c] = 1
                    temp[r + 1][c + 1] = 1
                    temp[r + 2][c + 2] = 1

        def helper(r, c, visit):
            if (
                r < 0
                or c < 0
                or r >= len(temp)
                or c >= len(temp[0])
                or (r, c) in visit
                or temp[r][c] != 0
            ):
                return
            visit.add((r, c))
            dirs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for dr, dc in dirs:
                helper(dr, dc, visit)

        visit = set()
        res = 0
        for row in range(len(temp)):
            for col in range(len(temp[0])):
                if temp[row][col] == 0 and (row, col) not in visit:
                    helper(row, col, visit)
                    res += 1
        return res