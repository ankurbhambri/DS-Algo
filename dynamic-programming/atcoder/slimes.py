# https://atcoder.jp/contests/dp/tasks/dp_n

# Top-Down DP

import sys

# Python mein recursion depth limit badhani padti hai
sys.setrecursionlimit(2000)

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    # Prefix sum for fast range sum calculation
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i+1] = pref[i] + a[i]

    # Memoization table: -1 matlab abhi calculate nahi kiya
    memo = [[-1] * n for _ in range(n)]

    def get_min_cost(i, j):
        # Base case: single slime
        if i == j:
            return 0
        
        # Check if already calculated
        if memo[i][j] != -1:
            return memo[i][j]
        
        res = float('inf')
        current_range_sum = pref[j+1] - pref[i]
        
        # Har possible split point 'k' ko try karein
        for k in range(i, j):
            # Left subproblem + Right subproblem + is merge ki cost
            total = get_min_cost(i, k) + get_min_cost(k+1, j) + current_range_sum
            if total < res:
                res = total
        
        memo[i][j] = res
        return res

    print(get_min_cost(0, n - 1))

solve()


# 2D Table Approach (Without Optimization)

import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    # Prefix Sum for O(1) range sum queries
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i+1] = pref[i] + a[i]

    # DP table initialized with a large value
    dp = [[0] * n for _ in range(n)]

    # l is the length of the interval
    for length in range(2, n + 1): 
        for i in range(n - length + 1):

            j = i + length - 1
            res = float('inf')
            
            # Current range sum
            current_sum = pref[j+1] - pref[i]
            
            # Try splitting the range at every possible k
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + current_sum
                if cost < res:
                    res = cost
            
            dp[i][j] = res

    print(dp[0][n-1])

solve()