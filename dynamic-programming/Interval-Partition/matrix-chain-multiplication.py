# https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1

'''
    Matrix multiplication is associative, that means the order of multiplication does not change the result, 
    but it does affect the number of operations required to compute the product.

    The problem is to find the most efficient way to multiply a given sequence of matrices.
    
    The goal is to minimize the total number of scalar multiplications needed to compute the product of the matrices.

    The input is an array where the ith matrix has dimensions arr[i - 1] x arr[i].

    Such as, for matrices A, B, C with dimensions 10 x 20, 20 x 30, and 30 x 40 respectively, the input would be [10, 20, 30, 40].
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
                solve(k + 1, j) +
                arr[i-1] * arr[k] * arr[j]
            )

            min_cost = min(min_cost, cost)

        memo[(i, j)] = min_cost
        return memo[(i, j)]

    # Solve for full chain multiplication from matrix 1 to n-1
    return solve(1, n-1)

# Here, matrix dimensions are given as an array where the ith matrix has dimensions arr[i-1] x arr[i].
# print(matrix_chain_order([10, 15, 20, 30]))  # Output: 8000


# Bottom-Up memo (iterative + tabulation) approach
def matrix_chain_order(arr):

    n = len(arr)

    # dp[i][j] will hold the min number of multiplications needed for matrices i through j
    dp = [[0 for _ in range(n)] for _ in range(n)]

    '''
        length represents how many metrics we can multiply together

        length = 1 means single matrix, no multiplication needed

        length = 2 means two matrices, we can multiply them directly

        n - 1 because we are considering matrices from 1 to n - 1 , arr = [10, 30, 5, 60] n = 4

        So, we have 3 matrices: A1: 10 x 30, A2: 30 x 5, A3: 5 x 60

        So, for arr = [10, 15, 20, 30], n = 4, we have 3 matrices:
            A1: 10 x 15
            A2: 15 x 20
            A3: 20 x 30
    '''

    for length in range(2, n):  # length = 2 becuase we need at least two matrices to perform a multiplication

        # i loop goes from 0 to n - length because we are considering sub-chains of matrices starting at index i
        # and ending at index j = i + length - 1, and we don't want j to go out of bounds

        for i in range(n - length + 1):

            j = i + length - 1

            dp[i][j] = float('inf')

            for k in range(i, j):

                '''
                Dimensions Array (arr[]) kaise kaam karta hai?
                
                MCM problem mein humein matrices ki dimensions ek single array mein di jati hain.
                Agar arr = [10, 20, 30, 40], iska matlab hamare paas 3 matrices hain:
                    - Matrix A1: 10 x 20 (i.e., arr[0] x arr[1])
                    - Matrix A2: 20 x 30 (i.e., arr[1] x arr[2])
                    - Matrix A3: 30 x 40 (i.e., arr[2] x arr[3])

                arr[i-1] x arr[k] x arr[j] ka logic:

                Jab hum matrices ki chain ko k point par split karte hain:
                    - Left Side (Ai ... Ak): Isko multiply karke jo ek final matrix banega, uska size hoga arr[i-1] x arr[k].
                    - Right Side (Ak+1 ... Aj): Isko multiply karke jo ek final matrix banega, uska size hoga arr[k] x arr[j].
                
                Ab in dono final matrices ko aapas mein multiply karne ki cost kya hogi?
                Cost = (Row of Left) x (Common Dimension) x (Col of Right)
                Cost = arr[i-1] x arr[k] x arr[j]
                
                Example Dry Run:
                Maan lijiye hum (A1 * A2) * A3 kar rahe hain:
                    - Chain range: i=1, j=3
                    - Humne split kiya k=2 par (yaani (A1, A2) ek saath aur A3 alag).
                    - Left Part (A1, A2): Iska result matrix hoga 10 x 30 (Row of A1, Col of A2).
                    - Right Part (A3): Iska result matrix hai 30 x 40.
                    - Final Multiplication: 10 x 30 x 40.
                    - arr[i-1] = arr[0] = 10
                    - arr[k] = arr[2] = 30
                    - arr[j] = arr[3] = 40
                
                Yeh formula har partition par lagta hai taaki hum check kar sakein ki kis k par divide karne se sabse sasta 
                (minimum) cost pad raha hai. Kya ab dimensions ka array aur yeh formula ka link clear hua?
                '''

                cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n - 1]


print(matrix_chain_order([10, 15, 20, 25]))  # Output: 8000


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

    for length in range(2, n):

        for i in range(n - length + 1):

            j = i + length - 1

            dp[i][j] = float('inf')

            for k in range(i, j):

                cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]

                if cost < dp[i][j]:
                    dp[i][j] = cost
                    s[i][j] = k
    return dp, s

# TC: O(n^2) and SC: O(n)
def build_parenthesis(s, i, j, result=[]):

    # result list ko use kar rahe hain taaki recursive calls ke through
    # parenthesis ko build kar sakein. Base case me agar i==j hai
    # matlab ek hi matrix hai, toh uska naam append kar do.
    # Agar i!=j hai, toh hum split point k lete hain aur recursively
    # left aur right sub-chains ke liye parenthesis build karte hain.
    # Har recursive call ke start me "(" append karte hain aur end me ")"
    # append karte hain taaki proper parenthesization ban sake.

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