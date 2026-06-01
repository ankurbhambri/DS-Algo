# https://leetcode.com/problems/largest-submatrix-with-rearrangements/


class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        res = 0
        n = len(matrix[0])
        h = [0] * n
        for row in matrix:
            for i, num in enumerate(row):
                h[i] = 0 if num == 0 else h[i] + 1
            hg = sorted(h)
            for i, val in enumerate(hg):
                res = max(res, val * (n - i))
        return res


print(Solution().largestSubmatrix([[1,0,1,0,1]]))  # 3
print(Solution().largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]]))  # 4