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
        q = [root]
        level = []
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

def topView(root):
    if not root:
        return []

    q = deque([(root, 0)])  # (node, horizontal distance)
    hd_map = {}  # hd -> node.val

    while q:
        node, hd = q.popleft()

        if hd not in hd_map:
            hd_map[hd] = node.val  # first time seeing this hd

        if node.left:
            q.append((node.left, hd - 1))
        if node.right:
            q.append((node.right, hd + 1))

    # Sort by horizontal distance
    return [hd_map[hd] for hd in sorted(hd_map.keys())]


print(topView(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))))  # Output: [4, 2, 1, 3, 5]
print(topView(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))))  # Output: [5, 4, 2, 1, 3]
