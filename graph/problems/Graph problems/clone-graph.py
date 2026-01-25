# https://leetcode.com/problems/clone-graph/description/

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, root):

        if not root:
            return None

        # mapping of original nodes to cloned nodes
        cloned_nodes = {}

        def dfs(node):

            if node in cloned_nodes:
                return cloned_nodes[node]

            # Create a new node for the cloned graph
            clone = Node(node.val)
            cloned_nodes[node] = clone

            # Recursively clone the neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(root)


obj = Node(1)
obj.neighbors.append(Node(2))
obj.neighbors.append(Node(3))
obj.neighbors[0].neighbors.append(obj.neighbors[1])  # 2 -> 3
obj.neighbors[1].neighbors.append(obj.neighbors[0])  # 3 -> 2
print(Solution().cloneGraph(obj))  # Should return a deep copy of the graph starting from node 1