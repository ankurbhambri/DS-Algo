from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        # BFS: queue with (node, depth)
        queue = deque([(root, 1)])
        
        while queue:
            node, depth = queue.popleft()
            
            # If leaf node found, return its depth
            if not node.left and not node.right:
                return depth
            
            # Add children to queue with incremented depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))


    def maxDepth(self, root: TreeNode) -> int:
            # Empty tree
            if not root:
                return 0
            
            # BFS: queue with nodes
            queue = deque([root])
            depth = 0
            
            while queue:
                level_size = len(queue)
                depth += 1  # Increment depth for current level
                
                # Process all nodes at current level
                for _ in range(level_size):
                    node = queue.popleft()
                    
                    # Add children to queue
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            
            return depth


