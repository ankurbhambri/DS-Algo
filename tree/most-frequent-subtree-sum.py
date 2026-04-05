# https://leetcode.com/problems/most-frequent-subtree-sum/

# TC: O(N) where N is number of nodes in the tree
# SC: O(N) in worst case when all nodes have unique subtree sum

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root):

        self.sum_freq = {}
        self.max_freq = 0
        
        def helper(root) -> int:

            if not root:
                return 0

            # Get left and right subtree's sum.
            left_subtree_sum = helper(root.left)
            right_subtree_sum = helper(root.right)

            # Use child's tree's sums to get current root's tree's sum
            curr_sum = root.val + left_subtree_sum + right_subtree_sum

            self.sum_freq[curr_sum] = self.sum_freq.get(curr_sum, 0) + 1
            self.max_freq = max(self.max_freq, self.sum_freq[curr_sum])
            return curr_sum

        # Traverse on all nodes one by one, and find it's tree's sum.
        helper(root)
        max_freq_sums = []
        for val in self.sum_freq:
            if self.sum_freq[val] == self.max_freq:
                max_freq_sums.append(val)

        return max_freq_sums