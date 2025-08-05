# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

'''
Question: Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note:
    - The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
    - A subtree of root is a tree consisting of root and all of its descendants.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        self.res = 0

        def helper(node):

            if not node:
                return 0, 0
            
            left, left_total_node = helper(node.left)
            right, right_total_node = helper(node.right)

            temp = node.val + left + right

            total_node = 1 + left_total_node + right_total_node

            if temp // total_node == node.val:
                self.res += 1

            return temp, total_node

        helper(root)

        return self.res


print(Solution().averageOfSubtree(TreeNode(4, TreeNode(8), TreeNode(5))))  # Output: 2
print(Solution().averageOfSubtree(TreeNode(1, TreeNode(2), TreeNode(3))))  # Output: 2
print(Solution().averageOfSubtree(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4)), TreeNode(5)), TreeNode(6))))  # Output: 3
print(Solution().averageOfSubtree(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, TreeNode(5), TreeNode(6)))))  # Output: 4


# Variation of this problem

'''
Given the root of a binary tree, return a boolean whether the value of every node is equal to the average of the values in its subtree.

Note:
• The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
• A subtree of root is a tree consisting of root and all of its descendants.

'''

# In above code will just match with the total node count with the condition matching variable if both are equal then return True else False


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        def helper(node):

            if not node:
                return 0, 0

            left, left_total_node = helper(node.left)
            right, right_total_node = helper(node.right)

            if left == -1 or right == -1:
                return -1, -1

            temp = node.val + left + right

            total_node = 1 + left_total_node + right_total_node

            if temp // total_node != node.val:
                return -1, -1

            return temp, total_node

        return helper(root) != -1


print(Solution().averageOfSubtree(TreeNode(4, TreeNode(8), TreeNode(5))))  # Output: False
print(Solution().averageOfSubtree(TreeNode(2, TreeNode(2), TreeNode(2))))  # Output: True
print(Solution().averageOfSubtree(TreeNode(3, TreeNode(3), TreeNode(3))))  # Output: True
print(Solution().averageOfSubtree(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4)), TreeNode(5)), TreeNode(6))))  # Output: False
print(Solution().averageOfSubtree(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, TreeNode(5), TreeNode(6)))))  # Output: False
