# Using Tarjan's Algorithm finding bridges in graph
# TC O(V+E)


from collections import defaultdict


def utils(graph, n):
    disc = low = parent = [-1] * n
    bridge = []

    def dfs(u):
        time = 0
        disc[u] = low[u] = time
        time += 1

        for v in graph[u]:
            if disc[v] == -1:

                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])

                if low[v] > disc[u]:
                    print(u, v)
                    bridge.append((u, v))

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    for i in range(n):
        if disc[i] == -1:
            dfs(i)

    return bridge


graph = defaultdict(list)
# graph[0].append(2)
# graph[2].append(0)
# graph[0].append(3)
# graph[3].append(0)
# graph[1].append(0)
# graph[0].append(1)
# graph[2].append(1)
# graph[1].append(2)
# graph[3].append(4)
# graph[4].append(3)

graph[1].append(0)
graph[0].append(2)
graph[2].append(1)
graph[0].append(3)
graph[3].append(4)


print(utils(graph, 5))
