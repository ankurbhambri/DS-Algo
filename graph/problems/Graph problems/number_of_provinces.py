# https://leetcode.com/problems/number-of-provinces/


def solve(graph):
    n = len(graph)
    visit = set()
    res = 0

    def dfs(node):
        visit.add(node)
        for i in range(n):
            if graph[node][i] == 1 and node not in visit:
                dfs(graph[node][i])

    for i in range(n):
        if i not in visit:
            res += 1
            dfs(i)

    return res
