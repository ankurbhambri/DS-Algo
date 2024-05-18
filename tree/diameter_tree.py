class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
def diameter_of_binary_tree(root):
    diameter = 0

    def height_and_diameter(node):

        nonlocal diameter

        if not node:
            return 0

        left_height = height_and_diameter(node.left)
        right_height = height_and_diameter(node.right)

        diameter = max(diameter, left_height + right_height)

        return max(left_height, right_height) + 1

    height_and_diameter(root)
    return diameter


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
