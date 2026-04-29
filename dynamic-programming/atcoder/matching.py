# https://atcoder.jp/contests/dp/tasks/dp_o

import sys

def solve():
    # Input handling
    n = int(sys.stdin.readline())
    adj = []
    for _ in range(n):
        adj.append(list(map(int, sys.stdin.readline().split())))

    MOD = 10**9 + 7
    
    # DP array of size 2^n
    # dp[mask] stores the number of ways to match the first 'k' men 
    # with the women represented by the set bits in 'mask'
    dp = [0] * (1 << n)
    dp[0] = 1
    
    # Iterate through every possible mask
    for mask in range((1 << n)):
        # k is the index of the man we are currently matching
        # bin(mask).count('1') tells us how many men have already been assigned
        k = bin(mask).count('1')
        
        # We try to match man 'k' with every woman 'j'
        for j in range(n):
            # If man 'k' is compatible with woman 'j' 
            # AND woman 'j' is not already in the mask
            if adj[k][j] == 1 and not (mask & (1 << j)):
                new_mask = mask | (1 << j)
                dp[new_mask] = (dp[new_mask] + dp[mask]) % MOD
                
    # The answer is when all N women are matched (mask with all 1s)
    print(dp[(1 << n) - 1])

solve()