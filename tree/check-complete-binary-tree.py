# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        have_null = False
        q = [root]
        
        while q:

            node = q.pop(0)

            if not node: 
                have_null = True
                continue

            # there is a node but left side is null
            # data must be filled from left to right
            if have_null:
                return False

            q.append(node.left)
            q.append(node.right)
            
        return True
