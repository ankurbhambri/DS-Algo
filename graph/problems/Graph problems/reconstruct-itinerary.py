# https://leetcode.com/problems/reconstruct-itinerary

from collections import defaultdict

# TC: O(E log E) due to sorting the adjacency list, where E is the number of edges (tickets)
# SC: O(V + E) for the graph representation, where V is the number of vertices (airports) and E is the number of edges (tickets)
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:

        # Step 1: Adjacency list (Graph) banana
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