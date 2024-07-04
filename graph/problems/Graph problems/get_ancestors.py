class Solution:
    def getAncestors(self, n, edges):
        # Create adjacency list
        adj = [[] for _ in range(n)]

        # Fill the adjacency list and indegree array based on the edges
        indegree = [0 for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1

        # Queue for nodes with no incoming edges (starting points for topological sort)
        q = [i for i in range(n) if indegree[i] == 0]

        # List to store the topological order of nodes
        topological_order = []
        while q:
            current_node = q.pop(0)
            topological_order.append(current_node)

            for neighbor in adj[current_node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # Initialize the result list and set list for storing ancestors
        ancestors_set_list = [set() for _ in range(n)]

        # Fill the set list with ancestors using the topological order
        for node in topological_order:
            for neighbor in adj[node]:
                # Add immediate parent, and other ancestors.
                ancestors_set_list[neighbor].add(node)
                ancestors_set_list[neighbor].update(ancestors_set_list[node])

        res = [[] for _ in range(n)]
        # Convert sets to lists and sort them
        for i in range(n):
            res[i].extend(ancestors_set_list[i])
            res[i].sort()

        return res
