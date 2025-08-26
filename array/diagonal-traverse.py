# https://leetcode.com/problems/diagonal-traverse/


class Solution:
    def findDiagonalOrder(self, mat):

        res = []
        n, m = len(mat), len(mat[0])

        for d in range(n + m - 1):

            i = 0 if d < m else d - m + 1
            j = d if d < m else m - 1

            diag = []
            while i < n and j >= 0:
                diag.append(mat[i][j])
                i += 1
                j -= 1

            # reverse even diagonals
            if d % 2 == 0:
                diag.reverse()

            res.extend(diag)

        return res


print(Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().findDiagonalOrder([[1,2],[3,4]]))
