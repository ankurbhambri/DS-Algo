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


def func(arr, k):
    r, c = len(arr), len(arr[0])

    prefix_sum = [[0] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            prefix_sum[i][j] = arr[i][j]
            if j > 0:
                prefix_sum[i][j] += prefix_sum[i][j - 1]
            if i > 0:
                prefix_sum[i][j] += prefix_sum[i - 1][j]
            if i > 0 and j > 0:
                prefix_sum[i][j] -= prefix_sum[i - 1][j - 1]

    res = []
    for i in range(k - 1, r):
        for j in range(k - 1, c):
            a = (
                prefix_sum[i][j]
                - prefix_sum[i - 1][j]
                - prefix_sum[i][j - 1]
                + prefix_sum[i - 1][j - 1]
            )
        res.append(a)

    return res


# [[1, 3, 6], [5, 12, 21], [12, 27, 45]]

print(func([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2))  # [[12, 16], [24, 28]]
