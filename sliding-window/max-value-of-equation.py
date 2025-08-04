# https://leetcode.com/problems/max-value-of-equation/

from collections import deque

class Solution:
    def findMaxValueOfEquation(self, points, k: int) -> int:

        q = deque()
        res = float("-inf")

        for j in range(len(points)):
            xj, yj = points[j]

            # Remove points from front where |xj - xi| > k
            while q and xj - points[q[0]][0] > k:
                q.popleft()

            # Compute max value using the front of deque
            if q:
                i = q[0]
                xi, yi = points[i]
                res = max(res, yi + yj + xj - xi)

            # Remove points from back where (yj - xj) is larger
            while q and (points[q[-1]][1] - points[q[-1]][0]) <= (yj - xj):
                q.pop()

            # Add current point to deque
            q.append(j)

        return res


print(Solution().findMaxValueOfEquation([[1,3],[2,0],[3,10],[4,5]], 1))  # 4
print(Solution().findMaxValueOfEquation([[1,1],[2,2],[3,3],[4,4]], 1))  # 7
print(Solution().findMaxValueOfEquation([[0,0],[3,0],[9,2]], 3))  # 3
print(Solution().findMaxValueOfEquation([[0,0],[1,3],[2,5],[3,4]], 3))  # 7
