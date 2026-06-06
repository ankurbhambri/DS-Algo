# https://leetcode.com/problems/maximum-sum-bst-in-binary-tree

# similar to largest bst in binary tree - https://www.geeksforgeeks.org/dsa/largest-bst-binary-tree-set-2/
# difference is instead of calculating the size of the bst we need to calculate the max sum of the bst.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:

        self.ans = 0

        def dfs(node):

            if not node:
                return True, 0, float("inf"), float("-inf")

            l_bst, l_sum, l_min, l_max = dfs(node.left)

            r_bst, r_sum, r_min, r_max = dfs(node.right)

            if l_bst and r_bst and l_max < node.val < r_min:

                sm = l_sum + node.val + r_sum

                self.ans = max(self.ans, sm)

                return True, sm, min(l_min, node.val), max(node.val, r_max)

            return False, 0, 0, 0

        dfs(root)

        return self.ans