from collections import defaultdict
from heapq import heappop, heappush


def countPaths(n, roads):
    MOD = 10**9 + 7
    
    # Step 1: Adjacency list banao
    adj = defaultdict(list)
    for u, v, t in roads:
        adj[u].append((v, t))
        adj[v].append((u, t))  # Undirected graph
    
    # Step 2: Arrays initialize karo
    dist = [float('inf')] * n  # Shortest time to each node
    ways = [0] * n            # Ways to reach each node in shortest time
    dist[0] = 0               # Start node ka time 0
    ways[0] = 1               # Start node tak 1 tareeka
    
    # Step 3: Priority queue (min-heap) for Dijkstra’s
    pq = [(0, 0)]  # (time, node)
    
    # Step 4: Process nodes
    while pq:
        time, u = heappop(pq)
        
        if time > dist[u]:
            continue
        
        for v, t in adj[u]:
            new_time = time + t
            
            if new_time < dist[v]:
                dist[v] = new_time    # Update shortest time
                ways[v] = ways[u]     # Ways copy from u
                heappush(pq, (new_time, v))
            
            # Case 2: If new time equal  to shortest time
            elif new_time == dist[v]:
                ways[v] = (ways[v] + ways[u]) % MOD  # Ways added
            
    return ways[n-1]

# Example usage
print(countPaths(7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]])) # Output: 4
print(countPaths(5, [[0, 1, 1], [0, 2, 2], [1, 2, 1], [1, 3, 2], [2, 3, 1], [3, 4, 1]])) # Output: 3
print(countPaths(3, [[0, 1, 1], [1, 2, 2], [0, 2, 2]])) # Output: 1
print(countPaths(4, [[0, 1, 2], [1, 2, 3], [2, 3, 4], [0, 3, 5]])) # Output: 1
