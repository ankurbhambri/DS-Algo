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
# TC: O((V + E) log V) - E is the number of edges, V is the number of vertices using priority queue aka Min Heap
# SC: O(V) for the distance array and priority queue
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

Why this matters: This tests your understanding of basic Dijkstra and edge case handling. 
Think of it as a signal broadcast - everyone receives it when the furthest person gets it.

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

            # Relaxtion
            new_t = time + t

            if dist[nei] > new_t:
                dist[nei] = new_t
                heapq.heappush(hm, (new_t, nei))

    res = max(dist.values())
    return -1 if res == float("inf") else res


print(networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))


'''
problem Link - https://leetcode.com/problems/path-with-minimum-effort/description/

Iss problem me, aapko ek grid diya gaya hai jisme har cell ka height diya gaya hai.

Aapko top-left se bottom-right tak ka path find karna hai jisme maximum absolute difference between consecutive cells ko minimize karna hai.

Key insight: When relaxing edges, use new_effort = max(current_effort, abs(height[current] - height[next])) instead of addition.
This pattern appears in many grid-based problems where you minimize the "worst" step rather than total cost.

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

        directions = [(1, 0), (-1, 0), (0,1), (0,-1)]

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
                    
                    # yha pe humne heights ke difference ka absolute value liya aur usko current effort ke sath max kiya
                    step = abs(heights[r][c] - heights[nr][nc])

                    new_effort = max(effort, step)

                    if dist[nr][nc] > new_effort:
                        dist[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))

        return 0


print(Solution().minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]))


'''
Pattern: Dijkstra with constraints (expanding state space) TODO

Problem Link - https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

Find cheapest flight from source to destination with at most K stops. The constraint on number of stops changes everything.

Why this matters: You cannot use standard visited set optimization. You might visit the same node multiple times with different numbers of stops.

Key insight: State becomes (node, stops_used) instead of just (node). You need to track the best cost for each (node, stops) pair. 

Here, we don't need to mark nodes in visited set because the state includes stops used.

Pro tip: This pattern appears whenever there are constraints on path properties (max edges, required visits, etc.)

'''

# TC: O((V + E) * K * log(V * K)) - Each node can be processed up to K+1 times (with strictly decreasing stop counts), so total heap operations are O((V + E) * K), each costing O(log(V * K)).
# SC: O(V * K + E) - The heap can hold O(V * K) entries in the worst case, visit array is O(V), and adjacency list is O(E).

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):

        adj = {i: [] for i in range(n)}

        for u, v, price in flights:
            adj[u].append((v, price))

        dist = [float("inf")] * n

        q = [(0, 0, src)] # cost, stops, node

        while q:
            cost, stops, node = heapq.heappop(q)

            # Have seen the node already, and the current stops are more than last time
            if dist[node] <= stops:  
                continue

            if stops > k: # More than k stops, invalid
                continue

            if node == dst:
                return cost

            dist[node] = stops

            for nei, weight in adj[node]: # weight means cost
                heapq.heappush(q, (cost + weight, stops + 1, nei))

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
Pattern: Minimizing maximum value on path

Problem Link - https://leetcode.com/problems/swim-in-rising-water/description/

Find path where the maximum elevation encountered is minimized. Similar to "Path with Minimum Effort" but simpler.

Why this matters: Another example of modifying the cost metric. Instead of summing costs, track the maximum.

Key insight: Use max(current_time, grid[next_cell]) as the cost. Can also be solved with binary search + BFS,
but Dijkstra is more intuitive once you understand the pattern.

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

        directions = [(1,0), (-1,0), (0, 1), (0, -1)]

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

    # fee, time, node
    heap = [(passingFees[0], 0, 0)]

    while heap:

        fee, time, node = heapq.heappop(heap)

        if node == n - 1:
            return fee

        # yha pe min_time ka use hum iske liye kar rahe hai ki agar hum kisi node pe pahuchne ke liye already ek time record kar chuke hai,
        # toh agar hum wapas usi node pe pahuchte hai aur time zyada hai toh usko ignore kar denge kyunki hume minimum time me destination tak pahuchna hai
        if time >= min_time[node]:
            continue

        min_time[node] = time
        
        for nei, t in graph[node]:

            new_time = time + t

            new_fee = fee + passingFees[nei]
            
            if new_time <= maxTime:
                heapq.heappush(heap, (new_fee, new_time, nei))
    
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
            adj[v].append((u, 2 * w)) # reversal cost humne yhi nikal li hai

        dist = [float("inf")] * n
        dist[0] = 0

        mh = [(0, 0)]  # (cost, current_node)

        while mh:

            weight, node = heapq.heappop(mh)

            if node == n - 1:
                return weight

            if weight > dist[node]:
                continue

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

        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = [float('inf')] * n
        dist[0] = 0

        pq = [(0, 0)]  # (time, node)

        while pq:

            time, node = heapq.heappop(pq)

            if time > dist[node]:
                continue

            for nei, wt in graph[node]:
                new_time = time + wt

                # Must arrive before node disappears
                if new_time < disappear[nei] and new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(pq, (new_time, nei))

        for i in range(n):
            if dist[i] == float('inf'):
                dist[i] = -1

        return dist



# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/

'''

Pattern: Dijkstra with additional counting logic TODO

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
            # cnt + 1 because we need to account for the original edge as well
            adj[u].append((v, cnt + 1))
            adj[v].append((u, cnt + 1))

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

print(Solution().reachableNodes(edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3))  # Output: 13

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
            
            # yha pe hum dono source se destination ka total shortest distance nikal rhe h

            # jaise 0 se 1 ka distance 3 and 1 se 5 (dest) ka distance 6 h toh toal 9 distance mein dono source se destination tak pahuch sakte h

            # question mein yhi puch h ki minium distance from both of the source to destination kya h
            ans = min(ans, dist1[i] + dist2[i] + distToDest[i])

        return -1 if ans == float('inf') else ans


print(Solution().minimumWeight(
    n = 6, edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]],
    src1 = 0, src2 = 1, dest = 5
))  # Output: 9


# https://leetcode.com/problems/modify-graph-edge-weights/description/# 


# TC: O(E log V) for each Dijkstra run, and we may run Dijkstra up to E times in the worst case (if all edges are -1). So worst case is O(E^2 log V).
# SC: O(V + E) for the graph representation and distance arrays.
class Solution:
    def modifiedGraphEdges(self, n, edges, source, destination, target):

        # 1. Sirf fixed edges (weight != -1) ke saath graph banao
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            if w != -1:
                adj[u].append([v, w])
                adj[v].append([u, w])

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

        # Pehla check: Kya fixed edges se distance target se chota hai?
        # ab hum -1 vale edges ko kuch bhi change kar le, Djikstra humesha yhi chota vala hi choose karega
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

            # ** ignore ** just to change that change adj with. new change is giving target or not
            # adj[u][-1][1] = edges[i][2]
            # adj[v][-1][1] = edges[i][2]
            # new_dist = dijkstra(adj, n, source, destination)
            # print(f"After processing edge {u}-{v}, new distance: {new_dist}, target: {target}")

        return edges if found else []


# print(Solution().modifiedGraphEdges(3, [[0, 1, -1], [1, 2, 5]], 0, 2, 6))  # [[0,1,1],[1,2,5]]
print(Solution().modifiedGraphEdges(5, [[0, 1, -1], [0, 2, 5], [1, 2, -1], [1, 3, 8], [2, 4, -1], [3, 4, 2]], 0, 4, 20))  # [[0,1,1],[0,2,5],[1,2,14],[1,3,8],[2,4,1],[3,4,2]]