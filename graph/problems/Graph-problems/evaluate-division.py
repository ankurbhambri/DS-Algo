from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:

        graph = defaultdict(list)

        # Step 1: Build the graph
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))       # a / b = val
            graph[b].append((a, 1 / val))   # b / a = 1 / val

        # Step 2: DFS to find the result
        def dfs(src, dst, visited, acc_product):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return acc_product
            visited.add(src)
            for neighbor, weight in graph[src]:
                if neighbor in visited:
                    continue
                result = dfs(neighbor, dst, visited, acc_product * weight)
                if result != -1.0:
                    return result
            return -1.0

        res = []
        for src, dst in queries:
            res.append(dfs(src, dst, set(), 1.0))

        return res

print(Solution().calcEquation(
    [["a", "b"], ["b", "c"]],
    [2.0, 3.0],
    [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
))  # Output: [6.0, 0.5, -1.0, 1.0, -1.0]