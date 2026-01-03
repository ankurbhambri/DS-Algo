"""
    Shortest path algorithm works may work in negative weights or may not

It runs only one iterations - o(n^2) best and worst o(n^3)

TC:
- O((V + E) log V) - E is the number of edges, V is the number of vertices using priority queue aka Min Heap
- O(E log V) for the priority queue operations
- O(V) for the initialization of the distances

TC worst case is O(n^2) in case of n vertices processed and n vertex relaxed

# To find the shortest path in unweighted graphs - BFS
# To find the shortest path in Weighted Graphs - Dijkstra's

https://leetcode.com/discuss/post/7322154/10-dijkstra-variations-for-interview-pre-s8by/

"""

import heapq
from collections import defaultdict, deque

# For Unweighted Graphs (BFS)
def bfs_shortest_path(graph, root):

    # distance dict
    distances = {node: float("inf") for node in graph}
    distances[root] = 0

    queue = deque([root])

    while queue:

        current_node = queue.popleft()

        for neighbor in graph[current_node]:

            if distances[neighbor] == float("inf"):

                distances[neighbor] = distances[current_node] + 1
                queue.append(neighbor)

    return distances


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print(bfs_shortest_path(graph, "A"))


# For Weighted Graphs (Dijkstra's)
def dijkstra(graph, N, start):

    adj = defaultdict(list)

    for u, v, w in graph:
        adj[u].append((v, w))

    dist = {i: float("inf") for i in range(N)}
    dist[start] = 0

    minHeap = [(0, start)]  # (cost_so_far, current_node)

    while minHeap:

        # weight, node
        weight, node = heapq.heappop(minHeap)

        # If current cost is more than known cost, skip
        if weight > dist[node]:
            continue

        for child, child_weight in adj[node]:
            # Relaxtion
            new_dist = dist[node] + child_weight

            if dist[child] > new_dist:
                dist[child] = new_dist
                heapq.heappush(minHeap, (new_dist, child))

    return dist


# graph = [2 (U), 1 (V), 1 (Weight)]
print(
    dijkstra([[1, 2, 5], [1, 3, 2], [2, 4, 4], [3, 2, 1], [3, 4, 4]], N=5, start=1)
)  # o/p {1: 0, 2: 3, 3: 2, 4: 6}

"""
    https://leetcode.com/problems/network-delay-time/
    Used Dijkstra's algorithm here - TC - O(E log N), SC - O(E + N) 
"""

def networkDelayTime(times, n: int, k: int) -> int:

    adj = defaultdict(list)

    for u, v, w in times:
        adj[u].append((v, w))

    # Here, k is the starting node so will keep its distance as 0
    dist = {node: float("inf") for node in range(1, n + 1)}
    dist[k] = 0

    hm = [(0, k)]

    while hm:
        time, node = heapq.heappop(hm)

        if time < dist[node]:
            continue

        for nei, t in adj[node]:
            new_t = time + t
            
            if new_t < dist[nei]:
                dist[nei] = new_t
                heapq.heappush(hm, (new_t, nei))

    res = max(dist.values())
    return -1 if res == float("inf") else res


print(networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))

# https://leetcode.com/problems/path-with-maximum-probability/

# Here, we want to maximize the success probability, so will user max-heap
def maxProbability(n: int, edges, succProb, start_node: int, end_node: int) -> float:

    adj = defaultdict(list)

    for (u, v), p in zip(edges, succProb):
        adj[u].append((v, p))
        adj[v].append((u, p))

    dist = [0.0] * n
    dist[start_node] = 1.0
    
    # Use negative probability to simulate max-heap
    heap = [(-1.0, start_node)]  # (negated probability, node)

    while heap:
        neg_prob, node = heapq.heappop(heap)
        prob = -neg_prob  # convert back to positive

        # Early exit if we've reached the end
        if node == end_node:
            return prob

        for nei, edge_prob in adj[node]:
            new_prob = prob * edge_prob
            if new_prob > dist[nei]:
                dist[nei] = new_prob
                heapq.heappush(heap, (-new_prob, nei))  # max-heap behavior

    return 0.0



# https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/

def minCost(maxTime, edges, passingFees):

    n = len(passingFees)
    graph = defaultdict(list)
    
    for u, v, t in edges:
        graph[u].append((v, t))
        graph[v].append((u, t))
    
    min_time = [float("inf")] * n
    heap = [(passingFees[0], 0, 0)]
    
    while heap:
        cost, time, node = heapq.heappop(heap)

        if node == n - 1:
            return cost

        if time >= min_time[node]:
            continue

        min_time[node] = time
        
        for nei, t in graph[node]:
            new_time = time + t
            new_cost = cost + passingFees[nei]
            
            if new_time <= maxTime:
                heapq.heappush(heap, (new_cost, new_time, nei))
    
    return -1


# https://cses.fi/problemset/task/1196

def find_k_shortest_paths(n, m, k, edges):
    # Build the graph
    graph = defaultdict(list)
    for a, b, c in edges:
        graph[a].append((b, c))

    # Min-heap priority queue
    pq = [(0, 1)]  # (current_cost, current_node)

    # Tracking k shortest distances for each node
    dist = defaultdict(list)  # dist[node] will store the k smallest costs to reach node

    # BFS-style traversal using the priority queue
    while pq:
        cost, node = heapq.heappop(pq)

        # If we've already found k shortest paths to this node, skip
        if len(dist[node]) >= k:
            continue

        # Add the current path cost to the list for this node
        dist[node].append(cost)

        # Traverse neighbors
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            heapq.heappush(pq, (new_cost, neighbor))

    # Output the k shortest distances to node n
    if len(dist[n]) >= k:
        return sorted(dist[n])[:k]
    else:
        return []


# Reading input
n, m, k = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

# Finding the k shortest paths
result = find_k_shortest_paths(n, m, k, edges)

# Output the result
print(" ".join(map(str, result)))


# https://cses.fi/problemset/task/1195/

def find_min_cost_with_coupon(n, m, edges):

    graph = [[] for _ in range(n + 1)]

    for a, b, c in edges:
        graph[a].append((b, c))

    dist = [[float("inf")] * 2 for _ in range(n + 1)]
    dist[1][0] = 0  # Starting at node 1 without using a coupon

    # (current_cost, current_node, coupon_used)
    pq = [(0, 1, 0)]

    while pq:
        current_cost, node, coupon_used = heapq.heappop(pq)

        # If the current cost is maximum than the recorded distance, skip
        if current_cost > dist[node][coupon_used]:
            continue

        for neighbor, weight in graph[node]:

            # Option 1: Move to the next node without using a coupon
            if current_cost + weight < dist[neighbor][coupon_used]:
                dist[neighbor][coupon_used] = current_cost + weight
                heapq.heappush(pq, (dist[neighbor][coupon_used], neighbor, coupon_used))

            # Option 2: Use the coupon on this edge (if not already used)
            if not coupon_used and current_cost + weight // 2 < dist[neighbor][1]:
                dist[neighbor][1] = current_cost + weight // 2
                heapq.heappush(pq, (dist[neighbor][1], neighbor, 1))

    # minimum cost to reach node n with or without using the coupon
    return min(dist[n][0], dist[n][1])


# More Problems
# https://leetcode.com/problems/the-maze/
# https://leetcode.com/problems/the-maze-ii/
# https://leetcode.com/problems/the-maze-iii/
# https://leetcode.com/problems/modify-graph-edge-weights/
