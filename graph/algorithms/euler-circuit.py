# https://www.geeksforgeeks.org/problems/euler-circuit-and-path/1


class Solution:
    def isEulerCircuitExist(self, V, adj):
        # Find a vertex having non-zero degree
        start = -1

        for i in range(V):
            if len(adj[i]) > 0:
                start = i
                break

        # No edges at all
        if start == -1:
            return 2

        visited = [False] * V

        # dfs se hum check karenge ki graph connected hai ya nahi (ignoring isolated vertices)
        def dfs(node):
            visited[node] = True

            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)

        dfs(start)

        # Agar koi aisa vertex hai jiske paas edge hai, lekin DFS us tak nahi pahunchi, to graph disconnected hai.
        for i in range(V):
            if len(adj[i]) > 0 and not visited[i]:
                return 0

        odd = 0

        for i in range(V):
            if len(adj[i]) % 2 == 1:
                odd += 1

        # Euler Circuit
        if odd == 0:
            return 2

        # Euler Path
        if odd == 2:
            return 1

        # 2 se zyada odd vertices → Impossible
        return 0


print(Solution().isEulerCircuitExist(5, [[1, 2], [0, 2], [0, 1, 3], [2, 4], [3]]))  # Output: 1 (Euler Path exists)
print(Solution().isEulerCircuitExist(3, [[1], [0, 2], [1]]))  # Output: 2 (Euler Circuit exists)