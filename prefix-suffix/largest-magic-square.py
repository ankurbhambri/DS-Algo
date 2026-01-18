# https://leetcode.com/problems/largest-magic-square/


class Solution:
    def largestMagicSquare(self, grid):

        m, n = len(grid), len(grid[0])

        preSumRow = [[0] * (n + 1) for _ in range(m)]
        preSumCol = [[0] * (m + 1) for _ in range(n)]

        for r in range(m):
            for c in range(n):
                preSumRow[r][c + 1] = preSumRow[r][c] + grid[r][c]
                preSumCol[c][r + 1] = preSumCol[c][r] + grid[r][c]

        def getSumRow(row, l, r):  # row, l, r inclusive
            return preSumRow[row][r + 1] - preSumRow[row][l]

        def getSumCol(col, l, r):  # row, l, r inclusive
            return preSumCol[col][r + 1] - preSumCol[col][l]

        def test(k):

            for r in range(m - k + 1):
                for c in range(n - k + 1):

                    diag, antiDiag = 0, 0

                    for d in range(k):
                        diag += grid[r + d][c + d]
                        antiDiag += grid[r + d][c + k - 1 - d]

                    match = diag == antiDiag
                    nr, nc = r, c

                    while nr < r + k and match:
                        match = diag == getSumRow(nr, c, c + k - 1)
                        nr += 1

                    while nc < c + k and match:
                        match = diag == getSumCol(nc, r, r + k - 1)
                        nc += 1

                    if match:
                        return True  # if all the sums is equal then return True as valid

            return False

        for k in range(min(m, n), 1, -1):
            if test(k):
                return k  # the first valid `k` is the maximum result

        return 1

print(Solution().largestMagicSquare(
    [[7,1,4,5,6],
    [2,5,1,6,4],
    [1,5,4,3,2],
    [1,2,7,3,4]]
))  # 3