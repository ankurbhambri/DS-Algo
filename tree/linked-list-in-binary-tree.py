# https://leetcode.com/problems/linked-list-in-binary-tree/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TC: O(n * m) where n is the number of nodes in the binary tree and m is the number of nodes in the linked list
# SC: O(h) where h is the height of the binary tree for the recursion stack
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        # If the tree is empty, we can't match any list
        if not root:
            return False

        # Check if the path matches starting from the current root node,
        # OR if it matches starting from anywhere in the left or right subtrees.
        return (
            self.checkPath(head, root) or 
            self.isSubPath(head, root.left) or 
            self.isSubPath(head, root.right)
        )

    def checkPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        # Base Case 1: If we successfully reached the end of the linked list, we found a match
        if not head:
            return True

        # Base Case 2: If the tree path ends before the linked list does, match fails
        if not root:
            return False

        # Base Case 3: If values don't match, this path is invalid
        if head.val != root.val:
            return False

        # Recursively check the next element of the linked list in both children
        return self.checkPath(head.next, root.left) or self.checkPath(head.next, root.right)


# KMP approach

# TC: O(n + m) where n is the number of nodes in the binary tree and m is the number of nodes in the linked list
# SC: O(m) for the lps array and O(h) for the recursion stack where h is the height of the binary tree
class Solution:
    def isSubPath(self, head, root):

        # Linked List -> Array
        pattern = []

        while head:
            pattern.append(head.val)
            head = head.next

        m = len(pattern)

        # Build LPS
        lps = [0] * m

        j = 0
        for i in range(1, m):

            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]

            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j

        def dfs(node, j):

            if not node:
                return False

            while j > 0 and node.val != pattern[j]:
                j = lps[j - 1]

            if node.val == pattern[j]:
                j += 1

            if j == m:
                return True

            return dfs(node.left, j) or dfs(node.right, j)

        return dfs(root, 0)