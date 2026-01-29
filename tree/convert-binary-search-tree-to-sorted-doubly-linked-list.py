# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/

# https://github.com/doocs/leetcode/blob/main/solution/0400-0499/0426.Convert%20Binary%20Search%20Tree%20to%20Sorted%20Doubly%20Linked%20List/README_EN.md

'''
    Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

    You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. 

    For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

    We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, 

    and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

'''

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root):

        if not root:
            return None

        self.first = None
        self.last = None

        self.inorder(root)

        # Make it circular
        self.last.right = self.first
        self.first.left = self.last

        return self.first

    def inorder(self, node):

        if not node:
            return

        # Left
        self.inorder(node.left)

        # Node (Link the predecessor)
        if self.last:
            self.last.right = node
            node.left = self.last
        else:
            # This is the smallest node
            self.first = node

        self.last = node

        self.inorder(node.right)

print(Solution().treeToDoublyList(Node(4, Node(2, Node(1), Node(3)), Node(5))))


# Variant

'''

Convert a Binary Tree to a Circular Doubly-Linked List according to its Inorder Traversal in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. 
For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor,
and the right pointer should point to its successor. You should return the pointer to the first element processed (by the inorder traversal) of the linked list.

'''

# Code and Logic is same as above variant, only difference is that here its a Binary Tree, not BST.