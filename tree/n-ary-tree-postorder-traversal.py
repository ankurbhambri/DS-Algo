# https://leetcode.com/problems/n-ary-tree-postorder-traversal


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# TC: O(n)
# SC: O(h) where h is the height of the tree
class Solution:
    def postorder(self, root):
        
        res = []
        # If the root is None, return the empty list

        def dfs(node):

            if node is None:
                return

            # Traverse all children first
            for child in node.children:
                dfs(child)

            # Then add the node's value to the result
            res.append(node.val)

        dfs(root)
        return res

# Iterative approach

# TC: O(n)
# SC: O(h) where h is the height of the tree
class Solution:
    def postorder(self, root):

        res = []

        # If the root is None, return the empty list
        if root is None:
            return res

        st = [(root, False)]

        while st:

            node, is_visited = st.pop()

            if is_visited:
                # If the node has been visited, add its value to the result
                res.append(node.val)

            else:
                # Mark the current node as visited and push it back to the stack
                st.append((node, True))

                # Push all children to the stack in reverse order
                for child in reversed(node.children):
                    st.append((child, False))

        return res