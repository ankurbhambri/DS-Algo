# https://cses.fi/problemset/result/15712595/

# https://leetcode.com/problems/kth-ancestor-of-a-tree-node/description/


def solution(n, bosses, queries):

    LOG = 18 # enough for 2*10^5 nodes
    up = [[-1] * LOG for _ in range(n + 1)]

    # base case: 2 ^ 0-th ancestor (direct boss)
    for i in range(2, n + 1):
        up[i][0] = bosses[i - 2]

    # build binary lifting table
    for j in range(1, LOG):
        for i in range(1, n + 1):
            if up[i][j - 1] != -1:
                up[i][j] = up[ up[i][j - 1] ][j - 1]

    def kth_boss(x, k):
        for j in range(LOG):
            if k & (1 << j):
                x = up[x][j]
                if x == -1:
                    return -1
        return x

    results = []
    for x, k in queries:
        results.append(kth_boss(x, k))

    return results


# tree looking like this:

#        1
#      /   \
#     2     3
#    /       \
#   4         5

print(solution(5, [1, 1, 2, 3], [(4, 1), (5, 1), (4, 2), (5, 2), (3, 3)]))  # Output: [2, 3, 1, 1, -1]
print(solution(9, [1, 1, 2, 2, 3, 3, 4, 4], [(3, 1024), (4, 3), (2, 1), (3, 1), (2, 2), (3, 2)]))  # Output: [-1, -1, 1, 1, -1, -1]


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

    # same depth
    if depth[a] < depth[b]:
        a, b = b, a

    diff = depth[a] - depth[b]

    if a == b:
        return a

    for j in range(LOG):
        if diff & (1 << j):
            a = up[a][j]

    if a == b:
        return a

    # jump both up
    for j in range(LOG-1, -1, -1):
        if up[a][j] != -1 and up[a][j] != up[b][j]:
            a = up[a][j]
            b = up[b][j]

    # parent is answer
    return up[a][0]

# process queries
for _ in range(q):
    a, b = map(int, input().split())
    print(lca(a, b))
