"""
    Binary lifting is used in tree algorithms, to solve problems involving Lowest Common Ancestor (LCA) or efficiently finding ancestors at specific levels. 
    It uses dynamic programming and precomputes answers for certain queries to enable quick resolution during execution.

    why binary lifting?
    Without binary lifting, finding ancestors might involve traversing the tree repeatedly, which can be slow for large trees. Binary lifting preprocesses the tree to allow ancestor-related queries to be answered efficiently in O(log N) time.

"""

# https://leetcode.com/problems/kth-ancestor-of-a-tree-node/


class TreeAncestor:

    def __init__(self, n, parent):

        self.max = 17  # 10^5 binary representation is 17 bits
        self.parent = parent
        self.n = n

        self.dp = [[-1] * (n + 1) for _ in range(self.max)]

        self.dp[0] = parent

        # for i in range(n):
        #     self.dp[0][i] = parent[i]

        for i in range(1, self.max):
            for j in range(n):
                self.dp[i][j] = self.dp[i - 1][self.dp[i - 1][j]]

    def getKthAncestor(self, node, k):

        for i in range(self.max):
            if k & (1 << i):
                node = self.dp[i][node]

        return node


obj = TreeAncestor(5, [-1, 0, 0, 1, 2])
print(obj.getKthAncestor(3, 5))
print(obj.getKthAncestor(3, 2))
print(obj.getKthAncestor(2, 2))
print(obj.getKthAncestor(0, 2))
print(obj.getKthAncestor(2, 1))
