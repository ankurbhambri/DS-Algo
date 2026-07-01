from collections import defaultdict

class Solution:

    def kosaraju(self, V, adj):

        # Original graph
        graph = defaultdict(list)

        # Reverse graph
        rev_graph = defaultdict(list)

        for u in range(V):
            for v in adj[u]:
                graph[u].append(v)
                rev_graph[v].append(u)

        # Stack mein finishing order store hoga
        stack = []

        visited = [False] * V

        # ----------------------------
        # First DFS
        # Finish hone ke baad node ko stack mein push karo
        # ----------------------------
        def dfs(node):

            visited[node] = True

            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)

            # Sab children explore ho gaye
            stack.append(node)

        for i in range(V):
            if not visited[i]:
                dfs(i)

        # ----------------------------
        # Second DFS on Reverse Graph
        # ----------------------------
        visited = [False] * V


        def reverse_dfs(node, component):

            visited[node] = True
            component.append(node)

            for nei in rev_graph[node]:
                if not visited[nei]:
                    reverse_dfs(nei, component)

        scc = []
        # Stack se reverse finishing order mein process karo
        while stack:

            node = stack.pop()

            if visited[node]:
                continue

            component = []

            reverse_dfs(node, component)

            scc.append(component)

        return scc


print(Solution().kosaraju(5, [[1], [2], [0], [4], [3]]))  # Output: [[3, 4], [0, 1, 2]]



# https://pkg.go.dev/github.com/lee-hen/Algoexpert/very_hard/22_airport_connections#section-readme


from collections import defaultdict

def get_airport_connections(airports, routes, starting_airport):
    # Step 1: Adjacency list aur Reverse Adjacency list banao
    graph = defaultdict(list)
    rev_graph = defaultdict(list)
    for u, v in routes:
        graph[u].append(v)
        rev_graph[v].append(u)

    # Kosaraju's Step 1: Order fill karo stack mein
    visited = set()
    stack = []

    def fill_order(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                fill_order(neighbor)
        stack.append(node)

    for airport in airports:
        if airport not in visited:
            fill_order(airport)

    # Kosaraju's Step 3: Reversed graph par DFS chalao SCCs nikalne ke liye
    visited = set()
    sccs = []
    # Ek map jo har airport ko uske SCC ID (index) se connect karega
    airport_to_scc_id = {} 

    def dfs_reverse(node, component):
        visited.add(node)
        component.append(node)
        airport_to_scc_id[node] = len(sccs) # Current SCC ka index assign kiya
        for neighbor in rev_graph[node]:
            if neighbor not in visited:
                dfs_reverse(neighbor, component)

    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs_reverse(node, component)
            sccs.append(component)

    # Step 4: Har SCC ki In-degree nikalna
    # Total SCCs jitna bada array banao jisme initially sabki in-degree 0 ho
    scc_in_degree = [0] * len(sccs)

    for u, v in routes:
        scc_u = airport_to_scc_id[u]
        scc_v = airport_to_scc_id[v]
        # Agar edge do alag-alag SCCs ke beech mein hai
        if scc_u != scc_v:
            scc_in_degree[scc_v] += 1

    # Step 5: Answer calculate karo
    # Pata karo starting_airport kaunse SCC mein aata hai
    starting_scc_id = airport_to_scc_id[starting_airport]

    connections_needed = 0
    for scc_id in range(len(sccs)):
        # Agar kisi SCC ki in-degree 0 hai aur wo starting wala SCC nahi hai
        if scc_in_degree[scc_id] == 0 and scc_id != starting_scc_id:
            connections_needed += 1

    return connections_needed


airports = [
    "BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN",
    "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD",
]

routes = [
    ["DSM", "ORD"], ["ORD", "BGI"], ["BGI", "LGA"], ["SIN", "CDG"],
    ["CDG", "SIN"], ["CDG", "BUD"], ["DEL", "DOH"], ["DEL", "CDG"],
    ["TLV", "DEL"], ["EWR", "HND"], ["HND", "ICN"], ["HND", "JFK"],
    ["ICN", "JFK"], ["JFK", "LGA"], ["EYW", "LHR"], ["LHR", "SFO"],
    ["SFO", "SAN"], ["SFO", "DSM"], ["SAN", "EYW"]
]

startingAirport = "LGA"

print("Minimum connections needed:", get_airport_connections(airports, routes, startingAirport)) # Output: 3