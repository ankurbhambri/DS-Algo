# https://cses.fi/problemset/task/1132


# Tree Distances I

# Tree Diameter Technique (Two DFS / Two BFS method)

def tree_distances_example(edges, n):

    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    # DFS function
    def dfs(node, parent, dist, d):
        dist[node] = d
        for child in adj[node]:
            if child != parent:
                dfs(child, node, dist, d + 1)

    # Distance arrays
    distA = [0] * (n + 1)
    distB = [0] * (n + 1)

    # 1 Find first endpoint A
    dfs(1, -1, distA, 0)
    A = 1
    for i in range(1, n + 1):
        if distA[i] > distA[A]:
            A = i

    # 2 Find second endpoint B
    dfs(A, -1, distA, 0)
    B = A
    for i in range(1, n + 1):
        if distA[i] > distA[B]:
            B = i

    # 3 Find distances from B
    dfs(B, -1, distB, 0)

    # Output
    print("Tree edges:")
    for a, b in edges:
        print(f"{a} - {b}")

    print("\nMaximum distance for each node:")
    for i in range(1, n + 1):
        print(f"Node {i}: {max(distA[i], distB[i])}")


tree_distances_example([(1, 2), (1, 3), (3, 4),(3, 5)], 5)