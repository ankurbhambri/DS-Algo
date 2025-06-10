# https://leetcode.com/problems/01-matrix/

from collections import deque

class Solution:
    def updateMatrix(self, mat):

        rows, cols = len(mat), len(mat[0])

        q = deque([])

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1  # Marked as not processed yet!

        while q:

            r, c = q.popleft()

            for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:

                nr, nc = r + x, c + y

                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:

                    # if we're currently at a cell (r, c) whose value is k, its neighbor (nr, nc) will have distance k + 1.
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr, nc))

        return mat


print(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))  # Output: [[0,0,0],[0,1,0],[1,2,1]]
print(Solution().updateMatrix([[0, 0, 0], [1, 1, 1], [1, 1, 1]]))  # Output: [[0,0,0],[1,2,1],[2,3,2]]
print(Solution().updateMatrix([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))  # Output: [[2,1,2],[1,0,1],[2,1,2]]
print(Solution().updateMatrix([[1, 0, 1], [1, 1, 1], [1, 0, 1]]))  # Output: [[0,0,0],[1,2,1],[0,0,0]]
