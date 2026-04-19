# https://atcoder.jp/contests/dp/tasks/dp_k


n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [False] * (k + 1)

for i in range(1, k + 1):
    for x in a:
        if i - x >= 0 and dp[i - x] == False:
            dp[i] = True
            break

print("First" if dp[k] else "Second")