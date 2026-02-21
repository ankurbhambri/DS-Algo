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
from typing import List
from collections import defaultdict, deque

# For Unweighted Graphs (BFS)
def bfs(graph, root):

    # distance dict
    distances = {node: float("inf") for node in graph}
    distances[root] = 0

    queue = deque([root])

    while queue:

        current_node = queue.popleft()

        for neighbor in graph[current_node]:

            if distances[neighbor] == float("inf"):

                # level order traversal, so distance of neighbor is distance of current node + 1
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

print(bfs(graph, "A"))


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


'''
Pattern: Basic Dijkstra with modified output

problem Link - https://leetcode.com/problems/network-delay-time/description/

Instead of returning distance to a specific node, return the maximum distance among all reachable nodes. If any node is unreachable, return -1.

Why this matters: This tests your understanding of basic Dijkstra and edge case handling. Think of it as a signal broadcast - everyone receives it when the furthest person gets it.

Key insight: After running standard Dijkstra, check max(distances). This is a warm-up problem that appears frequently in OAs.

'''

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


'''
Pattern: Modified cost function (max instead of sum)

problem Link - https://leetcode.com/problems/path-with-minimum-effort/description/

The cost of a path is the maximum absolute difference between consecutive cells, not the sum. You want to minimize this maximum difference.

Why this matters: Shows that Dijkstra works for any monotonic cost function, not just addition. The greedy property still holds.

Key insight: When relaxing edges, use new_effort = max(current_effort, abs(height[current] - height[next])) instead of addition. This pattern appears in many grid-based problems where you minimize the "worst" step rather than total cost.

Similar problems: Swim in Rising Water (LC 778)
'''

# TC: O(m * n * log(m * n)) - We process each cell at most once, and each cell has up to 4 neighbors. The priority queue operations take O(log(m * n)) time.
# SC: O(m * n) - We maintain a cost array of size m * n

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

'''

Pattern: Minimizing maximum value on path

Problem Link - https://leetcode.com/problems/swim-in-rising-water/description/

Find path where the maximum elevation encountered is minimized. Similar to "Path with Minimum Effort" but simpler.

Why this matters: Another example of modifying the cost metric. Instead of summing costs, track the maximum.

Key insight: Use max(current_time, grid[next_cell]) as the cost. Can also be solved with binary search + BFS, but Dijkstra is more intuitive once you understand the pattern.

Common mistake: We often try to use BFS without considering that different paths to same cell can have different maximum heights.

'''

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


'''
Pattern: Dijkstra with constraints (expanding state space)

Problem Link - https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

Find cheapest flight from source to destination with at most K stops. The constraint on number of stops changes everything.

Why this matters: You cannot use standard visited set optimization. You might visit the same node multiple times with different numbers of stops.

Key insight: State becomes (node, stops_used) instead of just (node). You need to track the best cost for each (node, stops) pair. This is crucial - many candidates fail here because they try to mark nodes as visited.

Pro tip: This pattern appears whenever there are constraints on path properties (max edges, required visits, etc.)

'''

# TC: O((V + E) * K * log(V * K)) - Each node can be processed up to K+1 times (with strictly decreasing stop counts), so total heap operations are O((V + E) * K), each costing O(log(V * K)).
# SC: O(V * K + E) - The heap can hold O(V * K) entries in the worst case, visit array is O(V), and adjacency list is O(E).

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

'''
Pattern: Maximization instead of minimization

Problem Link - https://leetcode.com/problems/path-with-maximum-probability/description/

Find path with maximum probability (multiply probabilities along edges) instead of minimum cost.

Why this matters: Tests understanding that Dijkstra is fundamentally about greedy optimization, not just minimization.

Key insight: Use max-heap (negate values in Python), multiply probabilities instead of adding, and update when new_probability > current_probability. The greedy property works for maximization too!

Watch out: Make sure to handle probability comparisons with floating point carefully.

'''
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


'''
Pattern: Dijkstra with time and cost constraints

Problem Link - https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/description/

Find minimum cost to reach destination within maxTime. Edges have both time and cost.

Why this matters: Tests ability to handle multiple constraints in Dijkstra. You need to track both time and cost, and ensure you don't exceed maxTime.

Key insight: State is (cost_so_far, time_so_far, node). When relaxing edges, update both cost and time.

Make sure to check time constraint before pushing new state into the heap. This pattern appears in many problems where you have a budget or time limit.

'''

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

'''

Pattern: Dijkstra with edge reversals

Problem Link - https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/description/

Find minimum cost path where you can reverse edges at a cost. This creates a new graph with both original and reversed edges.

Why this matters: Tests ability to modify the graph on the fly and handle additional states (reversed or not).

Key insight:
    When building the graph, add both (u -> v, cost 0) and (v -> u, cost 1) to represent the option of reversing. 
    Then run standard Dijkstra on this modified graph. 
    This pattern appears in problems where you have the option to change the graph structure at a cost.

'''

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


