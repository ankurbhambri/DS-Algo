'''

Given a n number of vertical lines in an XY plane, assume the length of lines is infinity, there also exists m number of rectangles in the plane, 

if a line cuts through a rectangle, then it makes two intersection points with the rectangle (one point with the upper horizontal line of rectangle, 

another with lower horizontal line), if a line aligns or overlaps over the vertical line of the rectangle then it is not considered any intersection point. 

Find the total number of intersection points in efficient time and space complexity.

'''

from bisect import bisect_left, bisect_right

def count_intersection_points(vertical_lines, rectangles):

    # Step 1: Vertical lines ko sort karein
    vertical_lines.sort()
    
    total_intersections = 0

    # Step 2: Har rectangle ke liye process karein
    for rect in rectangles:

        # rect format assumed: (x_start, y_bottom, x_end, y_top)
        x_start, _, x_end, _ = rect

        # Binary search se lines ka range find karein jo rectangle ke andar hain
        # bisect_right(x_start) -> pehli line jo > x_start ho
        left_idx = bisect_right(vertical_lines, x_start)

        # bisect_left(x_end) -> pehli line jo >= x_end ho (taki x_end strictly excluded rahe)
        right_idx = bisect_left(vertical_lines, x_end)

        # Kitni lines cut kar rahi hain
        lines_inside = right_idx - left_idx

        if lines_inside > 0:
            # Har line 2 intersection points banati hai (Top and Bottom edges par)
            total_intersections += lines_inside * 2

    return total_intersections


# Vertical lines ke x-coordinates
lines = [1, 3, 5, 8] 

# Rectangles format: (x_start, y_bottom, x_end, y_top)
rectangles = [
    (2, 1, 6, 5),  # Lines 3 aur 5 iske andar aayengi -> 2 lines * 2 = 4 points
    (5, 0, 9, 3)   # Line 8 iske andar aayegi (5 border par hai toh ignore) -> 1 line * 2 = 2 points
]

result = count_intersection_points(lines, rectangles)
print(f"Total Intersection Points: {result}")