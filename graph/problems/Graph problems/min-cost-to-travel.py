# https://leetcode.com/discuss/post/8285832/shortest-path-with-time-windows-dijkstra-ejcv/


'''
You are given a directed weighted graph of n nodes (0-indexed) and a list of edges where:

edges[i] = [u, v, w, open, close]

This represents a directed edge from u to v with travel cost w. However, each edge is only usable if your arrival time at node u falls within the window [open, close), i.e., open <= time < close.

Find the minimum cost to travel from node 0 to node n-1. If it is impossible, return -1.

Note: You may wait at a node for free. Waiting increases your arrival time by 1 per step. Cost of waiting = 0.

Examples

Example 1:

Input:  n = 4, edges = [[0,1,2,0,5],[0,2,5,0,3],[1,3,3,2,10],[2,3,1,4,8]]
Output: 5
Explanation:
  Path 0 -> 1 -> 3:
  At node 0, t=0, edge [0,5) open. Cost=2. Arrive at node 1 at t=2.
  At node 1, t=2, edge [2,10) open. Cost=3.
  Total = 5. Alternative path 0->2->3 costs 6.

Example 2:

Input:  n = 3, edges = [[0,1,4,0,2],[1,2,3,5,9]]
Output: 7
Explanation:
  Arrive at node 1 at t=4. Edge 1->2 opens at t=5.
  Wait 1 step for free (t=5), then travel. Cost = 4+3 = 7.

Example 3:

Input:  n = 3, edges = [[0,1,5,0,10],[1,2,3,0,4]]
Output: -1
Explanation:
  Arrive at node 1 at t=5. Edge 1->2 closes at t=4. Window shut. No path.

Constraints
    1 <= n <= 200
    0 <= edges.length <= 500
    1 <= w <= 1000
    0 <= open < close <= 100
    No self-loops


'''

import heapq

# TC: O(E log(V * T)) where E is the number of edges, V is the number of vertices, and T is the maximum time constraint (100 in this case).
# SC: O(V * T) for the min_cost table and the priority queue in the worst case.
def minCostToTravel(n, edges):

    MAX_TIME = 200

    # 1. Graph (Adjacency List) banate hain
    adj = {i: [] for i in range(n)}

    for u, v, w, open_t, close_t in edges:
        adj[u].append((v, w, open_t, close_t))

    # 2. min_cost[node][time] table initialized with infinity
    # Max time constraint is MAX_TIME, so we take size MAX_TIME
    min_cost = [[float('inf')] * MAX_TIME for _ in range(n)]

    # 3. Min-Heap stores elements as (cost, node, time)
    # Python's heapq automatically sorts by first element (cost), then second (node), etc.
    pq = [(0, 0, 0)]  # (cost, node, time)
    min_cost[0][0] = 0

    while pq:

        curr_cost, u, curr_time = heapq.heappop(pq)

        # Target node reached
        if u == n - 1:
            return curr_cost

        # Optimization: skip if we found a better path already
        if curr_cost > min_cost[u][curr_time]:
            continue

        # Check neighbors
        for v, w, open_t, close_t in adj[u]:

            # Agar window pehle hi close ho chuki hai
            if curr_time >= close_t:
                continue

            # Free waiting logic: agar jaldi hain toh open_t tak wait karenge
            next_time = max(curr_time, open_t)
            next_cost = curr_cost + w

            # Agar cost pehle se behtar hai, toh push karo heap mein
            if next_time < MAX_TIME and next_cost < min_cost[v][next_time]:
                min_cost[v][next_time] = next_cost
                heapq.heappush(pq, (next_cost, v, next_time))

    return -1


print(minCostToTravel(3, [[0, 1, 5, 0, 5], [1, 2, 10, 0, 5], [0, 2, 20, 0, 5]]))  # Expected Output: 15
print(minCostToTravel(4, [[0, 1, 5, 0, 10], [1, 2, 10, 5, 15], [0, 2, 15, 0, 20], [2, 3, 5, 10, 20]]))  # Expected Output: 20