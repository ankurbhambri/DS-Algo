"""
    Given an n x n square matrix, find sum of all sub-squares of size k x k where k is smaller than or equal to n.
    https://www.geeksforgeeks.org/given-n-x-n-square-matrix-find-sum-sub-squares-size-k-x-k/

    - prefix[i][j]: Represents the prefix sum at index (i, j) in the prefix sum matrix.
    - prefix[i-1][j]: Prefix sum of the element above the current element.
    - prefix[i][j-1]: Prefix sum of the element to the left of the current element.
    - prefix[i-1][j-1]: Common prefix sum shared by the above two elements (avoiding double counting).
    - arr[i-1][j-1]: Current element's value in the input matrix.
"""


def sumOfKxKMatrices(arr: list, k: int):
    n = len(arr)

    ans = [[0] * (n - k + 1) for i in range(n - k + 1)]

    prefix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Compute the prefix sum using the formula
            prefix[i][j] = (
                prefix[i - 1][j]
                + prefix[i][j - 1]
                - prefix[i - 1][j - 1]
                + arr[i - 1][j - 1]
            )
    # Calculate the sum of sub-squares of size k x k
    for i in range(1, n - k + 2):
        for j in range(1, n - k + 2):
            # Use prefix sums to find the sum of elements within each sub-square
            ans[i - 1][j - 1] = (
                prefix[i + k - 1][j + k - 1]
                - prefix[i - 1][j + k - 1]
                - prefix[i + k - 1][j - 1]
                + prefix[i - 1][j - 1]
            )

    return ans


print(
    sumOfKxKMatrices(
        [
            [1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3],
            [4, 4, 4, 4, 4],
            [5, 5, 5, 5, 5],
        ],
        3,
    )
)
print(sumOfKxKMatrices([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2))


print(sumOfKxKMatrices([[8, 1, 3], [2, 9, 3], [0, 3, 5]], 2))
