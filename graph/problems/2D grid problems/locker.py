# https://leetcode.com/discuss/interview-question/operating-system/5271472/amazon-phone-screen-sde-ii/2612626

"""

Given grid's dimensions (m and n) and a list of lockers(cooridnates) return a grid[m][n] where every cell represents the euclidean distance to its nearest lockers.

Example
m = 2, n= 2, listofLockers = [[1,2]]

Output:
[[1.4,1]
[1, 0]]


"""


import math


def calculate_distances(m, n, list_of_lockers):

    grid = [[float("inf")] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            for locker in list_of_lockers:
                x, y = locker
                if i == x and j == y:
                    # Set the locker position to 0 without calculating distance
                    grid[i][j] = 0
                else:
                    # Euclidean distance between the cell and the locker
                    distance = math.sqrt((x - i) ** 2 + (y - j) ** 2)

                    if distance < grid[i][j]:
                        grid[i][j] = round(distance, 1)

    return grid


m = 2  # row
n = 2  # col
listOfLockers = [(1, 1)]

print(calculate_distances(m, n, listOfLockers))

m = 4
n = 3
listOfLockers = [(3, 0), (2, 2)]

print(calculate_distances(m, n, listOfLockers))


# Approach: Multisource BFS

from collections import deque


def nearest_lockers(m, n, lockers):
    # Initialize grid with large distances
    grid = [[float("inf")] * n for _ in range(m)]

    # Queue for BFS
    queue = deque()

    # Directions for moving in the grid (up, down, left, right)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Mark all lockers with distance 0 and add them to the queue
    for x, y in lockers:
        grid[x][y] = 0
        queue.append((x, y))

    # BFS from all locker locations
    while queue:
        x, y = queue.popleft()

        # Explore all 4 directions
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            # Check if new coordinates are within bounds
            if 0 <= new_x < m and 0 <= new_y < n:
                # Calculate the Euclidean distance from the current locker
                distance = math.sqrt((new_x - x) ** 2 + (new_y - y) ** 2)

                # If we found a shorter distance to this cell, update it and add it to the queue
                if grid[new_x][new_y] > grid[x][y] + distance:
                    grid[new_x][new_y] = grid[x][y] + distance
                    queue.append((new_x, new_y))

    return grid


m = 4
n = 3
listOfLockers = [(3, 0), (2, 2)]

print(nearest_lockers(m, n, listOfLockers))
