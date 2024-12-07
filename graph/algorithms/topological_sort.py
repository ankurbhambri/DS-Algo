""" 
- It sorts parents and child in correct ordering

- DAG - A directed graph with no cycle is called DAG.

- Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of 
  vertices such that for every directed edge u v, vertex u comes before v in the ordering.

- Topological Sorting for a graph is not possible if the graph is not a DAG(Direct Acyclic Graph).



"""


def topologicalSort(n, graph):
    adj = {c: [] for c in range(n)}

    for n1, n2 in graph:
        adj[n1].append(n2)

    res = []
    visit = cycle = set()

    def dfs(node):
        # if there is cycle means no possible to do topological sort
        if node in cycle:
            return True

        if node in visit:
            return False

        # First add in cycle then remove it.
        cycle.add(node)
        visit.add(node)

        for ch in adj[node]:
            if dfs(ch):
                return True

        cycle.remove(node)  # backtrack
        res.append(node)

        return False

    for cur in range(n):
        if dfs(cur):
            return []

    return res


print(topologicalSort(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))


# Cycle Detection in Directed Graph using BFS(Kahn's Algorithm) indegree method
def khan_algo(graph):

    indegree = {i: 0 for i in graph}

    for i in range(len(graph)):  # need n here
        for node in graph[i]:
            indegree[node] += 1

    q = [i for i in range(len(graph)) if indegree[i] == 0]

    res = []
    while q:
        node = q.pop(0)
        res.append(node)

        for nei in adj[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return res


adj = {0: [], 1: [], 2: [3], 3: [1], 4: [0, 1], 5: [0, 2]}
print(khan_algo(adj))

"""
Note:-
Topological sort is an algorithm that takes a directed acyclic graph (DAG) as 
input and produces a linear ordering of its vertices such that for every directed
edge uv from vertex u to vertex v, u comes before v in the ordering.

Kahn's algorithm, also known as the "topological sorting algorithm", is another
algorithm used to perform topological sorting of a DAG. It works by iteratively
removing nodes with no incoming edges and adding them to the sorted list until
all nodes have been processed.

In summary, Kahn's algorithm is one specific implementation of the topological
sort algorithm.
"""

# Q1 - https://leetcode.com/problems/course-schedule/
# Q2 - https://leetcode.com/problems/course-schedule-ii/


# Q1 solution


def canFinish(n, preq):

    indegree = {i: 0 for i in range(n)}
    adj = {i: [] for i in range(n)}

    for crs, pre in preq:
        # [1, 0] 0 must be completed before 1 so this way we can make adj
        adj[pre].append(crs)
        indegree[crs] += 1  # no

    q = [i for i in range(n) if indegree[i] == 0]

    res = []
    while q:

        node = q.pop(0)
        res.append(node)

        for nei in adj[node]:
            indegree[nei] -= 1

            if indegree[nei] == 0:
                q.append(nei)

    return len(res) == n


# Q2 Solution


def findOrder(n, preq):

    indegree = {i: 0 for i in range(n)}
    adj = {i: [] for i in range(n)}

    for u, v in preq:
        adj[u].append(v)
        indegree[v] += 1

    q = [i for i in range(n) if indegree[i] == 0]

    res = []
    while q:

        node = q.pop(0)
        res.append(node)

        for nei in adj[node]:
            indegree[nei] -= 1

            if indegree[nei] == 0:
                q.append(nei)

    return res[::-1] if len(res) == n else []  # reverse to get the last from first
