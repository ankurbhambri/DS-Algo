# https://leetcode.com/problems/count-submatrices-with-all-ones/

# similar - https://leetcode.com/problems/largest-submatrix-with-rearrangements/
# https://leetcode.com/problems/sum-of-subarray-minimums/
# https://leetcode.com/problems/largest-rectangle-in-histogram/
# https://leetcode.com/problems/maximal-rectangle/
 
class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:

        res = 0
        heights = [0] * len(mat[0])

        for row in mat:

            for i, x in enumerate(row):
                heights[i] = 0 if x == 0 else heights[i] + 1

            stack = [[-1, 0, -1]] # idx, value, height

            for i, h in enumerate(heights):

                while stack[-1][2] >= h:
                    stack.pop()

                j, val, _ = stack[-1]

                # formula, previous value + (gap(curr idx - prev idx) * curr height)
                cur = val + (i - j) * h

                stack.append([i, cur, h])

                res += cur

        return res