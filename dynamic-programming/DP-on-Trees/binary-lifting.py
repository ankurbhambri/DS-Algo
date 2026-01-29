from collections import deque

class TreeAncestor:
    def __init__(self, n, edges, root=1):

        self.LOG = 18
        self.n = n

        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 1. Initialize Table and Depth
        self.up = [[-1] * self.LOG for _ in range(n + 1)]
        self.depth = [0] * (n + 1)

        # 2. BFS: Fill direct parents (2^0) and depth
        visited = {root}
        queue = deque([root])

        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if v not in visited:
                    self.up[v][0] = u
                    self.depth[v] = self.depth[u] + 1
                    queue.append(v)
                    visited.add(v)

        # 3. Fill the rest of the table (Powers of 2)
        for j in range(1, self.LOG):
            for i in range(1, n + 1):
                if self.up[i][j-1] != -1:
                    # i ka 2^j ancestor = (i ke 2^j-1 ancestor) ka 2^j-1 ancestor
                    self.up[i][j] = self.up[self.up[i][j-1]][j-1]

    def kth_ancestor(self, u, k):
        for j in range(self.LOG):
            if k & (1 << j): # Bit Manipulation: check if j-th bit is active
                u = self.up[u][j]
                if u == -1:
                    break
        return u

    def get_lca(self, u, v):

        # 1. U ko deeper node banao
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        # 2. U ko V ke same level par lao
        diff = self.depth[u] - self.depth[v]
        u = self.kth_ancestor(u, diff)

        if u == v:
            return u

        # 3. Binary Jumps together
        for j in range(self.LOG - 1, -1, -1):
            if self.up[u][j] != self.up[v][j]:
                u = self.up[u][j]
                v = self.up[v][j]

        # Final step: Dono ka parent hi LCA hai
        return self.up[u][0]


# Tree Structure: 
#      1
#     / \
#    2   3
#   / \
#  4   5

n = 5
edges = [(1, 2), (1, 3), (2, 4), (2, 5)]
tree = TreeAncestor(n, edges)

print(f"LCA of 4 and 5: {tree.get_lca(4, 5)}") # Output: 2 (Unka parent 2 hai)
print(f"LCA of 4 and 3: {tree.get_lca(4, 3)}") # Output: 1 (Root)
print(f"LCA of 2 and 4: {tree.get_lca(2, 4)}") # Output: 2 (Kyuki 2 khud ancestor hai)