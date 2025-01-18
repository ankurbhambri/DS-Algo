"""
    Shortest path algorithm works may work in negative weights or may not
It runs only one iterations - o(n^2) best and worst o(n^3)

TC:
- O((V + E) log V) - E is the number of edges, V is the number of vertices using priority queue aka Min Heap
- O(E log V) for the priority queue operations
- O(V) for the initialization of the distances

TC worst case is O(n^2) in case of n vertices processed and n vertex relaxed

# For Unweighted Graphs - BFS
# For Weighted Graphs - Dijkstra's Algorithm

"""

import heapq
import math
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


def dijkstra(graph, N, start):
    adj = defaultdict(list)

    for u, v, w in graph:
        adj[u].append((v, w))

    dist = {i: float("inf") for i in range(N)}

    dist[start] = 0

    minHeap = [(0, start)]  # weight, node

    while minHeap:
        # weight, node
        weight, node = heapq.heappop(minHeap)

        """
        However, the check if dist > distances[current_node]: continue is still
        included as an optimization to improve the algorithm's efficiency.
        The reason is that when a node is added to the priority queue with a
        certain tentative distance, there may be other nodes in the queue with
        smaller tentative distances to the same node. These nodes may be processed
        later and update the distance to the same node, resulting in a shorter path.

        If we did not skip the node in the check, we would process the node again
        with a longer distance, which would not result in a shorter path and would
        slow down the algorithm unnecessarily. By skipping the node if its distance
        is already smaller than the tentative distance in the priority queue, we
        avoid processing it again and guarantee that we have found the shortest
        path to that node.

        So the check if dist > distances[current_node]: continue is a way to ensure
        that we are only processing each node once and that we are finding the
        shortest path to each node, while avoiding unnecessary computations and
        speeding up the algorithm.
        """

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
                # Relaxtion
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        max_time = max(distances.values())
        return max_time if max_time < float("inf") else -1


obj = Solution()
# times, N, K
print(obj.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))


# https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/
class Solution:
    def minCost(self, maxTime, edges, passingFees):

        n = len(passingFees)

        graph = [[] for _ in range(n)]

        for x, y, t in edges:
            graph[x].append((y, t))
            graph[y].append((x, t))

        cost = [math.inf] * n  # cost[i] := min cost to reach cities[i]
        time = [math.inf] * n  # time[i] := min cost to reach cities[i]
        minHeap = [(passingFees[0], 0, 0)]  # (cost, time, node)

        # start with node 0 with cost = time = 0
        cost[0] = passingFees[0]
        time[0] = 0

        while minHeap:
            currCost, currTime, node = heapq.heappop(minHeap)

            for child, pathTime in graph[node]:
                if currTime + pathTime <= maxTime:
                    newCost = currCost + passingFees[child]
                    newTime = currTime + pathTime

                    if cost[child] > newCost:
                        cost[child] = newCost
                        time[child] = newTime
                        heapq.heappush(minHeap, (newCost, newTime, child))

                    elif time[child] > newTime:
                        time[child] = newTime
                        heapq.heappush(minHeap, (newCost, newTime, child))

        return -1 if cost[-1] == math.inf else cost[-1]


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
# https://leetcode.com/problems/minimum-cost-to-convert-string-i/
