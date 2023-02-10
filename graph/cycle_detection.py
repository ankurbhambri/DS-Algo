''' 
In graph theory, a cycle graph or circular graph is a graph that consists of a single cycle, 
or in other words, some number of vertices connected in a closed chain
'''
from collections import defaultdict

def has_cycle(graph, vertex, parent, visited):
    visited[vertex] = True

    for v in graph[vertex]:
        if not visited[v]:
            if has_cycle(graph, v, vertex, visited):
                return True
        elif v != parent:
            return True

    return False

def find_cycle(graph, n):
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            if has_cycle(graph, i, -1, visited):
                return True

    return False

# Example usage
n = 5
graph = defaultdict(list)
graph[1].append(0)
graph[0].append(2)
graph[2].append(1)
graph[0].append(3)
graph[3].append(4)

if find_cycle(graph, n):
    print("Graph contains a cycle")
else:
    print("Graph does not contain a cycle")
    
    

'''
It is not possible to find a cycle in a graph using a breadth-first search (BFS) algorithm,
as BFS traverses the graph in a level-by-level manner, visiting all vertices at the current
level before moving on to the next level. On the other hand, cycles are formed by vertices
that are reachable from each other in a circular manner, which is not possible to detect
using BFS. To find a cycle in a graph, you can use depth-first search (DFS), as explained
in my previous answer.
'''
