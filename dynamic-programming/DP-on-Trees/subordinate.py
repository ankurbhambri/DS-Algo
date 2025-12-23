# https://cses.fi/problemset/task/1674/

# Simple need to return the size of each subtree (number of subordinates for each employee), nothing else

from collections import defaultdict

def solution(edges, n):

    # adjacency list: boss -> subordinates
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)

    size = [1] * n

    # bottom-up DFS to calculate subtree sizes
    def dfs(node):
        for child in tree[node]:
            dfs(child)
            size[node] += size[child]

    dfs(0)

    return size

print(solution([[0,1],[0,2],[1,3],[1,4],[2,5]], 6))  # [6, 3, 2, 1, 1, 1]
print(solution([[0,1],[0,2],[1,3],[3,4],[2,5],[4,6]], 7))  # [7, 4, 2, 3, 2, 1, 1]