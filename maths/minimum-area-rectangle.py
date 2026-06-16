# https://leetcode.com/problems/minimum-area-rectangle/


# TC: O(N ^ 2) in worst case when all points are unique and form a grid
# SC: O(N) for storing points in set and unique coordinates
class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:

        visit = set()

        res = float("inf")

        for x1, y1 in points:

            for x2, y2 in points:

                if (x1, y2) in visit and (x2, y1) in visit:

                    size = abs(x2 - x1) * abs(y2 - y1)

                    res = min(res, size)

            visit.add((x1, y1))

        return res if res != float("inf") else 0


print(Solution().minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))  # Output: 4
print(Solution().minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))  # Output: 2