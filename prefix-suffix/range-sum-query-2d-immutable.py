# https://leetcode.com/problems/range-sum-query-2d-immutable/


class NumMatrix:
    def __init__(self, matrix: list[list[int]]):

        m, n = len(matrix), len(matrix[0])
        self.prex = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.prex[i][j] = matrix[i - 1][j - 1] + self.prex[i][j - 1] + self.prex[i - 1][j] - self.prex[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        # prefix matric is 1 based
        r1, c1 = row1 + 1, col1 + 1
        r2, c2 = row2 + 1, col2 + 1

        ans = (
            self.prex[r2][c2]
            - self.prex[r1 - 1][c2]
            - self.prex[r2][c1 - 1]
            + self.prex[r1 - 1][c1 - 1]
        )

        return ans


matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5],
]
num_matrix = NumMatrix(matrix)
print(num_matrix.sumRegion(2, 1, 4, 3))  # 8
print(num_matrix.sumRegion(1, 1, 2, 2))  # 11
print(num_matrix.sumRegion(1, 2, 2, 4))  # 12
print(num_matrix.sumRegion(0, 0, 0, 0))  # 3
print(num_matrix.sumRegion(0, 0, 0, 1))  # 3