# https://leetcode.com/problems/shortest-path-visiting-all-nodes

from collections import deque

class Solution:
    def shortestPathLength(self, graph):

        n = len(graph)
        goal = (1 << n) - 1

        ans = 0
        q = deque()  # (u, state)
        seen = set()

        for i in range(n):
            q.append((i, 1 << i))

        while q:

            for _ in range(len(q)):
                u, state = q.popleft()

                if state == goal:
                    return ans

                if (u, state) in seen:
                    continue

                seen.add((u, state))

                for v in graph[u]:
                    q.append((v, state | (1 << v)))

            ans += 1

        return -1


print(Solution().shortestPathLength([[1, 2, 3], [0], [0], [0]]))  # Output: 4
print(Solution().shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]))  # Output: 4