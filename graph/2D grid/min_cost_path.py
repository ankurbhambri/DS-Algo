# Min Cost Path with right and bottom moves allowed.

''' Given a cost matrix cost[][] and a position (m, n) in cost[][],
write a function that returns cost of minimum cost path to reach (m, n) from (0, 0). 
Each cell of the matrix represents a cost to traverse through that cell. 
The total cost of a path to reach (m, n) is the sum of all the costs on that path 
(including both source and destination). You can only traverse down,
right and diagonally lower cells from a given cell, i.e., from a given cell (i, j), 
cells (i+1, j), (i, j+1), and (i+1, j+1) can be traversed. 
You may assume that all costs are positive integers. '''


def minCost(cost, row, col):

    # For 1st column
    for i in range(1, row):
        cost[i][0] += cost[i - 1][0]

    # For 1st row
    for j in range(1, col):
        cost[0][j] += cost[0][j - 1]
    print(cost)
    # For rest of the 2d matrix
    for i in range(1, row):
        for j in range(1, col):
            cost[i][j] += min(
                cost[i - 1][j - 1], min(cost[i - 1][j], cost[i][j - 1])
            )
    print(cost)

    return cost[row - 1][col - 1]


row = 3
col = 3
cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
# Time Complexity: O(row * col)
# Auxiliary Space: O(1)
print(minCost(cost, row, col))


# Minimum Cost Path with Left, Right, Bottom and Up moves allowed

'''Given a two dimensional grid, each cell of which contains integer cost which represents a 
cost to traverse through that cell, we need to find a path from top left cell to 
bottom right cell by which total cost incurred is minimum.
Note : It is assumed that negative cost cycles do not exist in input matrix.
This problem is extension of below problem.
Min Cost Path with right and bottom moves allowed.
'''


def dijkstra(grid):

    row, col = len(grid), len(grid[0])
    dist = [[float("inf")] * col for i in range(row)]

    dist[0][0] = grid[0][0]

    q = [(0, 0)]

    while q:

        r, c = q.pop(0)

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x = r + dr
            y = c + dc
            if (
                x >= 0
                and x < row
                and y >= 0
                and y < col
                and dist[x][y] > dist[r][c] + grid[x][y]
            ):
                dist[x][y] = dist[r][c] + grid[x][y]
                q.append((x, y))

    return dist[row - 1][col - 1]


grid = [
    [31, 100, 65, 12, 18],
    [10, 13, 47, 157, 6],
    [100, 113, 174, 11, 33],
    [88, 124, 41, 20, 140],
    [99, 32, 111, 41, 20],
]
print(dijkstra(grid))