'''

Pattern: Dijkstra with dynamic constraints

Problem Link - https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/description/

Nodes disappear at specific times. Can only visit if you arrive before disappearance.

Why this matters: Tests handling of time-dependent or dynamic constraints during path exploration.

Key insight: Add validation during edge relaxation: if arrival_time < disappear_time[node] and arrival_time < dist[node]. Must check BOTH conditions.

'''

# TC: O((V + E) log V) - Standard Dijkstra; each node is processed at most once, and each edge is relaxed at most once.
# SC: O(V + E) - O(V) for dist and answer arrays, O(V + E) for the adjacency list, and O(V) for the heap.

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:

        # Build graph
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Result & distance
        answer = [-1] * n
        dist = [float('inf')] * n

        # Dijkstra-like
        dist[0] = 0
        heap = [(0, 0)]  # (current_time, node)

        while heap:
            time, u = heapq.heappop(heap)
            # If we've already assigned a valid answer, skip,
            # or if we've reached too late
            if answer[u] != -1 or time >= disappear[u]:
                continue

            answer[u] = time

            for v, cost in graph[u]:
                newTime = time + cost
                if newTime < disappear[v] and newTime < dist[v]:
                    dist[v] = newTime
                    heapq.heappush(heap, (newTime, v))

        return answer


'''
Pattern: Dijkstra with coupon

problem Link - https://cses.fi/problemset/task/1195/

Find minimum cost path where you can use a coupon to halve the cost of one edge. State includes whether coupon used or not.

Why this matters: Tests ability to handle additional state (coupon used or not) in Dijkstra. You need to track best cost for both states at each node.

Key insight: State is (node, coupon_used). When relaxing edges, consider both options:

- Move without using coupon: new_cost = current_cost + edge_weight
- Move using coupon (if not used): new_cost = current_cost + edge_weight // 2

This pattern appears in problems where you have a one-time power-up or discount that can be applied to any edge.

'''

# TC: O((V + E) log V) - State space is 2V (each node with coupon used or not), edges are 2E. O((2V + 2E) log 2V) simplifies to O((V + E) log V).
# SC: O(V + E) - O(V) for the 2-state distance array, O(V + E) for the adjacency list, and O(V) for the heap.

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


'''

Pattern: K shortest paths

problem Link - https://cses.fi/problemset/task/1196

Find k shortest paths from source to destination. State includes the number of paths found so far.

Why this matters: Tests ability to track multiple best paths and handle more complex state in Dijkstra.

Key insight:
    Instead of tracking just the best cost to each node, track a list of the k best costs. 
    When relaxing edges, add new cost to the list and keep only the k smallest. 
    This pattern appears in problems where you need multiple solutions, not just the single best one.

'''

# TC: O(K * E * log(K * V)) - Each node can be popped at most K times. Total pops: O(V * K). Each pop pushes up to degree(node) neighbors, so total pushes: O(K * E). Each heap operation costs O(log(K * V)).
# SC: O(K * (V + E)) - O(V * K) for storing K shortest distances per node, and the heap can hold up to O(K * E) entries in the worst case.

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

'''

Pattern: 0-1 weighted graphs

problem Link - https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/

Grid with arrows. Following arrow = cost 0, changing direction = cost 1. This creates a 0-1 weighted graph.

Why this matters: When all edges have weight 0 or 1, you can optimize Dijkstra using 0-1 BFS with a deque instead of priority queue. Runs in O(V + E) instead of O((V + E) log V).

Key insight: While Dijkstra works fine here, mentioning 0-1 BFS optimization in interviews shows advanced knowledge. The pattern: edges with only two possible weights.

Interview tip: Always look for binary edge weights - it's an optimization opportunity.

'''

# TC: O(m * n) - We process each cell at most once, and each cell has up to 4 neighbors. The deque operations take O(1) time.
# SC: O(m * n) - We maintain a cost array of size m * n and a deque that can hold up to m * n entries in the worst case.

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

'''

Pattern: Dijkstra with additional counting logic

problem Link - https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/description/

Edges have intermediate nodes. Count how many total nodes (original + intermediate) are reachable within maxMoves.

Why this matters: Dijkstra is used for the distance calculation, but requires additional problem-specific logic afterward.

Key insight:

    Run standard Dijkstra to find distances to original nodes
    For each edge, calculate how many intermediate nodes reachable from both ends
    Use min(intermediate_count, reachable_from_u + reachable_from_v) to avoid double-counting

'''

