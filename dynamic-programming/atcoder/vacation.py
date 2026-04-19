# https://atcoder.jp/contests/dp/tasks/dp_c


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
