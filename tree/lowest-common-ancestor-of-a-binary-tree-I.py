# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: 

    The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# TC - O(N)
# SC - O(H) H - height of the tree
def lowestCommonAncestor(root, p, q):

    # Base case
    if not root:
        return None

    # if either p or q matches with root's key, report the presence by returning root, this means we found one of the nodes
    if root == p or root == q:
        return root

    # Check left and right subtrees
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    # If both left and right are non-null, that means our root is the LCA
    if left and right:
        return root

    # Otherwise, return the non-null result (or None if both null)
    return left or right


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

# tree looks like this:
#         3
#        / \
#       5   1
#      / \ / \
#     6  2 0  8
#       / \
#      7   4

p = root.left  # Node with value 5
q = root.left.right.right  # Node with value 4

print(lowestCommonAncestor(root, p, q).val)


# VARIANT: What if you were given an N-ary Tree as the input, no longer a binary tree?

class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.children = []


def lowestCommonAncestor(root, p, q):
    if not root:
        return None

    if root == p or root == q:
        return root

    matches = 0
    temp = None

    for child in root.children:
        res = lowestCommonAncestor(child, p, q)
        if res:
            matches += 1
            temp = res

    # If two or more children return non-null, this root is LCA
    if matches >= 2:
        return root

    return temp

# example:
root = Node(1)
child1 = Node(2)
child2 = Node(3)
child3 = Node(4)
root.children = [child1, child2, child3]
child1_1 = Node(5)
child1_2 = Node(6)
child1.children = [child1_1, child1_2]
child2_1 = Node(7)
child2.children = [child2_1]

# tree looks like this:
#         1
#       / | \
#      2  3  4
#     / \  \
#    5   6  7

p = child1_1  # Node with value 5
q = child1_2  # Node with value 6

print(lowestCommonAncestor(root, p, q).val)  # Output: 2

p = child1_1  # Node with value 5
q = child2_1  # Node with value 7
print(lowestCommonAncestor(root, p, q).val)  # Output: 1
