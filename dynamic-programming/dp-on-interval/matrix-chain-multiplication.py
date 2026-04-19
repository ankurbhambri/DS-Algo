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

'''

Follow-Up Questions:

    Can you solve it using Bottom-Up memo?
    → Yes, by filling the DP table diagonally.

    Can you return the optimal parenthesis sequence as well?
    → You'd maintain a separate bracket[i][j] to store the optimal k.

    Why is greedy not applicable here?
    → Because local optimal multiplication order doesn't guarantee global optimality.

'''

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
                j is the end index of the sub-chain

                For example:-
                    i = 1, l = 2 ,,,,,,,,,,, j = i + l - 1 = 1 + 2 - 1 = 2 ,,,,,,,,,,,, So we're multiplying matrices from index 1 to 2 → (A1, A2)
                    i = 2, l = 2 ,,,,,,,,,,, j = 2 + 2 - 1 = 3 ,,,,,,,,,,,,,,,,,,,,,,,, Matrices from A2 to A3
                    i = 3, l = 2 ,,,,,,,,,,, j = 3 + 2 - 1 = 4 ,,,,,,,,,,,,,,,,,,,,,,,, Matrices from A3 to A4
            '''

            j = i + l - 1

            dp[i][j] = float('inf')
            
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + arr[i-1] * arr[k] * arr[j]

                if cost < dp[i][j]:
                    dp[i][j] = cost
                    
    return dp[1][n-1]


dimensions = [10, 20, 30, 40]
print(matrix_chain_order(dimensions))  # Output: 18000



'''
    Parenthesization reconstruction means find optimal parenthesization, i.e., where to place brackets to minimize multiplication cost.

    To reconstruct the optimal parenthesization, we can maintain a separate table to store the split points (k values) for each sub-chain.

    We will maintain an auxiliary table s[i][j] which stores index k where the split happened to get the optimal cost for multiplying matrices from i to j.

'''

def matrix_chain_order(arr):

    n = len(arr)

    dp = [[0] * n for _ in range(n)]

    s = [[0] * n for _ in range(n)]  # stores split index

    for l in range(2, n):  # l = chain length

        for i in range(1, n - l + 1):

            j = i + l - 1

            dp[i][j] = float('inf')

            for k in range(i, j):

                cost = dp[i][k] + dp[k+1][j] + arr[i-1] * arr[k] * arr[j]

                if cost < dp[i][j]:
                    dp[i][j] = cost
                    s[i][j] = k  # remember split point

    return dp, s

# Function to print the optimal parenthesization
def print_parenthesis(s, i, j):
    if i == j:
        return f"A{i}"

    else:

        k = s[i][j] # k is the split point where we split the chain to get optimal cost

        '''
            Recursively print the left and right parts

            left part is from i to k, right part is from k+1 to j

            A[i] x A[k+1] is the multiplication of two matrices. So, we need to print the left and right parts recursively

            if s[i][j] = k, then we have A[i] x (A[k+1] x A[j]) ,,,,,,,,,, This means we need to print the left part from i to k and right part from k+1 to j. This will give us the optimal parenthesization

            Example: if s[1][3] = 2, then we have A[1] x (A[2] x A[3]),,,,,, This means we need to print the left part from 1 to 2 and right part from 3 to 3
            Example: if s[1][4] = 3, then we have A[1] x (A[2] x (A[3] x A[4])) ,,,,,,,, This means we need to print the left part from 1 to 3 and right part from 4 to 4

        '''

        left = print_parenthesis(s, i, k)
        right = print_parenthesis(s, k + 1, j)

        return f"({left} x {right})"


arr = [10, 30, 5, 60]

dp, s = matrix_chain_order(arr)

expr = print_parenthesis(s, 1, len(arr) - 1)

print("Optimal Parenthesization:", expr)
print("Minimum Cost:", dp[1][len(arr) - 1])
