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

        scc = []

        def reverse_dfs(node, component):

            visited[node] = True
            component.append(node)

            for nei in rev_graph[node]:
                if not visited[nei]:
                    reverse_dfs(nei, component)

        # Stack se reverse finishing order mein process karo
        while stack:

            node = stack.pop()

            if visited[node]:
                continue

            component = []

            reverse_dfs(node, component)

            scc.append(component)

        return scc