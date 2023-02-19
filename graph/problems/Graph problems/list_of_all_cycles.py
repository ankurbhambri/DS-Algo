'''

Given an undirected graph, indicate if there is a cycle in the graph. Follow up,
return a list of all cycles that are seen. If there is none, return an empty list.

0 -----1-----2
| xxxxx|xxxxx |
3 -----4-----5


there are three cycles:
0, 1, 4, 3, 0
0, 1, 2, 5, 4, 3, 0
1, 2, 4, 5, 1

'''


def find_cycles_util(node, parent, graph, visited, path, result):
    visited[node] = True
    path.append(node)

    for neighbor in graph[node]:
        if visited[neighbor] == False:
            find_cycles_util(neighbor, node, graph, visited, path, result)
        elif neighbor != parent:
            if neighbor in path:
                cycle = path[path.index(neighbor) :]
                result.append(cycle)
    path.pop()


def find_cycles(graph):
    n = len(graph)
    visited = [False for _ in range(n)]
    path = []
    result = []
    for i in range(n):
        if not visited[i]:
            find_cycles_util(i, -1, graph, visited, path, result)
    return result


graph = {
    0: [1, 3],
    2: [1, 5],
    1: [0, 2, 4],
    3: [0, 4],
    5: [2, 4],
    4: [1, 3, 5],
}

cycles = find_cycles(graph)
for cycle in cycles:
    print(" -> ".join([str(node) for node in cycle]))
