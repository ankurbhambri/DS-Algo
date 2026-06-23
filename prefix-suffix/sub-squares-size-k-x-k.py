# https://www.geeksforgeeks.org/given-n-x-n-square-matrix-find-sum-sub-squares-size-k-x-k/

"""
Given an n x n square matrix, find sum of all sub-squares of size k x k where k is smaller than or equal to n. 

Examples : 

Input:
n = 5, k = 3
arr[][] = { {1, 1, 1, 1, 1},
            {2, 2, 2, 2, 2},
            {3, 3, 3, 3, 3},
            {4, 4, 4, 4, 4},
            {5, 5, 5, 5, 5},
         };
Output:
       18  18  18
       27  27  27
       36  36  36


Input:
n = 3, k = 2
arr[][] = { {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9},
         };
Output:
       12  16
       24  28

"""


def sum_of_submatrices_naive(matrix, k):
    """
    Naive approach: Calculate sum for each k x k submatrix
    TC: O(n^2 * k^2)
    SC: O(1)
    """
    n = len(matrix)
    if k > n:
        return []
    
    result = []
    
    # Iterate through all possible top-left corners of k x k submatrices
    for i in range(n - k + 1):
        row_sums = []
        for j in range(n - k + 1):
            # Calculate sum of current k x k submatrix
            current_sum = 0
            for x in range(i, i + k):
                for y in range(j, j + k):
                    current_sum += matrix[x][y]
            row_sums.append(current_sum)
        result.append(row_sums)

    return result


def sum_of_submatrices_prefix_sum(matrix, k):
    """
    Using 2D prefix sum array
    TC: O(n^2) for preprocessing + O(n^2) for calculation = O(n^2)
    SC: O(n^2)
    """
    n = len(matrix)
    if k > n:
        return []
    
    # Create prefix sum matrix
    prefix = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Build prefix sum matrix
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            prefix[i][j] = (
                matrix[i - 1][j - 1] +
                prefix[i - 1][j] +
                prefix[i][j - 1] -
                prefix[i - 1][j - 1]
            )

    result = []

    # Calculate sum for each k x k submatrix using prefix sum
    for i in range(n - k + 1):
        row_sums = []
        for j in range(n - k + 1):
            # Sum of submatrix from (i,j) to (i+k-1, j+k-1)
            submatrix_sum = (
                prefix[i + k][j + k] -
                prefix[i][j + k] -
                prefix[i + k][j] +
                prefix[i][j]
            )
            row_sums.append(submatrix_sum)
        result.append(row_sums)

    return result


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
k = 2
print(sum_of_submatrices_naive(matrix, k))
print(sum_of_submatrices_prefix_sum(matrix, k))

matrix = [
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]
]
k = 2

print(sum_of_submatrices_naive(matrix, k))
print(sum_of_submatrices_prefix_sum(matrix, k))