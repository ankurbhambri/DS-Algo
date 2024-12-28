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

    # Step 1: Create a 2D grid and mark object positions
    grid = [[0] * (c + 1) for _ in range(r + 1)]
    for x, y in positions:
        grid[x][y] += 1

    # Step 2: Construct 2D prefix sum
    prefix_sum = [[0] * (c + 1) for _ in range(r + 1)]
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            prefix_sum[i][j] = (
                grid[i][j]
                + prefix_sum[i - 1][j]
                + prefix_sum[i][j - 1]
                - prefix_sum[i - 1][j - 1]
            )

    # Helper function to calculate sum of objects in a subgrid
    # sum of subgrid = prefix_sum[bottom][right] − prefix_sum[top − 1][right] − prefix_sum[bottom][left − 1]+prefix_sum[top − 1][left − 1]
    def count_objects(top, left, bottom, right):
        return (
            prefix_sum[bottom][right]
            - prefix_sum[top - 1][right]
            - prefix_sum[bottom][left - 1]
            + prefix_sum[top - 1][left - 1]
        )

    # Step 3: Iterate over all possible subgrids
    count = 0
    for top in range(1, r + 1):
        for bottom in range(top, r + 1):
            for left in range(1, c + 1):
                for right in range(left, c + 1):
                    if count_objects(top, left, bottom, right) >= k:
                        count += 1

    return count


# Examples
print(count_rectangles(2, 2, 1, 1, [(1, 2)]))  # Output: 4
print(count_rectangles(3, 2, 3, 3, [(1, 1), (3, 1), (2, 2)]))  # Output: 1
print(count_rectangles(3, 2, 3, 2, [(1, 1), (3, 1), (2, 2)]))  # Output: 4
