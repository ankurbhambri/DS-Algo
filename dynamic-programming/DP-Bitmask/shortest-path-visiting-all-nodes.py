# https://leetcode.com/problems/shortest-path-visiting-all-nodes

from collections import deque

# TC: O(n * 2^n) where n is the number of nodes in the graph
# SC: O(n * 2^n) for the seen set and the queue
class Solution:
    def shortestPathLength(self, graph):

        n = len(graph)

        final_mask = (1 << n) - 1

        q = deque()
        visited = set()

        for i in range(n):

            mask = 1 << i

            q.append((i, mask, 0))
            visited.add((i, mask))

        while q:

            node, mask, dist = q.popleft()

            if mask == final_mask:
                return dist

            for nei in graph[node]:

                new_mask = mask | (1 << nei)

                state = (nei, new_mask)

                if state not in visited:

                    visited.add(state)
                    q.append((nei, new_mask, dist + 1))


print(Solution().shortestPathLength([[1, 2, 3], [0], [0], [0]]))  # Output: 4
print(Solution().shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]))  # Output: 4