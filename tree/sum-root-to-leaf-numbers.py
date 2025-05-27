# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root):
        
        def helper(node, path):

            if not node:
                return 0

            path = path * 10 + node.val
            
            if not node.left and not node.right:
                return path

            l = helper(node.left, path)
            r = helper(node.right, path)
            
            return l + r
        
        return helper(root, 0)
        

print(Solution().sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3))))  # Output: 25
print(Solution().sumNumbers(TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))))  # Output: 1026
print(Solution().sumNumbers(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4))))  # Output: 1234
print(Solution().sumNumbers(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(5))))  # Output: 12345
print(Solution().sumNumbers(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, TreeNode(5)))))  # Output: 12345