# https://leetcode.com/problems/modify-graph-edge-weights/

import heapq

class Solution:
    def modifiedGraphEdges(self, n, edges, source, destination, target):

        def dijkstra(adj, n, src, dest):

            dist = [float('inf')] * n
            dist[src] = 0
            pq = [(0, src)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue
                for v, w in adj[u]:
                    if d + w < dist[v]:
                        dist[v] = d + w
                        heapq.heappush(pq, (dist[v], v))
            return dist[dest]

        # 1. Sirf fixed edges (weight != -1) ke saath graph banao
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            if w != -1:
                adj[u].append([v, w])
                adj[v].append([u, w])

        # Pehla check: Kya fixed edges se distance target se chota hai?
        current_dist = dijkstra(adj, n, source, destination)
        if current_dist < target:
            return []

        # Agar fixed edges se hi target mil gaya, toh saare -1 ko infinity kar do
        if current_dist == target:
            # Update edges with -1 weight to an impossible value
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = int(2e9)
            return edges
 
        found = False
        # 2. Ab ek-ek karke -1 waale edges ko process karo
        for i in range(len(edges)):

            u, v, w = edges[i]

            if w != -1:
                continue

            # Agar target mil chuka hai, baaki -1 ko max value de do
            if found:
                edges[i][2] = int(2e9)
                continue

            # Is -1 ko 1 bana kar check karo
            edges[i][2] = 1
            adj[u].append([v, 1])
            adj[v].append([u, 1])

            new_dist = dijkstra(adj, n, source, destination)

            # Agar weight 1 karne se distance target se kam ya barabar ho gaya
            if new_dist <= target:
                found = True
                # Extra weight adjust karo taaki exact target mile
                edges[i][2] += (target - new_dist)

        return edges if found else []


print(Solution().modifiedGraphEdges(3, [[0, 1, -1], [1, 2, 5]], 0, 2, 6))  # [[0,1,1],[1,2,5]]
print(Solution().modifiedGraphEdges(5, [[0, 1, -1], [0, 2, 5], [1, 2, -1], [1, 3, 8], [2, 4, -1], [3, 4, 2]], 0, 4, 20))  # [[0,1,1],[0,2,5],[1,2,14],[1,3,8],[2,4,1],[3,4,2]]