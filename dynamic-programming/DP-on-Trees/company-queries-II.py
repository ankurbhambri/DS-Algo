# https://cses.fi/problemset/task/1688


import sys
input = sys.stdin.readline

n, q = map(int, input().split())

LOG = 18
up = [[-1]*LOG for _ in range(n+1)]
depth = [0]*(n+1)

boss = list(map(int, input().split()))

# direct boss
for i in range(2, n+1):
    up[i][0] = boss[i-2]
    depth[i] = depth[up[i][0]] + 1

# binary lifting table
for j in range(1, LOG):
    for i in range(1, n+1):
        if up[i][j-1] != -1:
            up[i][j] = up[ up[i][j-1] ][j-1]

def lca(a, b):
    # 1️⃣ same depth
    if depth[a] < depth[b]:
        a, b = b, a

    diff = depth[a] - depth[b]
    for j in range(LOG):
        if diff & (1 << j):
            a = up[a][j]

    if a == b:
        return a

    # 2️⃣ jump both up
    for j in range(LOG-1, -1, -1):
        if up[a][j] != -1 and up[a][j] != up[b][j]:
            a = up[a][j]
            b = up[b][j]

    # 3️⃣ parent is answer
    return up[a][0]

# process queries
for _ in range(q):
    a, b = map(int, input().split())
    print(lca(a, b))
