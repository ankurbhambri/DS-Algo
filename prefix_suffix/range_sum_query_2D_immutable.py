# https://leetcode.com/problems/range-sum-query-2d-immutable/


class NumMatrix:

    def __init__(self, matrix):

        if not matrix:
            return

        rows, cols = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                self.prefix_sum[r][c] = (
                    matrix[r - 1][c - 1]
                    + self.prefix_sum[r - 1][c]
                    + self.prefix_sum[r][c - 1]
                    - self.prefix_sum[r - 1][c - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return (
            self.prefix_sum[row2][col2]
            - self.prefix_sum[row2][col1 - 1]
            - self.prefix_sum[row1 - 1][col2]
            + self.prefix_sum[row1 - 1][col1 - 1]
        )


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
