# https://leetcode.com/problems/create-binary-tree-from-descriptions


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TC: O(n)
# SC: O(n)
class Solution:
    def createBinaryTree(self, descriptions):

        chlid_nodes = set([v for _, v, _ in descriptions])

        parent = [u for u, v, i in descriptions if u not in chlid_nodes]

        if not parent:
            return None

        adj = {u: [] for u, v, i in descriptions}

        for u, v, l in descriptions:
            adj[u].append([v, l])        

        visit = set()

        def dfs(node):

            visit.add(node.val)

            if node.val not in adj:
                return

            for ch, l in adj[node.val]:

                if ch not in visit:

                    newNode = TreeNode(ch)

                    if l == 1:
                        node.left = newNode

                    else:
                        node.right = newNode

                    dfs(newNode)

        node = TreeNode(parent[0])
        dfs(node)

        return node