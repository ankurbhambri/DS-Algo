# https://leetcode.com/problems/graph-valid-tree/
# No cycle
# No multiple component in graph
class Solution:
    def validTree(self, n: int, edges):

        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    if dfs(child, node):
                        return True
                elif child != parent:
                    return True

            return False
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1  # to check this condition - a tree is an undirected graph in which any two vertices are connected by exactly one path
                if dfs(i, -1):
                    return False

        return True if res <= 1 else False
