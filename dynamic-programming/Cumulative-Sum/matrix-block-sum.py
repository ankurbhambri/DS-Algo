# https://leetcode.com/problems/matrix-block-sum

# similar - https://www.geeksforgeeks.org/given-n-x-n-square-matrix-find-sum-sub-squares-size-k-x-k/


class Solution:
    def matrixBlockSum(self, mat, k):

        m, n = len(mat), len(mat[0])

        pref = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                pref[i + 1][j + 1] = (
                    mat[i][j]
                    + pref[i][j + 1]
                    + pref[i + 1][j]
                    - pref[i][j]
                )

        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):

                r1 = max(0, i - k)
                c1 = max(0, j - k)

                r2 = min(m - 1, i + k)
                c2 = min(n - 1, j + k)

                ans[i][j] = (
                    pref[r2 + 1][c2 + 1]
                    - pref[r1][c2 + 1]
                    - pref[r2 + 1][c1]
                    + pref[r1][c1]
                )

        return ans


print(Solution().matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1)) # [[12, 21, 16], [27, 45, 33], [24, 39, 28]]
print(Solution().matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2)) # [[45, 45, 45], [45, 45, 45], [45, 45, 45]]