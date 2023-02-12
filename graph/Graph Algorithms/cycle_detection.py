''' 
In graph theory, a cycle graph or circular graph is a graph that consists of a single cycle, 
or in other words, some number of vertices connected in a closed chain
'''


def has_cycle(graph, node, parent, visited):

    visited[node] = True
    for nei in graph[node]:
        if not visited[nei]:
            if has_cycle(graph, nei, node, visited):
                return True
        elif nei != parent:
            return True

    return False


def find_cycle(graph, n):
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            if has_cycle(graph, i, -1, visited):
                return True
    return False


graph = {0: [1], 1: [2], 2: [3], 3: []}  # no cycle
graph1 = {0: [1], 3: [0, 2], 2: [1], 1: []}  # cycle

print("Cycle" if find_cycle(graph, 4) else "No cycle")  # no cycle

print("Cycle" if find_cycle(graph1, 4) else "No cycle")  # cycle


# Detect Cycle in a directed graph using colors


def DFSUtil(u, color, graph):
    # GRAY : This vertex is being processed (DFS
    # 		 for this vertex has started, but not
    # 		 ended (or this vertex is in function
    # 		 call stack)
    color[u] = "GRAY"

    for v in graph[u]:

        if color[v] == "GRAY":
            return True

        if color[v] == "WHITE" and DFSUtil(v, color, graph) == True:
            return True

    color[u] = "BLACK"
    return False


def isCyclic(graph, V):
    color = ["WHITE"] * V

    for i in range(V):
        if color[i] == "WHITE":
            if DFSUtil(i, color, graph) == True:
                return True
    return False


# Driver program to test above functions
g = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}

print(
    "Graph contains a cycle"
    if isCyclic(g, 4)
    else "Graph doesn't contain cycle"
)


'''
It is not possible to find a cycle in a graph using a breadth-first search (BFS) algorithm,
as BFS traverses the graph in a level-by-level manner, visiting all vertices at the current
level before moving on to the next level. On the other hand, cycles are formed by vertices
that are reachable from each other in a circular manner, which is not possible to detect
using BFS. To find a cycle in a graph, you can use depth-first search (DFS), as explained
above.
'''
