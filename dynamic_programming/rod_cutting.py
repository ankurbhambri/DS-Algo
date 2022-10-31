# https://practice.geeksforgeeks.org/problems/rod-cutting0840/1

def cutRod_memo(price, N):
    memo = {}
    def solve(cl, rl):
        if rl == 0 or cl == 0:
            return 0
        elif (cl, rl) in memo:
            return memo[(cl, rl)]
        else:
            val = price[cl - 1]
            if cl <= rl:
                c1 = val + solve(cl, rl - cl)
                c2 = solve(cl - 1, rl)
                c = max(c1, c2)
            else:
                c = solve(cl - 1, rl)
            memo[(cl, rl)] = c
            return c
        
    return solve(N, N)

def cutRod_iterative(price, n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        ans = 0
        for j in range(1, i + 1):
            ans = max(ans, price[j - 1] + dp[i - j])
        dp[i] = ans
    return dp[n]
