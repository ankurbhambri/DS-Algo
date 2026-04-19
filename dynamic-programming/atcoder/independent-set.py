# http://atcoder.jp/contests/dp/tasks/dp_p


import sys
sys.setrecursionlimit(10**7)

MOD = 10**9 + 7

n = int(input())
adj = [[] for _ in range(n + 1)]

# edges input
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# dp[u][0] = u white
# dp[u][1] = u black
dp = [[0, 0] for _ in range(n + 1)]

def dfs(u, parent):
    dp[u][0] = 1
    dp[u][1] = 1

    for v in adj[u]:
        if v == parent:
            continue

        dfs(v, u)

        # u black → v must be white
        dp[u][1] = (dp[u][1] * dp[v][0]) % MOD

        # u white → v can be white or black
        dp[u][0] = (dp[u][0] * (dp[v][0] + dp[v][1])) % MOD

# root at node 1
dfs(1, -1)

# final answer
print((dp[1][0] + dp[1][1]) % MOD)