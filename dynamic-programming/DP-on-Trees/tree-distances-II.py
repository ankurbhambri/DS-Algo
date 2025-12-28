# https://cses.fi/problemset/task/1133/

import sys

# Simple dp rerooting approach to find sum of distances from each node to all other nodes in tree

def solve():
    # Fast I/O
    input = sys.stdin.read().split()
    if not input:
        return
    
    n = int(input[0])
    adj = [[] for _ in range(n + 1)]
    
    ptr = 1
    for _ in range(n - 1):
        u = int(input[ptr])
        v = int(input[ptr+1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2

    sub = [0] * (n + 1)
    dp = [0] * (n + 1)
    ans = [0] * (n + 1)

    # Pehla DFS: Subtree size aur root (1) ke liye distances calculate karna
    def dfs1(u, p):
        sub[u] = 1
        current_dp = 0
        for v in adj[u]:
            if v == p:
                continue
            dfs1(v, u)
            sub[u] += sub[v]
            current_dp += dp[v] + sub[v]
        dp[u] = current_dp

    # Doosra DFS: Rerooting logic (Parent se child par answer shift karna)
    def dfs2(u, p):
        for v in adj[u]:
            if v == p:
                continue
            # Logic: Jab hum u se v par move karte hain:
            # v ke subtree waale nodes 1 kadam paas aa jate hain (-sub[v])
            # Baaki saare nodes (n - sub[v]) 1 kadam door chale jate hain
            ans[v] = ans[u] - sub[v] + (n - sub[v])
            dfs2(v, u)

    # Execution
    dfs1(1, 0)
    ans[1] = dp[1]
    dfs2(1, 0)

    # Output print karna
    print(*(ans[1:]))

# Run the function
if __name__ == "__main__":
    solve()