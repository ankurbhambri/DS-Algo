def shortest_cycle_undirected(graph, n):
    adj = {i: [] for i in range(n)}

    for u, v in graph:
        adj[u].append(v)
        adj[v].append(u)

    res = float("inf")

    for i in range(n):

        visit = set()
        distance = {i: 0 for i in range(n)}
        q = [(i)]

        while q:
            node = q.pop(0)

            for ch in adj[node]:

                if ch not in visit:
                    distance[ch] = 1 + distance[node]
                    visit.add(ch)
                    q.append(ch)

                else:
                    res = min(res, distance[node] + distance[ch] + 1)

    return res if res != float("inf") else -1


n = 7
graph = [[0, 6], [0, 5], [5, 1], [1, 6], [2, 6], [2, 3], [3, 4], [4, 1]]
print(shortest_cycle_undirected(graph, n))
