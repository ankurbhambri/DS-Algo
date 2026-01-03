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
print(count_connected_components([[0, 1], [1, 2], [3, 4]], list(range(5))))


# using UNION and FIND algo
def countComponent(graph, all_nodes):

    # initially everyone iteself is a parent
    parent = [i for i in all_nodes]

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

print(countComponent([[0, 1], [1, 2], [3, 4]], list(range(5))))
print(countComponent([[0, 1], [1, 2], [2, 3], [3, 4]], list(range(5))))


# Count the Number of Complete Components

# https://leetcode.com/problems/count-the-number-of-complete-components/description


def countCompleteComponents(n, edges):

    adj = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def is_complete_component(component):
        m = len(component)
        expected_edges = (m * (m - 1)) // 2

        actual_edges = sum(len(adj[node]) for node in component) // 2

        return actual_edges == expected_edges

    def dfs(node, visit, component):
        visit.add(node)
        component.append(node)
        for nei in adj[node]:
            if nei not in visit:
                dfs(nei, visit, component)
    
    visit = set()
    c = 0
    for i in range(n):
        if i not in visit:
            component = []
            dfs(i, visit, component)
            if is_complete_component(component):
                c += 1

    return c

print(countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4]]))  # Output: 3
print(countCompleteComponents(5, [[0,1],[0,2],[1,2],[3,4]]))  # Output: 2
