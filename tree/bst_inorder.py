class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        self.res = []
        def helper(node):
            if node:
                helper(node.left)
                self.res.append(node.val)
                helper(node.right)
        helper(root)
        return self.res
    
print(Solution().inorderTraversal(TreeNode(20, TreeNode(10, None, TreeNode(15)))))  # [10,15,20]
print(Solution().inorderTraversal(TreeNode(1, TreeNode(2), TreeNode(3))))  # [2, 1, 3]