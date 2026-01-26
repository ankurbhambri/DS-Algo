# Note: please go throught the copy-list-with-random-pointer.py file for similar problem on linked list.

# https://leetcode.com/problems/clone-binary-tree-with-random-pointer/description/

'''

A binary tree is given such that each node contains an additional random pointer which could point to any node in the tree or null. Return a deep copy of the tree.

The tree is represented in the same input/output way as normal binary trees where each node is represented as a pair of [val, random_index] where:
    val: an integer representing Node.val

    random_index: the index of the node (in the input) where the random pointer points to, or null if it does not point to any node.


You will be given the tree in class Node and you should return the cloned tree in class NodeCopy. 

NodeCopy class is just a clone of Node class with the same attributes and constructors.

Example 1:

Input: root = [[1,null],null,[4,3],[7,0]]
Output: [[1,null],null,[4,3],[7,0]]

Explanation: The original binary tree is [1,null,4,7].
The random pointer of node one is null, so it is represented as [1, null].
The random pointer of node 4 is node 7, so it is represented as [4, 3] where 3 is the index of node 7 in the array representing the tree.
The random pointer of node 7 is node 1, so it is represented as [7, 0] where 0 is the index of node 1 in the array representing the tree.

Example 2:

Input: root = [[1,4],null,[1,0],null,[1,5],[1,5]]
Output: [[1,4],null,[1,0],null,[1,5],[1,5]]

Explanation: The random pointer of a node can be the node itself.

Example 3:

Input: root = [[1,6],[2,5],[3,4],[4,3],[5,2],[6,1],[7,0]]
Output: [[1,6],[2,5],[3,4],[4,3],[5,2],[6,1],[7,0]]

Constraints:

    The number of nodes in the tree is in the range [0, 1000].
    1 <= Node.val <= 106

'''



# Definition for Node.
class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


# DFS + HashMap approach
# TC: O(n)
# SC: O(n)
class Solution:
    def copyRandomBinaryTree(self, root):

        mp = {}

        def dfs(root):

            if root is None:
                return None

            if root in mp:
                return mp[root]

            copy = Node(root.val)

            mp[root] = copy

            copy.left = dfs(root.left)
            copy.right = dfs(root.right)
            copy.random = dfs(root.random)

            return copy

        return dfs(root)


# BFS + HashMap approach

from collections import deque

# TC: O(n)
# SC: O(n)
class Solution:
    def copyRandomBinaryTree(self, root):

        if not root:
            return None

        # Mapping: {Original Node -> Cloned Node}
        mapping = {}

        # Step 1: BFS use karke saare nodes clone karo aur mapping mein daalo
        queue = deque([root])
        while queue:

            curr = queue.popleft()

            mapping[curr] = Node(curr.val)

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        # Step 2: BFS use karke connections (left, right, random) set karo
        queue = deque([root])
        while queue:

            curr = queue.popleft()
            cloned = mapping[curr]

            # Mapping se connections uthao
            if curr.left:
                cloned.left = mapping[curr.left]

            if curr.right:
                cloned.right = mapping[curr.right]

            if curr.random:
                cloned.random = mapping[curr.random]

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        return mapping[root]