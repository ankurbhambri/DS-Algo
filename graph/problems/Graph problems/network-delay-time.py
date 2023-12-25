# https://leetcode.com/problems/network-delay-time/

# Used Dijkstra's algorithm here - TC - O(E log N), SC - O(E + N)


import heapq


class Solution:
    def networkDelayTime(self, times, N: int, K: int) -> int:
        # adjacency list representation of the graph
        graph = {i: {} for i in range(1, N + 1)}
        for u, v, w in times:
            graph[u][v] = w

        # Initialize distances with infinity for all nodes except the source
        distances = {node: float("inf") for node in range(1, N + 1)}
        distances[K] = 0

        # Priority queue to store vertices and their distances
        pq = [(0, K)]  # Tuple: (distance, vertex)
        heapq.heapify(pq)

        while pq:
            dist, node = heapq.heappop(pq)
            if dist > distances[node]:
                continue

            # Traverse neighbors of the current node
            for neighbor, weight in graph[node].items():
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        max_time = max(distances.values())
        return max_time if max_time < float("inf") else -1


obj = Solution()
# times, N, K
print(obj.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
