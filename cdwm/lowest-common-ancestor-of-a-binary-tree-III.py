
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/description/

'''

1650. Lowest Common

Ancestor of a Binary Tree III

Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}

    "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

'''

class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

# with extra space
def lowestCommonAncestor(p, q):
    
    ancestors = set()

    # Traverse from p to root and store all ancestors
    while p:
        ancestors.add(p)
        p = p.parent

    # Traverse from q to root and find the first common ancestor
    while q:

        if q in ancestors:
            return q

        q = q.parent

    return None  # If no common ancestor found (should not happen in valid input)


# Same logic can be used for linkedlists : https://leetcode.com/problems/intersection-of-two-linked-lists/

# without extra space
def lowestCommonAncestor(p_start, q_start):

    p, q = p_start, q_start

    while p != q:

        p = p.parent if p else q_start
        q = q.parent if q else p_start

    return p

# Example usage:
root = Node(3)
node5 = Node(5)
node1 = Node(1)
node6 = Node(6)
node2 = Node(2)
node0 = Node(0)
node8 = Node(8)
node7 = Node(7)
node4 = Node(4)

root.left = node5
root.right = node1

node5.parent = root
node1.parent = root

node5.left = node6
node5.right = node2

node6.parent = node5
node2.parent = node5

node2.left = node7
node2.right = node4

node7.parent = node2
node4.parent = node2

node1.left = node0
node1.right = node8

node0.parent = node1
node8.parent = node1

# tree looks like this:
#         3
#        / \
#       5   1
#      / \ / \
#     6  2 0  8
#       / \
#      7   4

# 5, 4 -> 5
print(lowestCommonAncestor(node5, node4).val)  # Output: 5

# 5, 1 -> 3
print(lowestCommonAncestor(node5, node1).val)  # Output: 3


# VARIANT: What if you were given all the nodes as a part of a vector, and no longer the root node?

'''

Given two nodes of a binary tree p and q, as well as a list of all nodes in the tree 'nodes', 
where 'nodes' is unordered, return their lowest common ancestor (LCA).

class Node {
    public int val;
    public Node left;
    public Node right;
} 

'''

def lowestCommonAncestor(nodes, p_start, q_start):
    
    parent_map = {}

    # Build parent map
    for node in nodes:

        if node.left:
            parent_map[node.left] = node

        if node.right:
            parent_map[node.right] = node

    p, q = p_start, q_start

    while p != q:

        p = parent_map.get(p, q_start)
        q = parent_map.get(q, p_start)

    return p


# Example usage:
root = Node(3)
node5 = Node(5)
node1 = Node(1)
node6 = Node(6)
node2 = Node(2)
node0 = Node(0)
node8 = Node(8)
node7 = Node(7)
node4 = Node(4)

root.left = node5
root.right = node1
node5.left = node6
node5.right = node2
node2.left = node7
node2.right = node4
node1.left = node0
node1.right = node8

nodes = [root, node5, node1, node6, node2, node0, node8, node7, node4]

# tree looks like this:
#         3
#        / \
#       5   1
#      / \ / \
#     6  2 0  8
#       / \
#      7   4

# 5, 4 -> 5
print(lowestCommonAncestor(nodes, node5, node4).val)  # Output: 5
# 5, 1 -> 3
print(lowestCommonAncestor(nodes, node5, node1).val)  # Output: 3
# TC - O(N)
# SC - O(N)
