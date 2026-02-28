# https://open.kattis.com/problems/magicalcows

import sys

def solve():
    # Read C (capacity), N (initial farms), M (queries)
    line1 = sys.stdin.readline().split()
    if not line1: return
    C, N, M = map(int, line1)
    
    # dp[day][cows_in_farm]
    # Max days is usually 50 based on problem constraints
    max_days = 51
    dp = [[0] * (C + 1) for _ in range(max_days)]
    
    # Initial state (Day 0)
    for _ in range(N):
        cows = int(sys.stdin.readline())
        dp[0][cows] += 1
        
    # Fill DP table
    for d in range(max_days - 1):
        for i in range(1, C + 1):
            if dp[d][i] == 0:
                continue
            
            if i * 2 <= C:
                # Cows double, stay in one farm
                dp[d+1][i*2] += dp[d][i]
            else:
                # Farm splits into two farms with 'i' cows each
                dp[d+1][i] += 2 * dp[d][i]
                
    # Answer queries
    for _ in range(M):
        query_day = int(sys.stdin.readline())
        print(sum(dp[query_day]))

solve()