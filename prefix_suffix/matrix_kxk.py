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


def sum_of_sub_squares(arr, n, k):

    # Step 1: Create a 1-based prefix sum matrix
    prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            prefix_sum[i][j] = (
                arr[i - 1][j - 1]  # Access the original array using 0-based indexing
                + prefix_sum[i - 1][j]
                + prefix_sum[i][j - 1]
                - prefix_sum[i - 1][j - 1]
            )

    # Step 2: Calculate sums of k x k sub-squares
    result = []
    for i in range(1, n - k + 2):  # Loop over valid top-left corners (1-based)
        row_result = []
        for j in range(1, n - k + 2):

            bottom = i + k - 1
            right = j + k - 1

            # Use inclusion-exclusion to compute sub-square sum
            # sum of subgrid = prefix_sum[bottom][right] − prefix_sum[top − 1][right] − prefix_sum[bottom][left − 1]+prefix_sum[top − 1][left − 1]
            print(
                prefix_sum[bottom][right],
                prefix_sum[i - 1][right],
                prefix_sum[bottom][j - 1],
                prefix_sum[i - 1][j - 1],
            )
            sub_square_sum = (
                prefix_sum[bottom][right]
                - prefix_sum[i - 1][right]
                - prefix_sum[bottom][j - 1]
                + prefix_sum[i - 1][j - 1]
            )
            row_result.append(sub_square_sum)

        result.append(row_result)

    return result


# Example Usage
arr1 = [
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5],
]
n1, k1 = 5, 3
print(sum_of_sub_squares(arr1, n1, k1))

arr2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n2, k2 = 3, 2
print(sum_of_sub_squares(arr2, n2, k2))
