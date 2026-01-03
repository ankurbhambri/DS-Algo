'''
There are N coins valued (0 to N - 1).
Calculate no. of ways to select K coins such that their sum is divisible by M.

Return answer modulo 1e9 + 7.

    int solve(int N, int M, int K)

Input:
4 2 2
Output: 2

'''

# Here the idea is similar to classic Knapsack problem where we have to select K items (coins here) such that their sum % M == 0.
# We will use a 2D DP array where dp[j][r] represents number of ways to choose j coins such that their sum % M == r.
# We will iterate through each coin value and update the DP table accordingly.

def solve(N, M, K):
    MOD = 10**9 + 7

    # dp[j][r] = number of ways to choose j coins
    # such that sum % M == r
    dp = [[0] * M for _ in range(K + 1)]
    dp[0][0] = 1

    for val in range(N):          # coin values: 0 to N-1
        for j in range(K, 0, -1): # reverse to avoid reuse
            for r in range(M):
                new_r = (r + val) % M
                dp[j][new_r] = (dp[j][new_r] + dp[j - 1][r]) % MOD

    return dp[K][0]

print(solve(4, 2, 2))  # Output: 2