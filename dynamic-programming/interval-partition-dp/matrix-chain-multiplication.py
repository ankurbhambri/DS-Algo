# https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1

'''
    Matrix multiplication is associative, that means the order of multiplication does not change the result, but it does affect the number of operations required to compute the product.

    The problem is to find the most efficient way to multiply a given sequence of matrices.
    
    The goal is to minimize the total number of scalar multiplications needed to compute the product of the matrices.

    The input is an array where the ith matrix has dimensions arr[i - 1] x arr[i].

    Such as for matrices A, B, C with dimensions 10 x 20, 20 x 30, and 30 x 40 respectively, the input would be [10, 20, 30, 40].

'''

# O(n^3) Time Complexity and O(n^2) Space Complexity

# top-down memoization approach (recursive + memoization)
def matrix_chain_order(arr):

    n = len(arr)

    # dp[i][j] represents minimum cost to multiply matrices from i to j
    memo = {}

    def solve(i, j):

        # Base case: only one matrix
        if i == j:
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        min_cost = float('inf')

        # Try all possible positions to split the chain
        for k in range(i, j):
            cost = (
                solve(i, k) +
                solve(k+1, j) +
                arr[i-1] * arr[k] * arr[j]
            )

            min_cost = min(min_cost, cost)

        memo[(i, j)] = min_cost
        return memo[(i, j)]

    # Solve for full chain multiplication from matrix 1 to n-1
    return solve(1, n-1)

# Here, matrix dimensions are given as an array where the ith matrix has dimensions arr[i-1] x arr[i].
print(matrix_chain_order([10, 20, 30, 40]))  # Output: 18000


# Bottom-Up memo (iterative + tabulation) approach
def matrix_chain_order(arr):

    n = len(arr)

    # dp[i][j] will hold the min number of multiplications needed for matrices i through j
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    # l represents length of the matrix sub-chain, means how many metrics we can multiply together
    # l = 1 means single matrix, no multiplication needed
    # l = 2 means two matrices, we can multiply them directly

    # n-1 because we are considering matrices from 1 to n-1 , arr = [10, 30, 5, 60] n = 4  # So, we have 3 matrices: A1: 10 x 30, A2: 30 x 5, A3: 5 x 60

    for l in range(2, n):  # l = 2 to n-1

        for i in range(1, n - l + 1):

            '''
                n - L + 1 ka logic sirf ye ensure karne ke liye hai ki aapka loop matrix ki boundary ke bahar na nikal jaye.

                j is the end index of the sub-chain

                For example:-
                    i = 1, l = 2 ,,,,,,,,,,, j = i + l - 1 = 1 + 2 - 1 = 2 ,,,,,,,,,,,, So we're multiplying matrices from index 1 to 2 → (A1, A2)
                    i = 2, l = 2 ,,,,,,,,,,, j = 2 + 2 - 1 = 3 ,,,,,,,,,,,,,,,,,,,,,,,, Matrices from A2 to A3
                    i = 3, l = 2 ,,,,,,,,,,, j = 3 + 2 - 1 = 4 ,,,,,,,,,,,,,,,,,,,,,,,, Matrices from A3 to A4
            '''

            j = i + l - 1

            dp[i][j] = float('inf')

            for k in range(i, j):

                cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n - 1]

dimensions = [10, 20, 30, 40]
print(matrix_chain_order(dimensions))  # Output: 18000


# Follow-up: Parenthesization reconstruction

'''
    Parenthesization reconstruction means find optimal parenthesization, i.e., where to place brackets to minimize multiplication cost.

    To reconstruct the optimal parenthesization, we can maintain a separate table to store the split points (k values) for each sub-chain.

    We will maintain an auxiliary table s[i][j] which stores index k where the split happened to get the optimal cost for multiplying matrices from i to j.

'''
# TC: O(n^3) and SC: O(n^2)
def parenthesization_reconstruction(arr):

    n = len(arr)

    dp = [[0] * n for _ in range(n)]

    # why s[i][j] = k? Because we want to know where to split the chain of matrices to achieve the optimal cost. 
    # The value of k indicates the index at which we split the matrices from i to j.
    s = [[0] * n for _ in range(n)]

    for l in range(2, n):
        for i in range(1, n - l + 1):

            j = i + l - 1

            dp[i][j] = float('inf')

            for k in range(i, j):

                cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]

                if cost < dp[i][j]:
                    dp[i][j] = cost
                    s[i][j] = k
    return dp, s

# TC: O(n^2) and SC: O(n)
def build_parenthesis(s, i, j, result=[]):

    if i == j:
        result.append(f"A{i}")
        return

    result.append("(")
    k = s[i][j]
    build_parenthesis(s, i, k, result)
    build_parenthesis(s, k + 1, j, result)

    result.append(")")

    return "".join(result)


arr = [10, 20, 30, 40]
dp, s = parenthesization_reconstruction(arr)

print("Min Cost:", dp[1][len(arr)-1])
print("Optimal Parenthesization:", build_parenthesis(s, 1, len(arr)-1))