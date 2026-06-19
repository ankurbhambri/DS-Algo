# https://leetcode.com/problems/minimum-time-for-k-connected-components/

class Solution:
    def minTime(self, n: int, edges: list[list[int]], k: int) -> int:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return False
            parent[x] = y
            return True

        edges.sort(key = lambda e: -e[2])
        count = n

        parent = list(range(n))
        for u, v, t in edges:
            if union(u, v):
                count -= 1
            if count < k:
                return t
        return 0


print(Solution().minTime(5, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1]], 2)) # Output: 1
print(Solution().minTime(5, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1]], 1)) # Output: 0

# https://leetcode.com/problems/minimize-maximum-component-cost/

class Solution:
    def minCost(self, n: int, edges: list[list[int]], k: int) -> int:

        def find(x):
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]
    
        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return False
            f[x] = y
            return True

        if n <= k:
            return 0

        edges.sort(key = lambda e: e[2])

        count = n

        f = list(range(n))

        for u, v, w in edges:
            if union(u, v):
                count -= 1
            if count <= k:
                return w
        return 0

print(Solution().minCost(5, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1]], 2)) # Output: 1
print(Solution().minCost(5, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1]], 1)) # Output: 1