# https://leetcode.com/problems/kth-ancestor-of-a-tree-node/

# Simple Binary Lifting Implementation

class TreeAncestor:
    def __init__(self, n: int, parent):

        self.LOG = 18 # enough for 2*10^5 nodes
        self.up = [[-1] * self.LOG for _ in range(n + 1)]

        # base case: 2 ^ 0-th ancestor (direct boss)
        for i in range(n):
            self.up[i][0] = parent[i]

        # build binary lifting table
        for j in range(1, self.LOG):
            for i in range(1, n + 1):
                if self.up[i][j - 1] != -1:
                    self.up[i][j] = self.up[ self.up[i][j - 1] ][j - 1]

    def kth_boss(self, x, k):
        for j in range(self.LOG):
            if k & (1 << j):
                x = self.up[x][j]
                if x == -1:
                    return -1
        return x

    def getKthAncestor(self, node: int, k: int) -> int:
        return self.kth_boss(node, k)

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)