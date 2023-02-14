''' 
In graph theory, a cycle graph or circular graph is a graph that consists of a single cycle, 
or in other words, some number of vertices connected in a closed chain
'''

# In Undirected graph case using DFS


def has_cycle_undirected(graph, node, parent, visited):

    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            if has_cycle_undirected(graph, nei, node, visited):
                return True
        # already visited node and that node is not parent means cycle exists
        elif nei != parent:
            return True

    return False


def find_cycle_undirected(graph, n):
    visited = set()
    for i in range(n):
        if i not in visited:
            if has_cycle_undirected(graph, i, -1, visited):
                return True
    return False


graph = {0: [1], 1: [2], 2: [3], 3: []}  # no cycle
graph1 = {0: [1], 3: [0, 2], 2: [1], 1: []}  # cycle

print("Cycle" if find_cycle_undirected(graph, 4) else "No cycle")  # no cycle

print("Cycle" if find_cycle_undirected(graph1, 4) else "No cycle")  # cycle


# In  Directed graph case using DFS


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


def find_cycle_directed(graph, n):
    visited = set()
    dfs_visited = set()
    for i in range(n):
        if i not in visited:
            if has_cycle_directed(graph, i, visited, dfs_visited):
                return True
    return False


graph = {0: [1], 1: [2], 2: [3], 3: []}  # no cycle
graph1 = {0: [1], 1: [2], 2: [0]}  # cycle

print("Cycle" if find_cycle_directed(graph, 4) else "No cycle")  # no cycle

print("Cycle" if find_cycle_directed(graph1, 3) else "No cycle")  # cycle

'''
It is not possible to find a cycle in a graph using a breadth-first search (BFS) algorithm,
as BFS traverses the graph in a level-by-level manner, visiting all vertices at the current
level before moving on to the next level. On the other hand, cycles are formed by vertices
that are reachable from each other in a circular manner, which is not possible to detect
using BFS. To find a cycle in a graph, you can use depth-first search (DFS), as explained
above.
'''
