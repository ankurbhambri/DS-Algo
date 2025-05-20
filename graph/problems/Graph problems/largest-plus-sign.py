def orderOfLargestPlusSign(n, mines):

    if n == 0:
        return 0
    if n == 1:
        return 0 if mines else 1

    # Initialize the grid with all ones (1s)
    grid = [[1] * n for _ in range(n)]
    
    # Set mines to zero
    for i, j in mines:
        grid[i][j] = 0

    # Create four matrices for the 4 directions (left, right, up, down)
    left = [[0] * n for _ in range(n)]
    right = [[0] * n for _ in range(n)]
    up = [[0] * n for _ in range(n)]
    down = [[0] * n for _ in range(n)]
    
    # Fill the matrices
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                left[i][j] = left[i][j - 1] + 1 if j > 0 else 1
                up[i][j] = up[i - 1][j] + 1 if i > 0 else 1

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if grid[i][j] != 0:
                right[i][j] = right[i][j + 1] + 1 if j < n - 1 else 1
                down[i][j] = down[i + 1][j] + 1 if i < n - 1 else 1
    
    # Calculate the largest plus sign order
    res = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                order = min(left[i][j], right[i][j], up[i][j], down[i][j])
                res = max(res, order)

    return res


# [
#     [[1, 1, 1], [1, 2, 1], [1, 3, 1], [1, 4, 1], [1, 5, 1]], 
#     [[1, 1, 2], [1, 2, 2], [1, 3, 2], [1, 4, 2], [1, 5, 2]], 
#     [[1, 1, 3], [1, 2, 3], [1, 3, 3], [1, 4, 3], [1, 5, 3]], 
#     [[1, 1, 4], [1, 2, 4], [1, 3, 4], [1, 4, 4], [1, 5, 4]], 
#     [[1, 1, 5], [1, 2, 5], [0, 0, 0], [1, 1, 5], [1, 2, 5]]
# ]


print(orderOfLargestPlusSign(5, [[4, 2]]))  # 2
print(orderOfLargestPlusSign(1, []))  # 1