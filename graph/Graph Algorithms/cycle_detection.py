''' 
In graph theory, a cycle graph or circular graph is a graph that consists of a single cycle, 
or in other words, some number of vertices connected in a closed chain
'''
from collections import defaultdict


def has_cycle(graph, node, parent, visited):

    visited[node] = True
    print('node cam in fnction with visited', node, visited, parent)
    for nei in graph[node]:
        print('nei', nei)
        if not visited[nei]:
            if has_cycle(graph, nei, node, visited):
                return True
        elif nei != parent:
            return True

    return False


def find_cycle(graph, n):
    visited = [False] * n
    for i in range(n):
        print('find_cycle', i)
        if not visited[i]:
            if has_cycle(graph, i, -1, visited):
                return True
    return False


# Example usage
n = 6
graph = defaultdict(list)
graph[0].append(1)
graph[2].append(1)
graph[4].append(0)
# graph[2].append(3)
# graph[3].append(4)
# graph[4].append(2)

# graph[0].append(1)
# graph[1].append(2)
# graph[2].append(3)
# graph[3].append(4)
# graph[2].append(5)


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
above.
'''
