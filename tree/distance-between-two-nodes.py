# https://www.geeksforgeeks.org/dsa/find-distance-between-two-nodes-of-a-binary-tree/

'''

Formula to find distance between two nodes U and V in a binary tree:

Method 1: Using root and LCA (Lowest Common Ancestor)

    Dist(U, V) = Dist(root, U) + Dist(root, V) - 2 x Dist(root, LCA)

Method 2: Using LCA directly

    Dist(U, V) = Dist(LCA, U) + Dist(LCA, V)

                   1
                 /   \
                2     3
               / \   / \
              4   5 6   7

Example: Find distance between 4 and 5

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findDistance(self, root, p, q):

        def lca(node):

            if node is None:
                return None

            if node.val == p or node.val == q:
                return node

            left = lca(node.left)
            right = lca(node.right)

            if left and right:
                return node

            return left or right

        def distance(node, target, dist):

            if node is None:
                return -1

            if node.val == target:
                return dist

            left = distance(node.left, target, dist + 1)

            if left != -1:
                return left

            return distance(node.right, target, dist + 1)

        ancestor = lca(root)

        return distance(ancestor, p, 0) + distance(ancestor, q, 0)


print(Solution().findDistance(TreeNode(1), 4, 5))
print(Solution().findDistance(TreeNode(1), 4, 6))