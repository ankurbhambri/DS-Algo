class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # reverse
        l = 0
        r = len(matrix) -1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1

        # transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))  # Output: [[7,4,1],[8,5,2],[9,6,3]]
print(Solution().rotate([[1,2],[3,4]]))  # Output: [[3,1],[4,2]]
