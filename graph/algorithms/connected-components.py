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

    # Count the number of connected components
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



# https://leetcode.com/problems/count-the-number-of-complete-components/description


from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(u):

            visited[u] = True

            nodes = 1
            edge_cnt = len(graph[u])

            for v in graph[u]:

                if not visited[v]:

                    a, b = dfs(v)

                    nodes += a
                    edge_cnt += b

            return nodes, edge_cnt

        for i in range(n):

            if not visited[i]:

                nodes, edge_cnt = dfs(i)

                # edge_cnt counts every edge twice
                if edge_cnt == nodes * (nodes - 1):
                    ans += 1

        return ans


print(Solution().countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4]]))  # Output: 1
print(Solution().countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4], [4, 5]]))  # Output: 0