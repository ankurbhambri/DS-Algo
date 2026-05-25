# https://cses.fi/problemset/task/1132


# Tree Distances I

# Tree Diameter Technique (Three DFS or Three BFS method)

'''
Time Complexity: O(N)

DFS Visits: Humne poore code mein kul mila kar 3 baar DFS chalaya hai.
Tree mein N nodes aur N-1 edges hote hain.
Ek standard DFS poore tree ko visit karne mein O(V + E) = O(N + (N-1)) = O(N) time leta hai.
Humne 3 baar DFS chalaya, toh total time hua: 3 × O(N) = O(N).
Nodes ka maximum dhoondne ke liye humne O(N) ke loops chalaye hain.
'''

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
    dummyDist = [0] * (n + 1)  # Just to reuse the same array for DFS

    # 1 Find first endpoint A
    dfs(1, -1, dummyDist, 0)
    A = 1
    for i in range(1, n + 1):
        if dummyDist[i] > dummyDist[A]:
            A = i

    # 2 Find second endpoint B
    dfs(A, -1, distA, 0)
    B = 1
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