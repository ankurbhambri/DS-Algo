# https://leetcode.com/problems/minimum-area-rectangle/


# TC: O(N ^ 2) in worst case when all points are unique and form a grid
# SC: O(N) for storing points in set and unique coordinates
class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:

        visit = set((x, y) for x, y in points)
        res = float('inf')

        for i in range(len(points)):
            for j in range(i + 1, len(points)):

                x1, y1 = points[i]
                x2, y2 = points[j]

                # Check if they can form a diagonal of a rectangle
                if x1 != x2 and y1 != y2:

                    # Check if the other two corners exist
                    if (x1, y2) in visit and (x2, y1) in visit:
                        area = abs(x2 - x1) * abs(y2 - y1)
                        res = min(res, area)

        return res if res != float('inf') else 0
 

print(Solution().minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))  # Output: 4
print(Solution().minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))  # Output: 2