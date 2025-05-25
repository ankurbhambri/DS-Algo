# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

'''
The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):
    # Base case: empty node or found p or q
    if not root or root == p or root == q:
        return root
    
    # Check left and right subtrees
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    # If both left and right are non-null, root is LCA
    if left and right:
        return root
    
    # Otherwise, return the non-null result (or None if both null)
    return left if left else right 


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

p = root.left  # Node with value 5
q = root.left.right.right  # Node with value 4

print(lowestCommonAncestor(root, p, q).val)
