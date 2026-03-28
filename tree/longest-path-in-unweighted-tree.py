# Given an undirected tree, we need to find the longest path of this tree where a path is defined as a sequence of nodes.
# The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.  Each node has labels in the set {0, 1, ..., edges.length}.

# https://leetcode.ca/all/1245.html
# https://www.geeksforgeeks.org/longest-path-undirected-tree/


from collections import defaultdict, deque

# TC - O(V+E)
# SC - O(V)


def tree_diameter(edges):

    if not edges:
        return 0

    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def dfs(start):

        visited = set()
        queue = [(start, 0)]
        farthest_node = (start, 0)

        while queue:

            node, dist = queue.pop(0)
            visited.add(node)

            if dist > farthest_node[1]:
                farthest_node = (node, dist)

            for neighbor in adj[node]:
                if neighbor not in visited:
                    queue.append((neighbor, dist + 1))

        return farthest_node

    # First DFS to find the farthest node from an arbitrary node (e.g., 0)
    farthest_node, _ = dfs(0)

    # Second DFS from the farthest node found
    _, max_distance = dfs(farthest_node)

    return max_distance


edges = [[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]
print(tree_diameter(edges))  # Output: 4

edges = [[0, 1], [0, 2]]
print(tree_diameter(edges))  # Output: 2

edges = [
    [0, 1],
    [1, 2],
    [2, 3],
    [1, 4],
    [4, 5],
    [4, 6],
    [6, 7],
    [6, 8],
    [8, 9],
    [8, 10],
]
print(tree_diameter(edges))  # Output: 6

edges = [[0, 1], [1, 2], [2, 3], [2, 9], [2, 4], [4, 5], [1, 6], [6, 7], [6, 8]]
print(tree_diameter(edges))  # Output: 5


# Similar question - https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/
# Q) Find Minimum Diameter After Merging Two Trees


def minimumDiameterAfterMerge(edges1, edges2):

    def diameter(edges):

        if not edges:
            return 0

        n = len(edges) + 1
        adj = [[] for i in range(n)]

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(start):

            visited = set()
            queue = [(start, 0)]
            farthest_node = (start, 0)

            while queue:

                node, dist = queue.pop(0)
                visited.add(node)

                if dist > farthest_node[1]:
                    farthest_node = (node, dist)

                for neighbor in adj[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, dist + 1))

            return farthest_node

        # First DFS to find the farthest node from an arbitrary node (e.g., 0)
        farthest_node, _ = dfs(0)

        # Second DFS from the farthest node found
        _, max_distance = dfs(farthest_node)

        return max_distance

    d1 = diameter(edges1)  # diameter of tree 1
    d2 = diameter(edges2)  # diameter of tree 2

    """
        Case 1: The Diameter Stays in One of the Original Trees
        The longest path could remain entirely within one of the two original trees.
        This happens if the additional edge doesn't introduce a longer path.
        The diameter in this case is: max(d1, d2)

        Case 2: The Diameter Crosses the New Edge
        If the diameter crosses the new edge, the longest path will include:
        Half the diameter of Tree 1 (approximately its radius),
        Half the diameter of Tree 2 (approximately its radius),
        The weight of the new edge (typically +1 if no specific weight is given).
    """

    return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)


print(
    minimumDiameterAfterMerge(
        [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]],
        [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]],
    )
)  # Output: 5

print(minimumDiameterAfterMerge([[0, 1]], []))  # Output: 2
