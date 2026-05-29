# https://www.youtube.com/watch?v=EuPSibuIKIg

'''
Given a list of Cartesian coordinates (X, Y points) on a two-dimensional plane,
write a function to count how many rectangles can be formed using these points as corners.

The Constraints:

    A rectangle is only valid if all four of its corners exist in the input dataset.

    The rectangles must be parallel to the X and Y axes (axis-aligned).

    The rectangles must have a non-zero area (no degenerate rectangles)

'''
from collections import defaultdict


def count_rectangles(points):

    total_rectangles = 0
    n = len(points)

    vertical_lines_count = defaultdict(int)

    for i in range(n):
        for j in range(i + 1, n):

            x1, y1 = points[i]
            x2, y2 = points[j]

            # We only care if they form a vertical line (same X coordinate).
            # To ensure we only process each line once and clearly define 
            # 'lower' vs 'upper', we enforce that y1 must be less than y2.
            if x1 == x2 and y1 < y2:

                y_pair = (y1, y2)

                # Step 2: Add the number of PREVIOUS identical vertical lines
                # found at this exact height span to our total count.
                total_rectangles += vertical_lines_count[y_pair]

                # Step 3: Increment the count for this Y-pair in the map.
                vertical_lines_count[y_pair] += 1

    return total_rectangles


test_points = [
    (0, 0), (0, 2),  # First vertical line
    (2, 0), (2, 2),  # Second vertical line
    (4, 0), (4, 2)   # Third vertical line
]
print(count_rectangles(test_points))


# Follow up, What if the rectangles can be tilted or diagonal on the plane instead of just axis-aligned?
from collections import defaultdict


def count_tilted_rectangles(points):

    total_rectangles = 0
    n = len(points)

    # Map to store: Key = (sum_x, sum_y, dist_sq) -> Value = Frequency
    diagonal_map = defaultdict(int)

    # Step 1: Check every single pair of points as a potential diagonal
    for i in range(n):

        for j in range(i + 1, n):  # i+1 ensures we don't check a pair twice (A,B is same as B,A)

            x1, y1 = points[i]
            x2, y2 = points[j]

            # 1. Midpoint components (avoiding division to prevent float precision issues)
            sum_x = x1 + x2
            sum_y = y1 + y2

            # 2. Squared length of the diagonal
            dist_sq = (x1 - x2)**2 + (y1 - y2)**2

            # Our unique key for this diagonal
            diag_key = (sum_x, sum_y, dist_sq)

            # Step 2: If another diagonal shares the exact same center and length,
            # they form a rectangle. Add previous matches to the answer.
            total_rectangles += diagonal_map[diag_key]

            # Step 3: Register this diagonal in the map
            diagonal_map[diag_key] += 1

    return total_rectangles


# Let's test with 4 points that form a tilted square/rectangle (Diamond shape)
# Points: (1,0), (2,1), (1,2), (0,1)
tilted_points = [(1, 0), (2, 1), (1, 2), (0, 1)]
print(f"Total rectangles: {count_tilted_rectangles(tilted_points)}")  # Output: 1