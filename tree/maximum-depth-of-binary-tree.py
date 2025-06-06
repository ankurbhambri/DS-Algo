class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):

        if not root:
            return 0

        res = 0
        q = [root]
        level = []

        while q:

            for node in q:

                if node.left:
                    level.append(node.left)

                if node.right:
                    level.append(node.right)

            q = level
            level = []

            res += 1

        return res
    
print(Solution().maxDepth(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4))))  # Output: 3
print(Solution().maxDepth(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))))  # Output: 3
print(Solution().maxDepth(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))))  # Output: 4
print(Solution().maxDepth(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, TreeNode(5)))))  # Output: 3
print(Solution().maxDepth(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, TreeNode(5, TreeNode(6))))))  # Output: 4
print(Solution().maxDepth(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, TreeNode(5, TreeNode(6, TreeNode(7)))))))  # Output: 5