# unlimited supply of values in comparision of knapsack problem

def unbounded_knapSack_memo(N, W, val, wt):
    memo = {}
    def helper(n, cap):
        if n == 0 or cap == 0:
            return 0
        elif (n, cap) in memo:
            return memo[(n, cap)]
        else:
            cw = wt[n - 1]
            cv = val[n - 1]
            if cw <= cap:
                c1 = cv + helper(n, cap - cw)
                c2 = helper(n - 1, cap)
                c = max(c1, c2)
            else:
                c = helper(n - 1, cap)
            memo[(n, cap)] = c
            return c
        
    return helper(N, W)
    
# Bottom Up iterative or tabulation approach
# TC: O(N * W)
# Space: O(W)
def unbounded_knapSack_iterative(n, W, val, wt):

    dp = [0] * (W + 1)
    for i in range(n):
        for w in range(W + 1):
            cv, cw = val[i], wt[i]
            if cw <= w:
                dp[w] = max(dp[w], dp[w - cw] + cv)
    return dp[W]


N = 4
W = 8
val = [1, 4, 5, 7]
wt = [1, 3, 4, 5]
print(unbounded_knapSack_memo(N, W, val, wt), unbounded_knapSack_iterative(N, W, val, wt))
