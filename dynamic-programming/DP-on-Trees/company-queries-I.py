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


################ Ignore CSES input-output code below

# import sys
# input = sys.stdin.readline

# n, q = map(int, input().split())

# LOG = 18 # enough for 2*10^5 nodes
# up = [[-1]*LOG for _ in range(n+1)]

# # parents of 2..n
# boss = list(map(int, input().split()))

# # base case: 2^0-th ancestor (direct boss)
# for i in range(2, n+1):
#     up[i][0] = boss[i-2]

# # build binary lifting table
# for j in range(1, LOG):
#     for i in range(1, n+1):
#         if up[i][j-1] != -1:
#             up[i][j] = up[ up[i][j-1] ][j-1]

# def kth_boss(x, k):
#     for j in range(LOG):
#         if k & (1 << j):
#             x = up[x][j]
#             if x == -1:
#                 return -1
#     return x

# # process queries
# for _ in range(q):
#     x, k = map(int, input().split())
#     print(kth_boss(x, k))


