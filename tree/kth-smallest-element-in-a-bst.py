# https://leetcode.com/problems/kth-smallest-element-in-a-bst/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        stack = []
        curr = root
        
        while True:
            # Step 1: Sabse left tak jao
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Step 2: Element nikaalo
            curr = stack.pop()
            k -= 1 # Ek element mil gaya!
            
            # Step 3: Agar k zero ho gaya, wahi hamara answer hai
            if k == 0:
                return curr.val
            
            # Step 4: Agle bade element par jane ki taiyari (right)
            curr = curr.right