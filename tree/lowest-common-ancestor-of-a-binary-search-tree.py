# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# TC: O(H) where H is the height of the tree
# SC: O(1)
class Solution:
    def lowestCommonAncestor(self, root, p, q):

        curr = root
        
        while curr:

            curr_val = curr.val
            p_val = p.val
            q_val = q.val
            
            # If both p and q are smaller, go left
            if p_val < curr_val and q_val < curr_val:
                curr = curr.left

            # If both p and q are larger, go right
            elif p_val > curr_val and q_val > curr_val:
                curr = curr.right

            # If one is smaller and one is larger (or equal), current node is LCA
            else:
                return curr
        
        return None  # Unreachable due to problem constraints