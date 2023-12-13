from collections import defaultdict

# https://cses.fi/problemset/task/1674/


def subordinates(n, bosses):
    graph = [[] for _ in range(n)]

    for i in range(1, n):
        boss = bosses[i - 1]
        # starting with 0
        graph[boss - 1].append(i)

    ans = [0] * n

    def dfs(node):
        sm = 0
        for neighbor in graph[node]:
            sm += dfs(neighbor)
        ans[node] = sm
        return sm + 1

    dfs(0)
    return ans


n = 5
bosses = [1, 1, 2, 3]

result = subordinates(n, bosses)
print(result)
