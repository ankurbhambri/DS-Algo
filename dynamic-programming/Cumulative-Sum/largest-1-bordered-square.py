# https://leetcode.com/problems/largest-1-bordered-square/


class Solution:
    def largest1BorderedSquare(self, grid: list[list[int]]) -> int:

        m, n = len(grid), len(grid[0])

        left = [[0] * n for _ in range(m)]
        up = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):

                if grid[r][c] == 1:

                    left[r][c] = 1 + (left[r][c - 1] if c else 0)
                    up[r][c] = 1 + (up[r - 1][c] if r else 0)

        best = 0

        for r in range(m):

            for c in range(n):

                size = min(left[r][c], up[r][c])

                while size > best:

                    if (left[r - size + 1][c] >= size and up[r][c - size + 1] >= size):
                        best = size

                    size -= 1

        return best * best