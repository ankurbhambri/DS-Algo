# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/


class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:

        m, n = len(grid), len(grid[0])

        minDp = [[0] * n for _ in range(m)]
        maxDp = [[0] * n for _ in range(m)]

        minDp[0][0] = maxDp[0][0]  = grid[0][0]

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                vals = []
                x = grid[i][j]

                if i > 0:
                    vals.append(minDp[i - 1][j] * x)
                    vals.append(maxDp[i - 1][j] * x)

                if j > 0:
                    vals.append(minDp[i][j - 1] * x)
                    vals.append(maxDp[i][j - 1] * x)

                minDp[i][j] = min(vals)
                maxDp[i][j] = max(vals)

        ans = maxDp[m - 1][n - 1]

        return ans % (10**9 + 7) if ans >= 0 else -1


print(Solution().maxProductPath([[1, 3], [0, -4]]))
print(Solution().maxProductPath([[1, -2, 1], [1, -2, 1], [3, -4, 1]]))