from collections import defaultdict


def shortest_path(arr):
    adj = defaultdict(list)
    for u, v in arr:
        adj[u].append(v)
    visit = set()
    q = ["A"]
    depth = 1
    while q:
        for i in range(len(q)):
            node = q.pop(0)
            if node == "E":
                return depth
            for ch in adj[node]:
                if ch not in visit:
                    visit.add(ch)
                    q.append(ch)
        depth += 1
    return 0


def shortest_path_undirected_bfs(n, graph, start):

    dist = {i: float("inf") for i in range(n)}
    dist[start] = 0

    q = [(start)]

    while q:
        node = q.pop(0)
        for child in graph[node]:
            if dist[node] + 1 < dist[child]:  # adding one to connected nodes
                dist[child] = dist[node] + 1
                q.append(child)
    return dist


def shortest_path_directed_acyclic(n, edges, start):

    st = []  # first fill all nodes in topological sorted order in stack

    adj = defaultdict(list)

    for u, v, d in edges:
        adj[u].append((v, d))

    def topological_sort(visit, node):

        nonlocal st

        visit.add(node)

        for child, d in adj[node]:
            if child not in visit:
                topological_sort(visit, child)

        st.append(node)

    topological_sort(
        set(), 0
    )  # call topological sort and get stack filled w.t values

    # BFS to find shortest path for all values present in stack

    dist = {i: float("inf") for i in range(n)}

    dist[start] = 0

    while st:
        node = st.pop()
        if dist[node] != float("inf"):
            # in weighted graph make sure to add given distance
            for child, d in adj[node]:
                if dist[node] + d < dist[child]:
                    dist[child] = dist[node] + d

    return dist


arr = [["A", "B"], ["B", "E"], ["A", "C"], ["C", "D"], ["D", "E"]]
arr2 = [
    ["A", "B"],
    ["B", "G"],
    ["A", "C"],
    ["C", "D"],
    ["D", "E"],
    ["G", "F"],
    ["F", "E"],
]
arr3 = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: [1]}
arr4 = [
    [0, 1, 1],
    [0, 4, 1],
    [1, 2, 2],
    [2, 3, 3],
    [4, 5, 2],
    [4, 3, 2],
    [5, 3, 4],
]

print(shortest_path(arr))
print(shortest_path(arr2))
print(shortest_path_undirected_bfs(4, arr3, 0))
print(shortest_path_directed_acyclic(6, arr4, 0))
