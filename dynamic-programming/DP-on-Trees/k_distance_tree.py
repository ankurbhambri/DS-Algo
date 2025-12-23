# https://codeforces.com/contest/161/problem/D


def k_distance_tree(edges, n, k):
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    
    total_pairs = 0

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Bottom-up DFS
    def dfs(node, parent):

        nonlocal total_pairs

        dp[node][0] = 1  # Count the node itself

        for child in adj[node]:

            if child != parent:

                dfs(child, node)

                for dist in range(k):
                    # at ith distance from node and k-dist-1 from child subtree find those pairs
                    total_pairs += dp[node][dist] * dp[child][k - dist - 1]
                
                # updating it in the last to make sure we are not using it agin in the multiplicaton above for new child values
                for dist in range(k):
                    dp[node][dist + 1] += dp[child][dist]

    dfs(1, 0)

    return total_pairs

print(k_distance_tree([(1, 2),(2, 3),(3, 4),(2, 5)], 5, 2))  # Output: 4