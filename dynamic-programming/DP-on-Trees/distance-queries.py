# https://cses.fi/problemset/task/1135

import sys
from collections import deque

# Python mein fast I/O ke liye
input = sys.stdin.read

def solve():
    data = input().split()
    if not data: return
    
    n = int(data[0])
    q = int(data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(n - 1):
        u = int(data[idx])
        v = int(data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
    
    LOG = 19 # 2^18 ~ 2.6*10^5, so 19 is safe
    up = [[-1] * LOG for _ in range(n + 1)]
    depth = [0] * (n + 1)
    
    # 1. BFS to find depth and up[i][0]
    queue = deque([1])
    visited = [False] * (n + 1)
    visited[1] = True
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                up[v][0] = u
                depth[v] = depth[u] + 1
                queue.append(v)
    
    # 2. Binary Lifting Table
    for j in range(1, LOG):
        for i in range(1, n + 1):
            if up[i][j-1] != -1:
                up[i][j] = up[up[i][j-1]][j-1]
    
    # 3. LCA Function
    def get_lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        
        diff = depth[u] - depth[v]
        for j in range(LOG):
            if (diff >> j) & 1:
                u = up[u][j]
        
        if u == v: return u
        
        for j in range(LOG - 1, -1, -1):
            if up[u][j] != up[v][j]:
                u = up[u][j]
                v = up[v][j]
        return up[u][0]

    # 4. Process Queries
    output = []
    for _ in range(q):
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        
        lca_node = get_lca(a, b)
        # Distance formula apply kiya
        dist = depth[a] + depth[b] - 2 * depth[lca_node]
        output.append(str(dist))
    
    sys.stdout.write("\n".join(output) + "\n")

solve()