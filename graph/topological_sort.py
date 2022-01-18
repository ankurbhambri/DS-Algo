''' It sorts parents and child in correct ordering'''


def topologicalSort(n, graph):

    adj = {c: [] for c in range(n)}

    for n1, n2 in graph:
        adj[n1].append(n2)

    res = []
    visit = cycle = set()

    def dfs(node):

        if node in cycle:
            return False

        if node in visit:
            return True

        # First add in cycle then remove it.
        cycle.add(node)
        for preq in adj[node]:
            if not dfs(preq):
                return False

        cycle.remove(node)
        visit.add(node)
        res.append(node)

        return True

    for cur in range(n):

        if not dfs(cur):
            return []

    return res


print(topologicalSort(4, [[1, 0], [2, 0], [3, 1], [3, 4]]))
