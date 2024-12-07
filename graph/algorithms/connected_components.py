# Number of Connected Components in an Undirected Graph


def count_connected_components(graph, all_nodes):

    adj = {node: [] for node in all_nodes}

    for u, v in graph:
        adj[u].append(v)
        adj[v].append(u)

    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                dfs(neighbor)

    connected_components = 0
    for node in all_nodes:
        if node not in visited:
            dfs(node)
            connected_components += 1

    return connected_components


graph = [
    ["A", "B"],
    ["A", "C"],
    ["A", "D"],
    ["D", "E"],
    ["B", "E"],
    ["F", "H"],
    ["F", "G"],
    ["I", "J"],
]

all_nodes = ["A", "B", "C", "D", "E", "F", "G", "I", "J", "H"]
print(count_connected_components(graph, all_nodes))


# using UNION and FIND algo
def countComponent(graph, all_nodes):

    # everyone iteself is a parent
    parent = {i: [] for i in all_nodes}

    def find(node):
        if node != parent[node]:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        p1, p2 = find(node1), find(node2)
        if p1 != p2:
            # if both have different parent then node1 parent will be node2 parent
            parent[node2] = parent[node1]
            return 1
        return 0

    res = len(all_nodes)
    for n1, n2 in graph:
        res -= union(n1, n2)
    return res


graph = [
    ["A", "B"],
    ["A", "C"],
    ["A", "D"],
    ["D", "E"],
    ["B", "E"],
    ["F", "H"],
    ["F", "G"],
    ["I", "J"],
]

all_nodes = ["A", "B", "C", "D", "E", "F", "G", "I", "J", "H"]
# n = 5
# edges = [[0, 1], [1, 2], [3, 4]]
print(countComponent(graph, all_nodes))
