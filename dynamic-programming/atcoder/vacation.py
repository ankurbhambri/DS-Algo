# https://atcoder.jp/contests/dp/tasks/dp_c

# Similar to paint house problem, but here we have only 3 activities and we want to maximize the points instead of minimizing the cost.

N = int(input())

dp = [[0] * 3 for _ in range(N)]

for i in range(N):

    a, b, c = map(int, input().split())

    if i == 0:
        dp[i][0] = a
        dp[i][1] = b
        dp[i][2] = c

    else:
        # idea here is to add the current value to the maximum of the previous day for the other two activities.
        dp[i][0] = a + max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = b + max(dp[i-1][0], dp[i-1][2])
        dp[i][2] = c + max(dp[i-1][0], dp[i-1][1])

print(max(dp[N-1]))


# O(1) space optimization

N = int(input())

dp = [0, 0, 0]

for _ in range(N):

    a, b, c = map(int, input().split())

    dp0 = a + max(dp[1], dp[2])
    dp1 = b + max(dp[0], dp[2])
    dp2 = c + max(dp[0], dp[1])

    dp = [dp0, dp1, dp2]

print(max(dp))