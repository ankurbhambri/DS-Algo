def compute_prefix_sum(matrix):

    rows, cols = len(matrix), len(matrix[0])
    prefix_sum = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            prefix_sum[i][j] = matrix[i][j]
            if i > 0:
                prefix_sum[i][j] += prefix_sum[i - 1][j]
            if j > 0:
                prefix_sum[i][j] += prefix_sum[i][j - 1]
            if i > 0 and j > 0:
                prefix_sum[i][j] -= prefix_sum[i - 1][j - 1]

    return prefix_sum


def query_submatrix_sum(prefix_sum, r1, c1, r2, c2):
    total = prefix_sum[r2][c2]
    print(
        total,
        prefix_sum[r1 - 1][c2],
        prefix_sum[r1][c2 - 1],
        prefix_sum[r1 - 1][c1 - 1],
    )
    if r1 > 0:
        total -= prefix_sum[r1 - 1][c2]
    if c1 > 0:
        total -= prefix_sum[r2][c1 - 1]
    if r1 > 0 and c1 > 0:
        total += prefix_sum[r1 - 1][c1 - 1]
    return total


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

prefix_sum = compute_prefix_sum(matrix)

# Query the sum of submatrix from (1, 1) to (2, 2)
result = query_submatrix_sum(prefix_sum, 1, 1, 2, 2)
print("Submatrix sum:", result)  # Output: 28
