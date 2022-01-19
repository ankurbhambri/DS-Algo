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
        for ch in adj[node]:
            if dfs(ch) == False:
                return False

        cycle.remove(node)
        visit.add(node)
        res.append(node)

        return True

    for cur in range(n):

        if dfs(cur) == False:
            return []

    return res


# Using indegree method but finding cycle here !
def topologicalSort2(n, graph):
    adj = {c: [] for c in range(n)}
    indegree = {i: 0 for i in range(n)}

    for n1, n2 in graph:
        adj[n1].append(n2)
        indegree[n2] += 1

    res = []
    visit = set()
    q = [k for k, v in indegree.items() if v == 0]
    while q:
        node = q.pop(0)
        res.append(node)
        for ch in adj[node]:
            if ch not in visit:
                indegree[ch] -= 1
                if indegree[ch] == 0:
                    q.append(ch)
                    visit.add(ch)
    return res


print(topologicalSort(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
print(topologicalSort2(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