# TC: O((V + E) log V) for Dijkstra, plus O(E) for counting reachable nodes on edges, so overall O((V + E) log V).
# SC: O(V + E) for the graph representation and distance arrays.
class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        # Build adjacency list: weight = cnt + 1
        adj = defaultdict(list)
        for u, v, cnt in edges:
            w = cnt + 1
            adj[u].append((v, w))
            adj[v].append((u, w))

        # Dijkstra from node 0
        dist = [float("inf")] * n
        dist[0] = 0
        pq = [(0, 0)]  # (distance, node)

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

        # Count reachable original nodes
        ans = 0
        for i in range(n):
            if dist[i] <= maxMoves:
                ans += 1

        # Count reachable subdivided nodes on each edge
        for u, v, cnt in edges:
            # Moves left from both ends
            left_u = max(0, maxMoves - dist[u])
            left_v = max(0, maxMoves - dist[v])

            # We can cover at most cnt new nodes on this edge
            ans += min(cnt, left_u + left_v)

        return ans

'''

Pattern: Multiple source Dijkstra + graph reversal

problem Link - https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/description/

Two sources, one destination. Find minimum cost where paths can share edges.

Why this matters: Shows that running Dijkstra multiple times and combining results can solve complex problems.

Key insight:

    Run Dijkstra from src1 (normal graph)
    Run Dijkstra from src2 (normal graph)
    Run Dijkstra from destination on reversed graph (gets distances TO destination from all nodes)
    For each node i: answer = min(dist1[i] + dist2[i] + dist_to_dest[i])
    Catch: Reversing directed graph + Dijkstra = distances from all nodes TO a destination.

Similar pattern: Many multi-source/destination problems use this approach.

'''

# TC: O((V + E) log V) for each Dijkstra run, and we run it 3 times, so O(3 * (V + E) log V) = O((V + E) log V)
# SC: O(V + E) for the graph representation and distance arrays.
class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:

        graph = defaultdict(list)
        rev_graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))
            rev_graph[v].append((u, w))

        def dijkstra(start, adj):
            dist = [float('inf')] * n
            dist[start] = 0
            pq = [(0, start)]

            while pq:
                d, node = heapq.heappop(pq)
                if d > dist[node]:
                    continue
                for nei, w in adj[node]:
                    nd = d + w
                    if nd < dist[nei]:
                        dist[nei] = nd
                        heapq.heappush(pq, (nd, nei))
            return dist

        dist1 = dijkstra(src1, graph)
        dist2 = dijkstra(src2, graph)
        distToDest = dijkstra(dest, rev_graph)

        ans = float('inf')
        for i in range(n):
            ans = min(ans, dist1[i] + dist2[i] + distToDest[i])

        return -1 if ans == float('inf') else ans


'''

Pattern: Dijkstra with on-the-fly edge weight modification

problem Link - https://leetcode.com/problems/modify-graph-edge-weights/description/

Find edge weights to make shortest path from source to destination equal target. You can only increase weights of edges with -1.

Why this matters: Tests ability to integrate Dijkstra with a search over edge modifications. You need to check the impact of each modification on the shortest path.

Key insight:
    First, run Dijkstra with only fixed edges to see if target is already met or impossible
    Then, for each -1 edge, try setting it to 1 and check if we can meet the target. If we can, adjust it to hit the target exactly.
    This pattern appears in problems where you have to find the right parameters to achieve a specific path cost.

'''

# TC: O(E log V) for each Dijkstra run, and we may run Dijkstra up to E times in the worst case (if all edges are -1). So worst case is O(E^2 log V).
# SC: O(V + E) for the graph representation and distance arrays.
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

'''

Pattern: State compression using bitmask

problem Link - https://leetcode.com/problems/shortest-path-visiting-all-nodes/description/

Visit all nodes (can revisit) and return shortest path length. Can start from any node.

Why this matters: Most advanced pattern - combines Dijkstra concepts with bitmask state compression.

Key insight:

    State is (node, visited_bitmask) where bitmask tracks which nodes visited
    Can revisit nodes with different visited sets
    Goal: reach any node where bitmask = (1 << n) - 1 (all bits set)
    Since edges have weight 1, use BFS instead of Dijkstra

This is huge: Bitmask state compression appears in many hard problems (TSP, Hamiltonian paths, etc.)

'''

# TC: O(2^n * (V + E)) or O(n^2 * 2^n) in worst case - There are n * 2^n unique states, each processed once. For each state (u, mask), we iterate over graph[u] neighbors. Total transitions = 2^n * sum(degrees) = 2^n * 2E. For dense graphs (E = O(n^2)), this becomes O(n^2 * 2^n).
# SC: O(n * 2^n) - The queue can hold up to n * 2^n states in the worst case, and the seen set also stores these states.
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

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