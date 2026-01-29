# https://leetcode.com/problems/closest-binary-search-tree-value/description/

'''

Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple self.reswers, print the smallest.

Example 1:

Input: root = [4,2,5,1,3], target = 3.714286
Output: 4

Example 2:

Input: root = [1], target = 4.428571
Output: 1 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    0 <= Node.val <= 109
    -109 <= target <= 109

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC: O(h) where h is the height of the tree
# SC: O(1)
class Solution:
    def closestValue(self, root, target):

        closest = root.val

        while root:
            # Update closest if this node is nearer
            # Or if it's equally near but the value is smaller (tie-breaker)
            val = abs(root.val - target)

            if val < abs(closest - target):
                closest = root.val

            elif val == abs(closest - target):
                closest = min(closest, root.val)

            # Binary Search logic: move left or right
            if target < root.val:
                root = root.left
            else:
                root = root.right

        return closest

print(Solution().closestValue(TreeNode(1), 4.428571)) # 1
print(Solution().closestValue(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5)), 3.714286)) # 4