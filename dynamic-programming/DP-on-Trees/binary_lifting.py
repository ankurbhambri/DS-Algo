import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

LOG = 18
up = [[-1] * LOG for _ in range(n + 1)]
depth = [0] * (n + 1)

# BFS to avoid recursion limit
def bfs(root=1):
    q = deque([root])
    up[root][0] = -1
    depth[root] = 0

    while q:
        node = q.popleft()
        for child in adj[node]:
            if child != up[node][0]:
                up[child][0] = node
                depth[child] = depth[node] + 1
                q.append(child)

bfs()

# Build binary lifting table
for j in range(1, LOG):
    for i in range(1, n + 1):
        if up[i][j - 1] != -1:
            up[i][j] = up[ up[i][j - 1] ][j - 1]

# k-th ancestor
def kth_ancestor(node, k):
    for j in range(LOG):
        if k & (1 << j):
            node = up[node][j]
            if node == -1:
                break
    return node

# LCA function
def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a

    # make depth same
    diff = depth[a] - depth[b]
    a = kth_ancestor(a, diff)

    if a == b:
        return a

    for j in range(LOG-1, -1, -1):
        if up[a][j] != -1 and up[a][j] != up[b][j]:
            a = up[a][j]
            b = up[b][j]

    return up[a][0]
