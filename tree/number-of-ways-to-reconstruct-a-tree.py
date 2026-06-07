# https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/

from collections import defaultdict

class Solution:
    def checkWays(self, pairs):

        graph = defaultdict(set)

        for u, v in pairs:
            graph[u].add(v)
            graph[v].add(u)

        nodes = list(graph.keys())
        n = len(nodes)

        root = -1

        for node in nodes:
            if len(graph[node]) == n - 1:
                root = node
                break

        if root == -1:
            return 0

        ans = 1

        for node in nodes:

            if node == root:
                continue

            parent = -1
            parent_degree = float('inf')

            # find parent candidate
            for nei in graph[node]:
                if len(graph[nei]) >= len(graph[node]):
                    if len(graph[nei]) < parent_degree:
                        parent_degree = len(graph[nei])
                        parent = nei

            # verify all neighbors (except parent)
            # must also belong to parent's neighbor set
            for nei in graph[node]:
                if nei == parent:
                    continue

                if nei not in graph[parent]:
                    return 0

            if len(graph[parent]) == len(graph[node]):
                ans = 2

        return 2 if ans == 2 else 1