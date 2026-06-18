# https://leetcode.com/problems/valid-arrangement-of-pairs/

from collections import defaultdict


class Solution: 
    def validArrangement(self, pairs):
        ind = defaultdict(int)
        oud = defaultdict(int)
        adj = defaultdict(list)

        for u, v in pairs:
            oud[u] += 1
            ind[v] += 1
            adj[u].append(v)

        # Find the start node
        st = pairs[0][0]
        for node in adj:
            if oud[node] - ind[node] == 1:  # Start node for Eulerian path
                st = node
                break

        # Hierholzer's algorithm for Eulerian path
        stack = [st]
        result = []

        while stack:
            node = stack[-1]
            if adj[node]:
                next_node = adj[node].pop()
                stack.append(next_node)
            else:
                result.append(stack.pop())

        result.reverse()
        return [[result[i], result[i + 1]] for i in range(len(result) - 1)]


print(Solution().validArrangement([[1,3],[3,2],[2,1]]))  # [[1,3],[3,2],[2,1]]
print(Solution().validArrangement([[5,1],[4,5],[11,9],[9,4]]))  # [[11,9],[9,4],[4,5],[5,1]]