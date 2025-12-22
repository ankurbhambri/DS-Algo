# https://cses.fi/problemset/task/1674/

# Simple need to return the size of each subtree (number of subordinates for each employee), nothing else

import sys
from collections import defaultdict

def solution(edges, n):

    # adjacency list: boss -> subordinates
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)

    size = [1] * n

    def dfs(node):
        for child in tree[node]:
            dfs(child)
            size[node] += size[child]

    dfs(0)

    return size

print(solution([[0,1],[0,2],[1,3],[1,4],[2,5]], 6))  # [6, 3, 2, 1, 1, 1]


# OR We can write in below ways as well

def subordinates(n, bosses):
    graph = [[] for _ in range(n)]

    for i in range(1, n):
        boss = bosses[i - 1]
        # starting with 0
        graph[boss - 1].append(i)

    ans = [0] * n

    def dfs(node):
        sm = 0
        for child in graph[node]:
            sm += dfs(child)
        ans[node] = sm
        return sm + 1

    dfs(0)
    return ans


n = 5
bosses = [1, 1, 2, 3]

result = subordinates(n, bosses)
print(result)
