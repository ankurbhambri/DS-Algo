# https://leetcode.com/problems/minimum-falling-path-sum/


def minimum_falling_path_sum(matrix):
    n = len(matrix)

    for i in range(1, n):
        for j in range(n):

            mid = matrix[i - 1][j]
            left = matrix[i - 1][j - 1] if j - 1 >= 0 else float("inf")
            right = matrix[i - 1][j + 1] if j + 1 <= n - 1 else float("inf")
            matrix[i][j] = min(left, mid, right) + matrix[i][j]

    return min(matrix[-1])


print(minimum_falling_path_sum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
print(minimum_falling_path_sum([[17, 82], [1, -44]]))
print(minimum_falling_path_sum([[51, 24], [-50, 82]]))
