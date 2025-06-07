# https://leetcode.com/problems/delete-node-in-a-bst/description/

# Inorder Successor means the smallest node in the right subtree.
# Inorder Predecessor means the largest node in the left subtree.

# Time: O(H) where H = height of tree, (In worst case, unbalanced tree ⇒ O(N))
# Space: O(H) recursive stack

class Solution(object):
    def deleteNode(self, root, key):

        # If tree is empty or we've reached a null node
        if not root:
            return None

        # Case when we found Node to delete found
        if root.val == key:

            # Case 1a: No left child, return right child
            if not root.left:
                return root.right

            # Case 1b: No right child, return left child
            if not root.right:
                return root.left

            # In case, Node has both left and right children
            temp = root.right
            while temp.left:
                temp = temp.left  # leftmost node in right subtree

            # Replace current node's value with inorder successor's value
            root.val = temp.val

            # Now delete the inorder successor from right subtree
            root.right = self.deleteNode(root.right, root.val)

        # Recursion on left side if key is smaller.
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        # Recursion on right side if key is larger.
        else:
            root.right = self.deleteNode(root.right, key)

        return root


print(Solution().deleteNode(root=[5,3,6,2,4,None,7],key=3))  # Output: [5,4,6,2,null,null,7]
print(Solution().deleteNode(root=[5,3,6,2,4,None,7],key=5))  # Output: [6,3,null,2,4,null,7] (root node deleted)
print(Solution().deleteNode(root=[5,3,6,2,4,None,7],key=6))  # Output: [5,3,null,2,4,null,7] (node with value 6 deleted)
print(Solution().deleteNode(root=[5,3,6,2,4,None,7],key=0))  # Output: [5,3,6,2,4,null,7] (no change since key not found)
