# https://atcoder.jp/contests/dp/tasks/dp_m


# Top-Down DP

import sys

# Recursion limit badhani padegi kyunki N=100 aur K=10^5 hai
sys.setrecursionlimit(200000)

# TC: O(N * K^2) - worst case, SC: O(N*K) due to memoization + recursion stack
def solve():

    N, K = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    MOD = 10**9 + 7
    
    # Memoization table: N rows aur K columns
    # -1 matlab abhi tak calculate nahi kiya
    memo = [[-1] * (K + 1) for _ in range(N)]

    def get_ways(idx, rem):

        # Base Case: Agar saare bachhe process ho gaye
        if idx == -1:
            return 1 if rem == 0 else 0
        
        # Memoization check
        if memo[idx][rem] != -1:
            return memo[idx][rem]
        
        ways = 0
        # Current bachha (idx) kitni candies le sakta hai?
        # Wo 0 se lekar apni limit (a[idx]) tak le sakta hai, 
        # lekin utni hi jitni bachi hain (rem).
        upper_limit = min(a[idx], rem)
        
        for x in range(upper_limit + 1):
            ways = (ways + get_ways(idx - 1, rem - x)) % MOD
            
        memo[idx][rem] = ways
        return ways

    # Start: Aakhri bachhe se (N-1) aur poori K candies se

    print(get_ways(N - 1, K))

# Example: get_ways(1, 3) 
# -> bachha 1 (limit 2) takes 2 candies, calls get_ways(0, 1)
# -> bachha 0 (limit 1) takes 1 candy, calls get_ways(-1, 0) -> Returns 1

# solve()

# 2D Table Approach (Without Optimization)

# Yeh O(N * K^2) hai - TLE dega bade input par
def solve_2d_basic():
    N, K = 2, 3
    a = [1, 2]
    MOD = 10**9 + 7

    # dp[bachha][candies]
    # dp[i][j] = i bachhon mein j candies baantne ke tareeke
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    
    # Base Case: 0 bachhe, 0 candy = 1 tareeka
    dp[0][0] = 1

    for i in range(1, N + 1): # Child 1 se N tak
        for j in range(K + 1): # Total candies 0 se K tak
            # Child 'i' kitni candies le sakta hai? (0 se a[i-1] tak)
            limit = a[i-1]
            for x in range(min(j, limit) + 1):
                # Agar child i ne 'x' li, toh baki bacho ne (j-x) li honi chahiye
                dp[i][j] = (dp[i][j] + dp[i-1][j-x]) % MOD

    print(dp[N][K])

# Example Dry Run (N=2, K=3, a=[1,2]):
# Child 1 (limit 1): dp[1][0]=1, dp[1][1]=1
# Child 2 (limit 2): 
#   dp[2][3] = dp[1][3] + dp[1][2] + dp[1][1]
#   dp[2][3] = 0 + 0 + 1 = 1 (Correct!)


# optimize using prefix sums to reduce inner loop to O(1)

# TC: O(N * K), SC: O(N * K)

def solve():
    # Input format: N (children), K (total candies)
    # a: List of max candies each child can take
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    k = int(input_data[1])
    a = list(map(int, input_data[2:]))

    MOD = 10**9 + 7

    # dp[j] ka matlab: "Abhi tak jitne bacho ko process kiya, 
    # unhe milakar total j candies dene ke kitne tareeke hain."
    dp = [0] * (k + 1)
    
    # Base Case: 0 bache aur 0 candy = 1 tareeka (kuch mat karo)
    dp[0] = 1 

    # Loop 1: Har ek bache (child i) ko ek-ek karke process karenge
    for i in range(n):

        new_dp = [0] * (k + 1)
        
        # --- PREFIX SUM STEP ---
        # Hum pichle state (dp array) ka prefix sum banate hain.
        # prefix_sum[x] = dp[0] + dp[1] + ... + dp[x-1]
        prefix_sum = [0] * (k + 2)
        for j in range(k + 1):
            prefix_sum[j + 1] = (prefix_sum[j] + dp[j]) % MOD
        
        # --- DP TRANSITION STEP ---

        limit = a[i]  # i-th child maximum kitni candy le sakta hai
        
        # Ab humein nikalna hai ki child 'i' ko milakar total 'j' candies kaise baantein
        for j in range(k + 1):
            # Agar humein total 'j' candies karni hain aur child 'i' max 'limit' le sakta hai,
            # toh baki bacho (dp) ne [j - limit] se lekar [j] candies li honi chahiye.
            # Example: j=5, limit=2 -> baki bache 3, 4, ya 5 candies le sakte hain.
            
            lower = max(0, j - limit)
            upper = j
            
            # Range Sum Formula: Sum of dp[lower...upper] 
            # Is equal to: prefix_sum[upper + 1] - prefix_sum[lower]
            count = (prefix_sum[upper + 1] - prefix_sum[lower]) % MOD
            new_dp[j] = count
            
        # Current result ko update kar dete hain agli iteration (agle bache) ke liye
        dp = new_dp

    # Final Answer: N bacho mein K candies baantne ke tareeke
    print(dp[k])

if __name__ == "__main__":
    solve()