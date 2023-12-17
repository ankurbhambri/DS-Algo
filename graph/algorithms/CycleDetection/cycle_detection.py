''' 
In graph theory, a cycle graph or circular graph is a graph that consists of a single cycle, 
or in other words, some number of vertices connected in a closed chain
'''

# In Undirected graph case using DFS

# https://leetcode.com/problems/graph-valid-tree/


def find_cycle_undirected_graph(graph, n):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for child in graph[node]:
            if child not in visited:
                if dfs(child, node):
                    return True
            # already visited node and that node is not parent means cycle exists
            elif child != parent:
                return True

        return False

    for i in range(n):
        if i not in visited:
            if dfs(i, -1):
                return True
    return False


graph = {0: [1], 1: [2], 2: [3], 3: []}  # no cycle
graph1 = {0: [1], 3: [0, 2], 2: [1], 1: []}  # cycle

print("Cycle" if find_cycle_undirected_graph(
    graph, 4) else "No cycle")  # no cycle

print("Cycle" if find_cycle_undirected_graph(
    graph1, 4) else "No cycle")  # cycle


# In  Directed graph case using DFS
def find_cycle_directed(graph, n):
    visited = set()
    dfs_visited = set()

    def has_cycle_directed(graph, node, visited, dfs_visited):
        visited.add(node)
        dfs_visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                if has_cycle_directed(graph, nei, visited, dfs_visited):
                    return True
            # if node present in both set that means cycle exists.
            elif nei in dfs_visited:
                return True
        dfs_visited.remove(node)
        return False

    for i in range(n):
        if i not in visited:
            if has_cycle_directed(graph, i, visited, dfs_visited):
                return True
    return False


graph = {0: [1], 1: [2], 2: [3], 3: []}  # no cycle
graph1 = {0: [1], 1: [2], 2: [0]}  # cycle

print("Cycle" if find_cycle_directed(graph, 4) else "No cycle")  # no cycle

print("Cycle" if find_cycle_directed(graph1, 3) else "No cycle")  # cycle


# In Undirected graph case using BFS
def has_cycle_undirected_bfs(graph, node, visited):

    q = [(node, -1)]
    visited.add(node)

    while q:
        n, p = q.pop()
        for nei in graph[n]:
            if nei not in visited:
                visited.add(nei)
                q.append((nei, node))
            elif nei != p:
                return True
    return False


def find_cycle_undirected_bfs(graph, n):
    visited = set()
    for i in range(n):
        if i not in visited:
            if has_cycle_undirected_bfs(graph, i, visited):
                return True
    return False


graph = {0: [1], 1: [2], 2: [3], 3: []}  # no cycle
graph1 = {0: [1], 3: [0, 2], 2: [1], 1: []}  # cycle

print(
    "Cycle" if find_cycle_undirected_bfs(graph, 4) else "No cycle"
)  # no cycle

print("Cycle" if find_cycle_undirected_bfs(graph1, 4) else "No cycle")  # cycle


# Cycle Detection in Directed Graph using BFS(Kahn's Algorithm) indegree method
def topologicalSort2(n, graph):

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
                if in_degree[ch] == 0:
                    q.append(ch)
                    visit.add(ch)

    # If i'm able to generate the topological sort that means count will be
    # equal to n where n will be total number of nodes
    if count == n:  # if counting equals to
        return False
    return True


'''
It is not possible to find a cycle in a graph using a breadth-first search (BFS) algorithm,
as BFS traverses the graph in a level-by-level manner, visiting all vertices at the current
level before moving on to the next level. On the other hand, cycles are formed by vertices
that are reachable from each other in a circular manner, which is not possible to detect
using BFS. To find a cycle in a graph, you can use depth-first search (DFS), as explained
above.
'''
