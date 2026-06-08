# https://leetcode.com/problems/shortest-path-visiting-all-nodes

from collections import deque

# TC: O(n * 2^n) where n is the number of nodes in the graph
# SC: O(n * 2^n) for the seen set and the queue
class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:

        n = len(graph)

        # Agar graph mein sirf 1 hi node hai, toh 0 steps lagenge
        if n == 1:
            return 0

        # Target mask: agar n=4 hai, toh 1111 (binary) yani 15 (decimal)
        target_mask = (1 << n) - 1

        # Queue mein store karenge: (current_node, mask)
        queue = deque()

        # Visited set mein store karenge unique state: (current_node, mask)
        visited = set()

        # Hum kisi bhi node se shuru kar sakte hain, toh sabko queue mein daal do 0 steps ke saath
        for i in range(n):
            mask = 1 << i
            queue.append((i, mask, 0)) # (node, mask, steps)
            visited.add((i, mask))

        # Standard BFS
        while queue:

            curr_node, curr_mask, steps = queue.popleft()

            # Agar saare nodes visit ho gaye, toh yahi shortest path hai!
            if curr_mask == target_mask:
                return steps

            # Ab iske saare padosi (neighbors) par jao
            for neighbor in graph[curr_node]:

                # Naya mask banega padosi ko include karke
                next_mask = curr_mask | (1 << neighbor)

                # Agar yeh (neighbor, next_mask) wali state pehle nahi dekhi
                if (neighbor, next_mask) not in visited:
                    visited.add((neighbor, next_mask))
                    queue.append((neighbor, next_mask, steps + 1))

        return -1


print(Solution().shortestPathLength([[1, 2, 3], [0], [0], [0]]))  # Output: 4
print(Solution().shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]))  # Output: 4