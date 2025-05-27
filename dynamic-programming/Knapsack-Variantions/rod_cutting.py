# https://practice.geeksforgeeks.org/problems/rod-cutting0840/1


# TC = O(n^2)
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


# TC = O(n ^ 2)
def rod_cutting_dp(prices, n):
    dp = [0] * (n + 1)  # Initialize DP array

    for i in range(1, n + 1):
        max_profit = 0
        for j in range(1, i + 1):
            max_profit = max(max_profit, prices[j - 1] + dp[i - j])
        dp[i] = max_profit

    return dp[n]


print(cutRod_memo([1, 5, 8, 9, 10, 17, 17, 20], 8))
print(rod_cutting_dp([1, 5, 8, 9, 10, 17, 17, 20], 8))
