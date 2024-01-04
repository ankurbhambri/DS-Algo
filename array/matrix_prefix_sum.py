"""
    Explanation of the Prefix Sum Formula:
    
    In the context of the prefix sum computation for cell (i, j):

    prefix[i][j] represents the cumulative sum of the sub-matrix from (0, 0) to (i, j) in the original matrix arr.
    prefix[i - 1][j] is the sum of elements above the current cell (i, j).
    prefix[i][j - 1] is the sum of elements to the left of the current cell (i, j).
    prefix[i - 1][j - 1] represents the sum of the overlapping region.
    arr[i - 1][j - 1] denotes the current cell's value in the original matrix arr.
    
    Breaking Down the Formula:

    prefix[i - 1][j] and prefix[i][j - 1] are the sum of elements above and to the left of cell (i, j).
    prefix[i - 1][j - 1] is subtracted because it's included twice in the sum of prefix[i - 1][j] and prefix[i][j - 1] and shouldn't be counted twice in the sum.
    arr[i - 1][j - 1] adds the value of the current cell (i, j) in the original matrix to the prefix sum, effectively updating the cumulative sum for the current cell.
    
    Addressing the 'Top-Left' Corner:
    
    In this context, (0, 0) refers to the top-left corner of the matrix. However, in the code, it's shifted to (1, 1) as the prefix sum matrix is 1-indexed.
    Adjustments with -1 are made when accessing elements in the original matrix arr because arrays/lists in Python are 0-indexed.
    
    This formula combines the sum of elements from above, to the left, and the top-left corner, ensuring the correct accumulation of sums for each cell (i, j) in the prefix sum matrix.
"""


def compute_prefix_sum(arr):
    rows = len(arr)
    cols = len(arr[0]) if rows > 0 else 0

    # Initialize a prefix sum matrix with zeros
    prefix = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

    # Calculate the prefix sum
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            # Calculate the prefix sum for each cell
            prefix[i][j] = (
                prefix[i - 1][j]
                + prefix[i][j - 1]
                - prefix[i - 1][j - 1]
                + arr[i - 1][j - 1]
            )

    return prefix


# Example matrix
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Compute the prefix sum of the matrix
prefix_sum = compute_prefix_sum(arr)

# Display the prefix sum matrix
for row in prefix_sum:
    print(row)
