# https://www.geeksforgeeks.org/dsa/largest-bst-binary-tree-set-2/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestBST(self, root: TreeNode) -> int:

        self.ans = 0

        def dfs(node):

            if not node:
                return True, 0, float('inf'), float('-inf')

            l_bst, l_size, l_min, l_max = dfs(node.left)

            r_bst, r_size, r_min, r_max = dfs(node.right)

            if l_bst and r_bst and l_max < node.data < r_min:

                size = l_size + r_size + 1

                self.ans = max(self.ans, size)

                return (True, size, min(l_min, node.data), max(node.data, r_max))

            return False, 0, 0, 0

        dfs(root)

        return self.ans


print(Solution().largestBST(TreeNode(5, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(4))))  # 3
print(Solution().largestBST(TreeNode(10, TreeNode(5, TreeNode(1), TreeNode(8)), TreeNode(15, None, TreeNode(7)))))  # 3