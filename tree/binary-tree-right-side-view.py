# https://leetcode.com/problems/binary-tree-right-side-view/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):

        if not root:
            return []

        level = []
        q = [root]
        res = [root.val]

        while q:
            for node in q:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            q = level
            if level:
                res.append(level[-1].val)
            level = []

        return res


print(Solution().rightSideView(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))))  # Output: [1, 3, 4]
print(Solution().rightSideView(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))))  # Output: [1, 3, 5]


# Variant : Top View

'''

Given the root of a binary tree, imagine yourself standing on the top of it, return the values of the nodes you can see ordered from left to right.

Example 1:
Input: root = [1,2,3, null,5, null, 4]
Output: [2,1,3,4]

Example 2:
Input: root = [1,2,3,4, null, null, null, 5]
Output: [5,4,2,1,3]

Example 3:
Input: root = [1, null, 3]
Output: [1,3]

Constraints:
• The number of nodes in the tree is in the range [0, 100].
• -100 <= Node.val <= 100

'''


from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# TC: O(N Log N), bcoz of sorting
# SC: O(N)

def topView(root):

    if not root:
        return []

    col_map = {}  # col -> node.val
    q = deque([(root, 0)])  # (node, horizontal distance)

    while q:
        node, col = q.popleft()

        if col not in col_map:
            col_map[col] = node.val  # first time seeing this col

        if node.left:
            q.append((node.left, col - 1))
        if node.right:
            q.append((node.right, col + 1))

    # Sort by horizontal distance
    return [col_map[col] for col in sorted(col_map.keys())]


print(topView(TreeNode(42, TreeNode(66, None, TreeNode(98)), TreeNode(10, None, None))))  # Output: [66, 42, 10]
print(topView(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))))  # Output: [4, 2, 1, 3, 5]
print(topView(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))))  # Output: [5, 4, 2, 1, 3]


# Optimised approach - TC: O(N), using min and max variables

def topView(root):

    if not root:
        return []

    col_map = {}  # col -> node.val

    q = deque([(root, 0)])  # (node, horizontal distance)

    min_col, max_col = 0, 0 # keeping track of min and max horizontal distance, this will allow us to loop through left to right node, instead sorting in the end based on keys.

    while q:

        node, col = q.popleft()

        min_col = min(min_col, col)
        max_col = max(max_col, col)

        if col not in col_map:
            col_map[col] = node.val  # first time seeing this col

        if node.left:
            q.append((node.left, col - 1))
        if node.right:
            q.append((node.right, col + 1))

    # Sort by horizontal distance
    return [col_map[col] for col in range(min_col, max_col + 1) if col in col_map]


print(topView(TreeNode(42, TreeNode(66, None, TreeNode(98)), TreeNode(10, None, None))))  # Output: [66, 42, 10]
print(topView(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))))  # Output: [4, 2, 1, 3, 5]
print(topView(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))))  # Output: [5, 4, 2, 1, 3]
