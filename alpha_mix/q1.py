"""
    You are given a grid of size r × c and n objects located at specific coordinates. 
    
    You need to find the number of axis-parallel rectangular subgrids that contain at least k of these objects.

    Two rectangles are considered different if their coordinates are different.

    def count_rectangles(r: int, c: int, n: int, k: int, positions: List[Tuple[int, int]]) -> int:

    eg. 1
    r = 2
    c = 2
    n = 1
    k = 1
    positions = [(1, 2)]

    ans: 4


    r = 3
    c = 2
    n = 3
    k = 3
    positions = [(1, 1), (3, 1), (2, 2)]

    ans: 1
    
    r = 3
    c = 2
    n = 3
    k = 2
    positions = [(1, 1), (3, 1), (2, 2)]

    ans: 4

"""


def count_rectangles(r, c, n, k, positions):

    # Step 1: Create a grid and mark positions
    grid = [[0] * (c + 1) for _ in range(r + 1)]
    for x, y in positions:
        grid[x][y] += 1

    # Step 2: Build a prefix sum array
    prefix_sum = [[0] * (c + 1) for _ in range(r + 1)]
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            prefix_sum[i][j] = (
                grid[i][j]
                + prefix_sum[i - 1][j]
                + prefix_sum[i][j - 1]
                - prefix_sum[i - 1][j - 1]
            )

    # Function to calculate the sum of objects in a given subgrid
    def get_sum(x1, y1, x2, y2):
        return (
            prefix_sum[x2][y2]
            - prefix_sum[x1 - 1][y2]
            - prefix_sum[x2][y1 - 1]
            + prefix_sum[x1 - 1][y1 - 1]
        )

    # Step 3: Iterate over all possible subgrids
    count = 0
    for row1 in range(1, r + 1):
        for row2 in range(row1, r + 1):
            for col1 in range(1, c + 1):
                for col2 in range(col1, c + 1):
                    # Count the number of objects in this subgrid
                    if get_sum(row1, col1, row2, col2) >= k:
                        count += 1

    return count


print(count_rectangles(2, 2, 1, 1, [(1, 2)]))  # Output: 4
print(count_rectangles(3, 2, 3, 3, [(1, 1), (3, 1), (2, 2)]))  # Output: 1
print(count_rectangles(3, 2, 3, 2, [(1, 1), (3, 1), (2, 2)]))  # Output: 4
