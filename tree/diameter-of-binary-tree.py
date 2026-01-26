# https://leetcode.com/problems/diameter-of-binary-tree/description/
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
def diameter_of_binary_tree(root):

    d = 0

    def helper(node):

        nonlocal d

        if not node:
            return 0

        l = helper(node.left)
        r = helper(node.right)

        d = max(d, l + r)

        return max(l, r) + 1

    helper(root)

    return d


# Constructing the example tree
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(f"The diameter of the tree is: {diameter_of_binary_tree(root)}")


# Variant: How do you find the diameter of an N-ary tree? It’s no longer a binary tree where you only have up to 2 children nodes.

# Please see the file: tree/diameter-of-n-ary-tree.py + n-ary-tree-postorder-traversal.py