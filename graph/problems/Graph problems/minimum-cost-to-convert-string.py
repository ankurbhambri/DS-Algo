# https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/


from collections import defaultdict
import heapq

class Solution:
    
    def minimumCost(self, source: str, target: str, original, changed, cost):

        adj = defaultdict(list)

        for u, v, c in zip(original, changed, cost):
            adj[u].append((v, c))
        
        def djisktra(src):
                              
            heap = [(0, src)]
            min_cost = {}

            while heap:

                cost, node = heapq.heappop(heap)

                if node in min_cost:
                    continue  # Already processed with minimal cost

                min_cost[node] = cost

                for ch, d in adj[node]:

                    heapq.heappush(heap, (cost + d, ch))

            return min_cost
        
        dist = {i: djisktra(i) for i in set(source)}

        res = 0

        for src, dst in zip(source, target):

            if dst not in dist[src]:
                return -1

            res += dist[src][dst]

        return res


print(Solution().minimumCost("aaaa", "bbbb", ["a", "c"], ["c", "b"], [1, 2]))  # Output: 4
print(Solution().minimumCost("abc", "xyz", ["a", "b", "c"], ["x", "y", "z"], [1, 2, 3]))  # Output: 6
