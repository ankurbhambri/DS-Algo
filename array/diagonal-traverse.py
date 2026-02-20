# https://leetcode.com/problems/diagonal-traverse/

# TC: O(m * n) where m and n are the dimensions of the matrix
# SC: O(m * n) for the output array and the diagonal grouping
class Solution:
    def findDiagonalOrder(self, mat):

        if not mat or not mat[0]:
            return []

        diags = {}
        m, n = len(mat), len(mat[0])

        # Group elements by diagonal (i + j)
        for i in range(m):
            for j in range(n):
                if i + j not in diags:
                    diags[i + j] = []
                diags[i + j].append(mat[i][j])

        res = []
        for k in range(len(diags)):
            # Even diagonals go upwards (reverse)
            if k % 2 == 0:
                res.extend(reversed(diags[k]))
            else:
                res.extend(diags[k])

        return res


print(Solution().findDiagonalOrder([[1,2],[3,4]]))
print(Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))


# Space optimized version without using extra space for grouping diagonals

# TC: O(m * n) where m and n are the dimensions of the matrix
# SC: O(1) excluding the output array
class Solution:
    def findDiagonalOrder(self, mat):

        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        res = []

        r = c = 0
        direction = 1  # 1 = up-right, -1 = down-left

        for _ in range(m * n):

            res.append(mat[r][c])

            if direction == 1:  # moving up-right
                # Hit right wall
                if c == n - 1:
                    r += 1
                    direction = -1
                # Hit top wall
                elif r == 0:
                    c += 1
                    direction = -1
                else:
                    r -= 1
                    c += 1

            else:  # moving down-left
                # Hit bottom wall
                if r == m - 1:
                    c += 1
                    direction = 1
                # Hit left wall
                elif c == 0:
                    r += 1
                    direction = 1
                else:
                    r += 1
                    c -= 1

        return res

print(Solution().findDiagonalOrder([[1, 2], [3, 4]]))
print(Solution().findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


# https://leetcode.com/problems/diagonal-traverse-ii/description/

from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums):

        groups = defaultdict(list)

        # Iterate through the array normally
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                # Group by index sum (i + j)
                groups[i + j].append(nums[i][j])

        res = []
        # Iterate through groups in increasing order of sum
        for k in range(len(groups)):
            # Because we appended elements in increasing row order (i), 
            # and we need bottom-to-top, we reverse each group.
            res.extend(reversed(groups[k]))

        return res

print(Solution().findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().findDiagonalOrder([[1, 2, 3], [4], [5, 6], [7, 8, 9]]))