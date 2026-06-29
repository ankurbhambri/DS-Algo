from collections import defaultdict

# Directed Graph

# TC: O(E) where E is the number of edges
# SC: O(V + E) for the graph representation, where V is the number of vertices
def hierholzer(edges, start):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)

    path = []

    def dfs(u):
        while graph[u]:
            v = graph[u].pop()      # Remove unused edge
            dfs(v)
        path.append(u)              # Dead end -> add vertex

    dfs(start)

    return path[::-1]


# Iterative Version (No Recursion)

# TC: O(E) where E is the number of edges
# SC: O(V + E) for the graph representation, where V is the number of vertices
def hierholzer(edges, start):

    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)

    stack = [start]
    path = []

    while stack:

        u = stack[-1]

        if graph[u]:
            stack.append(graph[u].pop())
        else:
            path.append(stack.pop())

    return path[::-1]


# Undirected Graph

# TC: O(E) where E is the number of edges
# SC: O(V + E) for the graph representation, where V is the number of vertices
from collections import defaultdict

def hierholzer(edges, start):

    graph = defaultdict(list)

    for idx, (u, v) in enumerate(edges):
        graph[u].append((v, idx))
        graph[v].append((u, idx))

    used = [False] * len(edges)
    path = []

    def dfs(u):

        while graph[u]:

            v, eid = graph[u].pop()

            if used[eid]:
                continue

            used[eid] = True

            dfs(v)

        path.append(u)

    dfs(start)

    return path[::-1]


# https://leetcode.com/problems/reconstruct-itinerary


# TC: O(E log E) due to sorting the adjacency list, where E is the number of edges (tickets)
# SC: O(V + E) for the graph representation, where V is the number of vertices (airports) and E is the number of edges (tickets)
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:

        graph = defaultdict(list)

        for src, dst in tickets:
            graph[src].append(dst)

        # Step 2: Destinations ko ulta sort (reverse sort) karna
        # Taaki pop() karne par alphabetically sabse chota airport pehle nikle
        for src in graph:
            graph[src].sort(reverse=True)

        # Step 3: Hierholzer's Algorithm using Stack
        stack = ["JFK"] # Hamesha JFK se shuru karna hai
        result = []

        while stack:

            current_airport = stack[-1] # Stack ka sabse upar waala element check karo

            # Agar is airport se aur flights bachi hain
            if graph[current_airport]:
                next_airport = graph[current_airport].pop() # Agli flight lo
                stack.append(next_airport) # Stack mein daalo aur aage badho

            else:
                # Agar dead-end mil gaya (koi flight nahi bachi), toh ise result mein daalo
                result.append(stack.pop())

        # Step 4: Result ko ulta (reverse) karke return karo
        return result[::-1]


print(Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))  # Output: ['JFK', 'MUC', 'LHR', 'SFO', 'SJC']
print(Solution().findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))  # Output: ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']