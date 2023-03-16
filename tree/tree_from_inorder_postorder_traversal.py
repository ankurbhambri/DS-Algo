# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        pos = inorder.index(postorder[-1]) if inorder else -1
        
        return TreeNode(
            postorder[-1],
            self.buildTree(inorder[:pos], postorder[:pos]),
            self.buildTree(inorder[pos + 1:], postorder[pos: -1])
        ) if pos>-1 else None
