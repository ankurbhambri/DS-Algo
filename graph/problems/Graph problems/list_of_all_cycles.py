'''

Given an undirected graph, indicate if there is a cycle in the graph. Follow up,
return a list of all cycles that are seen. If there is none, return an empty list.

0 -----1-----2
| xxxxx|xxxxx |
3 -----4-----5


there are three cycles:
0, 1, 4, 3, 0
0, 1, 2, 5, 4, 3, 0
1, 2, 4, 5, 1

'''


def solve(graph, n):

    path = []
    res = []
    visit = set()

    # to find out cycle
    def dfs(node, parent):

        visit.add(node)
        path.append(node)

        for child in graph[node]:
            if child not in visit:
                dfs(child, node)
            elif child != parent:
                if child in path:
                    cycle = path[path.index(child):]
                    res.append(cycle)
        path.pop()

    for i in range(n):
        if i not in visit:
            dfs(i, -1)
    return res


graph = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4],
    5: [2, 4],
    4: [1, 3, 5],
}

cycles = solve(graph)
for cycle in cycles:
    print(" -> ".join([str(node) for node in cycle]))
