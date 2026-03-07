# https://leetcode.com/problems/campus-bikes/

'''

Campus Bikes I

On a campus represented on the X-Y plane, there are n workers and m bikes, with n <= m.

You are given an array workers of length n where workers[i] = [xi, yi] is the position of the ith worker. 
You are also given an array bikes of length m where bikes[j] = [xj, yj] is the position of the jth bike. All the given positions are unique.

Assign a bike to each worker. Among the available bikes and workers, we choose the (workeri, bikej) pair with the shortest Manhattan distance between each other and assign the bike to that worker.

If there are multiple (workeri, bikej) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index. 
If there are multiple ways to do that, we choose the pair with the smallest bike index. Repeat this process until there are no available workers.

Return an array answer of length n, where answer[i] is the index (0-indexed) of the bike that the ith worker is assigned to.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Example 1:

Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]] Output: [1,0] 

Explanation:

    Worker 1 grabs Bike 0 as they are closest (without ties), and Worker 0 is assigned Bike 1. So the output is [1, 0]. 

Example 2:
Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]] Output: [0,2,1]

Explanation:

    Worker 0 grabs Bike 0 at first. Worker 1 and Worker 2 share the same distance to Bike 2, 
    thus Worker 1 is assigned to Bike 2, and Worker 2 will take Bike 1. So the output is [0,2,1]. 
    
Constraints:

    n == workers.length 
    m == bikes.length 
    1 <= n <= m <= 1000 
    workers[i].length == bikes[j].length == 2 
    0 <= xi, yi < 1000 
    0 <= xj, yj < 1000 
    All worker and bike locations are unique.

'''

class Solution:
    def assignBikes(self, workers, bikes):

        pairs = []

        for i, (wx, wy) in enumerate(workers):
            for j, (bx, by) in enumerate(bikes):
                dist = abs(wx - bx) + abs(wy - by)
                pairs.append((dist, i, j))

        pairs.sort() # here, distance will help in sorting

        res = [-1] * len(workers)
        worker_used = set()
        bike_used = set()

        for _, w, b in pairs:

            if w not in worker_used and b not in bike_used:

                res[w] = b
                worker_used.add(w)
                bike_used.add(b)

        return res


print(Solution().assignBikes([[0,0],[2,1]], [[1,2],[3,3]]))
print(Solution().assignBikes([[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]]))
print(Solution().assignBikes([[0,0],[1,0],[2,0],[3,0],[4,0]], [[0,999],[1,999],[2,999],[3,999],[4,999]]))


# https://leetcode.com/problems/campus-bikes-ii/

'''
Campus Bikes II

On a campus represented as a 2D grid, there are n workers and m bikes, with n <= m. Each worker and bike is a 2D coordinate on this grid.

We assign one unique bike to each worker so that the sum of the Manhattan distances between each worker and their assigned bike is minimized.

Return the minimum possible sum of Manhattan distances between each worker and their assigned bike.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.
 

Example 1:

Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: 6

Explanation: 
We assign bike 0 to worker 0, bike 1 to worker 1. The Manhattan distance of both assignments is 3, so the output is 6.

Example 2:

Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
Output: 4

Explanation: 
We first assign bike 0 to worker 0, then assign bike 1 to worker 1 or worker 2, bike 2 to worker 2 or worker 1. Both assignments lead to sum of the Manhattan distances as 4.

Example 3:

Input: workers = [[0,0],[1,0],[2,0],[3,0],[4,0]], bikes = [[0,999],[1,999],[2,999],[3,999],[4,999]]
Output: 4995
 
Constraints:

    n == workers.length
    m == bikes.length
    1 <= n <= m <= 10
    workers[i].length == 2
    bikes[i].length == 2
    0 <= workers[i][0], workers[i][1], bikes[i][0], bikes[i][1] < 1000
    All the workers and the bikes locations are unique.

'''

from functools import lru_cache

class Solution:
    def assignBikes(self, workers, bikes):

        n = len(workers)
        m = len(bikes)

        def dist(w, b):
            return abs(w[0]-b[0]) + abs(w[1]-b[1])

        @lru_cache(None)
        def dfs(mask):

            worker = bin(mask).count("1")

            if worker == n:
                return 0

            ans = float('inf')

            for j in range(m):

                if mask & (1<<j) == 0:

                    cost = dist(workers[worker], bikes[j])

                    ans = min(ans,
                              cost + dfs(mask | (1<<j)))

            return ans

        return dfs(0)


print(Solution().assignBikes([[0,0],[2,1]], [[1,2],[3,3]]))
print(Solution().assignBikes([[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]]))
print(Solution().assignBikes([[0,0],[1,0],[2,0],[3,0],[4,0]], [[0,999],[1,999],[2,999],[3,999],[4,999]]))


'''
Campus Bikes II

Travelling Salesman

Minimum XOR pairs

Matchsticks to Square
'''