# https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1


def matrix_chain_order(p):

    n = len(p) - 1  # Number of matrices
    m = [[0] * n for _ in range(n)]  # DP table to store minimum costs

    # l is the chain length
    for l in range(2, n + 1):  # l = 2 to n
        for i in range(n - l + 1):

            j = i + l - 1
            m[i][j] = float("inf")

            for k in range(i, j):
                # Compute cost of splitting at k
                cost = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if cost < m[i][j]:
                    m[i][j] = cost

    return m[0][n - 1]


dimensions = [10, 20, 30, 40]
print(matrix_chain_order(dimensions))  # Output: 18000
