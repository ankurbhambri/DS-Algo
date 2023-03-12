# same as Minimum falling path sum

# https://www.codingninjas.com/codestudio/problems/maximum-path-sum-in-the-matrix_797998

# space optimization
def getMaxPathSum(matrix):
    m, n = len(matrix), len(matrix[0])
    prev = matrix[0]
    for i in range(1, m):
        tmp = [0] * n
        for j in range(n):
            up = matrix[i][j] + prev[j]
            left_up = matrix[i][j] + (prev[j - 1] if j - 1 >= 0 else float("-inf"))
            right_up = matrix[i][j] + (prev[j + 1] if j + 1 < n else float("-inf"))
            tmp[j] = max(up, left_up, right_up)
        prev = tmp
    return max(prev)
