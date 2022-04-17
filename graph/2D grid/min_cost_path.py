# Min Cost Path with right and bottom moves allowed. ... easy prblm

# https://www.geeksforgeeks.org/min-cost-path-dp-6/

''' Given a cost matrix cost[][] and a position (m, n) in cost[][],
write a function that returns minimum cost path to reach (m, n) from (0, 0). 
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

    # For rest of the 2d matrix
    for i in range(1, row):
        for j in range(1, col):
            cost[i][j] += min(
                cost[i - 1][j - 1], min(cost[i - 1][j], cost[i][j - 1])
            )

    return cost[-1][-1]


row = 3
col = 3
cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
# Time Complexity: O(row * col)
# Auxiliary Space: O(1)
print(minCost(cost, row, col))


# Minimum Cost Path with Left, Right, Bottom and Up moves allowed all four dirs ... hard prblm

'''
Given a two dimensional grid, each cell of which contains integer cost which 
represents a cost to traverse through that cell, we need to find a path from 
top left cell to bottom right cell by which total cost incurred is minimum.
'''

'''It is not possible to solve this problem using dynamic programming similar to 
previous problem (upper prblm) because here current state depends not only on right and bottom 
cells but also on left and upper cells. We solve this problem using dijkstra’s algorithm. 
Each cell of grid represents a vertex and neighbor cells adjacent vertices. 
We do not make an explicit graph from these cells instead we will use matrix 
as it is in our dijkstra’s algorithm. '''

# https://www.geeksforgeeks.org/minimum-cost-path-left-right-bottom-moves-allowed/


def dijkstra(grid):

    row, col = len(grid), len(grid[0])

    dist = [[float("inf")] * col for _ in range(row)]

    dist[0][0] = grid[0][0]  # initialize with first grid distance

    q = [(0, 0)]

    while q:

        r, c = q.pop(0)

        # min in all four directions
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
                # child dist = parent dist + grid dist
                dist[x][y] = dist[r][c] + grid[x][y]
                q.append((x, y))

    return dist[-1][-1]


grid = [
    [31, 100, 65, 12, 18],
    [10, 13, 47, 157, 6],
    [100, 113, 174, 11, 33],
    [88, 124, 41, 20, 140],
    [99, 32, 111, 41, 20],
]
print(dijkstra(grid))
