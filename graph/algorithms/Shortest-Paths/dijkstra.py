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
print(dijkstra([[1, 2, 5], [1, 3, 2], [2, 4, 4], [3, 2, 1], [3, 4, 4]], N=5, start=1))  # o/p {1: 0, 2: 3, 3: 2, 4: 6}


# https://leetcode.com/problems/network-delay-time/
# TC - O(E log N), SC - O(E + N) 

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

        if time > dist[node]:
            continue

        for nei, t in adj[node]:
            new_t = time + t
            
            if new_t < dist[nei]:
                dist[nei] = new_t
                heapq.heappush(hm, (new_t, nei))

    res = max(dist.values())
    return -1 if res == float("inf") else res


print(networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))

# https://leetcode.com/problems/path-with-minimum-effort/description/

class Solution:
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        
        # dist[r][c] = minimum effort to reach (r, c)
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        
        # min-heap: (effort_so_far, r, c)
        heap = [(0, 0, 0)]
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while heap:
            effort, r, c = heapq.heappop(heap)
            
            # If we reached destination, this is the minimum possible effort
            if r == m - 1 and c == n - 1:
                return effort
            
            # Skip stale entries
            if effort > dist[r][c]:
                continue
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    step = abs(heights[r][c] - heights[nr][nc])
                    new_effort = max(effort, step)
                    
                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))
        
        return 0

print(Solution.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))

# https://leetcode.com/problems/swim-in-rising-water/

class Solution:
    def swimInWater(self, grid):

        n = len(grid)

        # dist[r][c] = minimum time needed to reach (r, c)
        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = grid[0][0]

        # min-heap: (time_so_far, r, c)
        heap = [(grid[0][0], 0, 0)]

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while heap:
            time, r, c = heapq.heappop(heap)

            # Once we reach destination, this is the minimum possible time
            if r == n - 1 and c == n - 1:
                return time

            # Skip stale entries
            if time > dist[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    new_time = max(time, grid[nr][nc])
                    
                    if new_time < dist[nr][nc]:
                        dist[nr][nc] = new_time
                        heapq.heappush(heap, (new_time, nr, nc))

        return -1     

# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

# Time: O(n * len(flights) * log(n))
# Space: O(n)

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):

        adj = {i: [] for i in range(n)}

        for u, v, price in flights:
            adj[u].append((v, price))

        visit = [float("inf")] * n

        q = [(0, -1, src)] # cost, steps, node

        while q:
            cost, steps, node = heapq.heappop(q)

            # Have seen the node already, and the current steps are more than last time
            if visit[node] <= steps:  
                continue

            if steps > k: # More than k stops, invalid
                continue

            if node == dst:
                return cost

            visit[node] = steps

            for nei, weight in adj[node]: # weight means cost
                heapq.heappush(q, (cost + weight, steps + 1, nei))

        return -1


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


# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/

# TC: O(m * n * log(m * n)) - We process each cell at most once, and each cell has up to 4 neighbors. The priority queue operations take O(log(m * n)) time.
# SC: O(m * n) - We maintain a cost array of size m * n and a priority queue that can hold up to m * n entries in the worst case.
class Solution:
    def minCost(self, grid):

        m, n = len(grid), len(grid[0])

        # Directions: Right, Left, Down, Up (matching 1,2,3,4)
        directions = {
            1: (0, 1),   # Right
            2: (0, -1),  # Left
            3: (1, 0),   # Down
            4: (-1, 0)   # Up
        }

        # Cost array to track minimum cost to reach each cell
        cost = [[float('inf')] * n for _ in range(m)]
        cost[0][0] = 0

        # Deque for 0-1 BFS: (row, col)
        dq = deque([(0, 0)])

        while dq:

            r, c = dq.popleft()

            # Try all 4 directions
            for direction, (dr, dc) in directions.items():
                nr, nc = r + dr, c + dc

                # Check bounds
                if 0 <= nr < m and 0 <= nc < n:
                    # Calculate cost for this move
                    # If current cell points to this direction → cost = 0
                    # Otherwise → cost = 1 (need to change sign)
                    move_cost = 0 if grid[r][c] == direction else 1
                    new_cost = cost[r][c] + move_cost

                    # If found cheaper path to (nr, nc)
                    if new_cost < cost[nr][nc]:
                        cost[nr][nc] = new_cost

                        # 0-1 BFS trick:
                        if move_cost == 0:
                            dq.appendleft((nr, nc))  # Add to front
                        else:
                            dq.append((nr, nc))      # Add to back

        return cost[m-1][n-1]

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

# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals

class Solution:
    def minCost(self, n: int, edges):

        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, 2 * w))

        dist = [float("inf")] * n
        dist[0] = 0

        visit = set()
        mh = [(0, 0)]  # (cost_so_far, current_node)

        while mh:

            weight, node = heapq.heappop(mh)

            if node == n - 1:
                return weight

            if weight > dist[node]:
                continue

            if node in visit:
                continue

            visit.add(node)

            for child, d in adj[node]:
                new_dist = d + weight
                if new_dist < dist[child]:
                    dist[child] = new_dist
                    heapq.heappush(mh, (dist[child], child))

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