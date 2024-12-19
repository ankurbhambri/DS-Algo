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


def sum_of_sub_squares(arr, k):

    n = len(arr)
    prefix_sum = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            prefix_sum[i][j] = arr[i][j]
            if i > 0:
                prefix_sum[i][j] += prefix_sum[i - 1][j]
            if j > 0:
                prefix_sum[i][j] += prefix_sum[i][j - 1]
            if i > 0 and j > 0:
                prefix_sum[i][j] -= prefix_sum[i - 1][j - 1]

    result = []
    for i in range(k - 1, n):
        row = []
        for j in range(k - 1, n):
            total = prefix_sum[i][j]
            if i >= k:
                total -= prefix_sum[i - k][j]
            if j >= k:
                total -= prefix_sum[i][j - k]
            if i >= k and j >= k:
                total += prefix_sum[i - k][j - k]
            row.append(total)
        result.append(row)

    return result


arr = [
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5],
]
print(sum_of_sub_squares(arr, 4))

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(sum_of_sub_squares(arr, 2))
