'''Longest path to the bottom of a Binary Tree forming an Arithmetic Progression'''

'''
    Given a Binary Tree consisting of N nodes, the task is to find the length of
    the longest path from any node to the bottom of the tree such that all the node
    values form an Arithmetic Progression.
'''


class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


class Solution:
    def maximumLengthAP(self, root):
        self.res = 0

        # Base Cases
        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 1

        def dfs(node, cur_diff, count):

            if node.left:
                diff = node.left.val - node.val

                if diff == cur_diff:
                    dfs(node.left, cur_diff, count + 1)
                    self.res = max(self.res, count + 1)
                else:
                    dfs(node.left, diff, 2)
            if node.right:
                diff = node.right.val - node.val
                if diff == cur_diff:
                    dfs(node.right, cur_diff, count + 1)
                    self.res = max(self.res, count + 1)
                else:
                    dfs(node.right, diff, 2)

        # If the root's left child exists
        if root.left:
            difference = root.left.val - root.val
            dfs(root.left, difference, 2)

        # If the root's right child exists
        if root.right:
            difference = root.right.val - root.val
            dfs(root.right, difference, 2)

        return self.res


# Given Tree
root = Node(6)
root.right = Node(9)
root.right.left = Node(7)
root.right.right = Node(12)
root.right.right.right = Node(15)

obj = Solution()
print(obj.maximumLengthAP(root))
