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
            return False

        if node in visit:
            return True

        # First add in cycle then remove it.
        cycle.add(node)
        visit.add(node)

        for ch in adj[node]:
            if not dfs(ch):
                return False

        cycle.remove(node)  # backtrack
        res.append(node)

        return True

    for cur in range(n):
        if dfs(cur) == False:
            return []

    return res


print(topologicalSort(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))


# Khan's Algorithm for BFS to create topological sort using indegree method.

# Indegree means how many nodes directly connecting to a node.


def topologicalSort2(n, graph):
    adj = {c: [] for c in range(n)}
    in_degree = {i: 0 for i in range(n)}

    for n1, n2 in graph:
        adj[n1].append(n2)
        in_degree[n2] += 1  # finding indegree for nodes

    res = []
    visit = set()

    # Taking all the edges who has no incoming edge into it.
    q = [k for k, v in in_degree.items() if v == 0]

    while q:
        node = q.pop(0)
        res.append(node)
        for ch in adj[node]:
            if ch not in visit:
                in_degree[ch] -= 1
                if not in_degree[ch]:
                    q.append(ch)
                    visit.add(ch)
    return res


print(topologicalSort2(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))


# Cycle Detection in Directed Graph using BFS(Kahn's Algorithm) indegree method


def Kahn_algo(n, graph):
    adj = {c: [] for c in range(n)}
    in_degree = {i: 0 for i in range(n)}

    for n1, n2 in graph:
        adj[n1].append(n2)
        in_degree[n2] += 1

    visit = set()

    # Taking all the edges who has no incoming edge into it.
    q = [k for k, v in in_degree.items() if v == 0]

    count = 0  # only this is the change in above code

    while q:
        node = q.pop(0)
        count += 1  # keep counting
        for ch in adj[node]:
            if ch not in visit:
                in_degree[ch] -= 1
                if not in_degree[ch]:
                    q.append(ch)
                    visit.add(ch)

    # If i'm able to generate the topological sort that means count will be
    # equal to n where n will be total number of nodes
    if count == n:  # if counting equals to
        return False
    return True


print(Kahn_algo(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))

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
