''' 
- It sorts parents and child in correct ordering

- Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of 
  vertices such that for every directed edge u v, vertex u comes before v in the ordering.

- Topological Sorting for a graph is not possible if the graph is not a DAG.
'''


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
        visit.add(node)

        for ch in adj[node]:
            if not dfs(ch):
                return False

        cycle.remove(node) # backtrack
        res.append(node)

        return True

    for cur in range(n):

        if dfs(cur) == False:
            return []

    return res

# [0, 0, 1, 0, 2, 0, 1, 0, 2, 3]    


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
