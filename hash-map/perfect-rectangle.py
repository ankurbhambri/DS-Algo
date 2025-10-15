class Solution:
    def isRectangleCover(self, rectangles):

        corner_set = set()
        min_x = min_y = float('inf')
        max_x = max_y = float('-inf')
        actual_area = 0

        for x1, y1, x2, y2 in rectangles:

            # Update bounding box
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            # Add area
            actual_area += (x2 - x1) * (y2 - y1)

            # Toggle corners
            for p in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if p in corner_set:
                    corner_set.remove(p)
                else:
                    corner_set.add(p)

        # Check area
        expected_area = (max_x - min_x) * (max_y - min_y)
        if actual_area != expected_area:
            return False

        # Check corners
        expected_corners = {
            (min_x, min_y),
            (min_x, max_y),
            (max_x, min_y),
            (max_x, max_y)
        }

        return corner_set == expected_corners


print(Solution().isRectangleCover([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]))  # True
print(Solution().isRectangleCover([[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]))  # False