# https://cses.fi/problemset/view/1131/


def solution(edges, n):

    if n == 1:
        return 0

    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    diameter = 0

    def dfs(u, p):

        nonlocal diameter
        max1, max2 = 0, 0  # Top two heights

        for child in adj[u]:

            if child != p:

                height = dfs(child, u)
                
                if height > max1:

                    max2 = max1
                    max1 = height

                elif height > max2:
                    max2 = height

        diameter = max(diameter, max1 + max2)

        return max1 + 1
    
    dfs(1, -1)
    return diameter

print(solution([(1, 2), (1, 3), (3, 4), (3, 5)], 5)) # 3
print(solution([(1, 2)], 2)) # 1


# Alternative simpler 2 DFS approach, but hard to proove correctness

import sys
sys.setrecursionlimit(300000)

def find_diameter(n, edges):

    if n == 1: return 0
    
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def dfs(u, p, dist):

        # Yeh function (node, distance) return karega
        farthest_node = u
        max_dist = dist
        
        for v in adj[u]:
            if v != p:
                node, d = dfs(v, u, dist + 1)
                if d > max_dist:
                    max_dist = d
                    farthest_node = node

        return farthest_node, max_dist

    # Step 1: Kisi bhi node (1) se sabse door wala node (X) dhundo
    node_X, _ = dfs(1, -1, 0)
    
    # Step 2: Node X se sabse door wala node (Y) dhundo
    node_Y, diameter = dfs(node_X, -1, 0)
    
    return diameter


print(find_diameter(5, [(1, 2), (1, 3), (3, 4), (3, 5)])) # 3
print(find_diameter(2, [(1, 2)])) # 1