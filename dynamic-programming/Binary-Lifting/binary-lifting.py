from collections import deque

# TC: O(N log N) for preprocessing, O(log N) for each query
# SC: O(N log N) for the up table and O(N) for depth array
class TreeAncestor:
    def __init__(self, n, edges, root=1):

        self.n = n
        self.LOG = 18 # 2^18 > 10^5, so we can cover all ancestors up to 10^5 nodes

        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 1. Initialize Table and Depth
        self.depth = [0] * (n + 1)
        self.up = [[-1] * self.LOG for _ in range(n + 1)]

        # 2. BFS: Fill direct parents (2^0) and depth
        visited = {root}
        queue = deque([root])

        # we can also use dfs here
        '''
        def dfs(u, p):
            self.up[u][0] = p

            for i in range(1, self.LOG):
                if (self.up[u][i - 1] != -1):
                    self.up[u][i] = self.up[self.up[u][i - 1]][i - 1]
                else:
                    self.up[u][i] = -1
            
            for child in self.adj[u]:
                dfs(child, u)

        '''

        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if v not in visited:
                    self.up[v][0] = u # 2^0-th parent is immediate parent
                    self.depth[v] = self.depth[u] + 1
                    queue.append(v)
                    visited.add(v)

        # 3. Fill the rest of the table (Powers of 2)
        for i in range(1, self.LOG):
            for node in range(self.n):
                parent = self.up[node][i-1]
                if parent != -1:
                    self.up[node][i] = self.up[parent][i-1]

    def kth_ancestor(self, node, k):
        for i in range(self.LOG):
            if k & (1 << i): # if i-th bit is active
                node = self.up[node][i]
                if node == -1:
                    break
        return node


    def get_lca(self, u, v):

        # Step 1: Ensure u hamesha gehra (deeper) node ho
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        # Step 2: Dono nodes ko same level/depth par lao
        # u ko upar uthao jitna dono ki depth mein diff hai
        diff = self.depth[u] - self.depth[v]
        u = self.kth_ancestor(u, diff)

        # Agar same depth par aane ke baad u aur v ek hi node hain,
        # toh wahi LCA hai (e.g., agar v, u ka ancestor tha)
        if u == v:
            return u

        # Step 3: Dono ko ek saath upar uthao (Bade jumps se shuru karke chote tak)
        # Hum tabhi jump karenge jab dono ke ancestors ALAG honge
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