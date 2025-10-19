# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):

        graph = defaultdict(list)

        def helper(cur):

            if cur is None:
                return

            if cur.left:
                graph[cur.val].append(cur.left.val)
                graph[cur.left.val].append(cur.val)

            if cur.right:
                graph[cur.val].append(cur.right.val)
                graph[cur.right.val].append(cur.val)

            helper(cur.left)
            helper(cur.right)

        helper(root)
        
        res = []
        visited = set([target.val])
        queue = deque([(target.val, 0)])

        while queue:

            cur, distance = queue.popleft()

            if distance == k:
                res.append(cur)
                continue

            for neighbor in graph[cur]:

                if neighbor not in visited:

                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))

        return res
