# https://atcoder.jp/contests/dp/tasks/dp_g

# Note: Here we can also use Khan's algorithm to find the longest path in a DAG.

import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)

dp = [-1] * n

def dfs(u):
    if dp[u] != -1:
        return dp[u]

    res = 0
    for v in graph[u]:
        res = max(res, 1 + dfs(v))

    dp[u] = res
    return res

ans = 0
for i in range(n):
    ans = max(ans, dfs(i))

print(ans)