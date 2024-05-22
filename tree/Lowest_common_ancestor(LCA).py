# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None  # Adding parent pointer


def build_binary_tree():
    """
    Constructing a sample binary tree:
           1
         /   \
        2     3
       / \   / \
      4   5 6   7
    """

    # Creating nodes
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.parent = root
    root.right.parent = root

    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.parent = root.left
    root.left.right.parent = root.left

    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.parent = root.right
    root.right.right.parent = root.right

    return root


# Time complexity: O(h), where h is the height of the tree
# Space complexity: O(1)
def lowest_common_ancestor(p, q):
    a, b = p, q
    while a != b:
        a = a.parent if a.parent else q
        b = b.parent if b.parent else p
    return a


print(
    lowest_common_ancestor(
        build_binary_tree().left.left,
        build_binary_tree().left.right,
    )
)
# Expected output: Node(2)  # 2 is the lowest common ancestor of 4 and 5

print(lowest_common_ancestor(build_binary_tree().left.left, build_binary_tree().right))
# Expected output: Node(2)  # 1 is the lowest common ancestor of 4 and 3


# Similar problem based on same logic from LeetCode: https://leetcode.com/problems/intersection-of-two-linked-lists/
