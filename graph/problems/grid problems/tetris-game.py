"""
You are given a 2d matrix which consist of the following symbols ".", "#", "", where "." represent
free cell, "#" represent a obstacle, "" denotes shape. Your task is to find out the minimum obstacle
to remove from the matrix so that the shapes falls down to the bottom.

Test Case:

    [["*", "*", "*", "*"],
    ["#", "*", ".", "*"],
    [".", ".", "#", "."],
    [".", "#", ".", "#"] ]

    Output = 4
    Simulation:

    Initial matrix:
    [["*", "*", "*", "*"],
    ["#", "*", ".", "*"],
    [".", ".", "#", "."],
    [".", "#", ".", "#"] ]

    After removing matrix[1][0]
    [[".", ".", ".", "."],
    ["*", "*", "*", "*"],
    [".", "*", "#", "*"],
    [".", "#", ".", "#"] ]

    After removing matrix[2][2], matrix[3][1], matrix[3][3], we get
    [[".", ".", ".", "."],
    [".", ".", ".", "."],
    ["*", "*", "*", "*"],
    [".", "*", ".", "*"] ]


    Approach:

    - Iterate through the matrix from bottom to top: This ensures that shapes fall down correctly as obstacles are removed.
    - Check for shapes: If a shape ("*") is found, look for obstacles below it.
    - Find nearest obstacle: Use a while loop to find the first obstacle below the shape, skipping any empty cells.
    - Remove obstacle and increment count: If an obstacle is found, remove it from the matrix and increment the obstacles_removed counter.
    - Return the count: After iterating through the matrix, return the total number of obstacles removed.
"""


def find_min_obstacles(matrix):
    rows, cols = len(matrix), len(matrix[0])
    obstacles_removed = 0

    for i in range(rows - 1, -1, -1):  # starting from last row
        for j in range(cols):
            if matrix[i][j] == "*":
                # Find the nearest obstacle below, if any
                next_row = i + 1
                while next_row < rows and matrix[next_row][j] == ".":
                    next_row += 1

                if next_row < rows and matrix[next_row][j] == "#":
                    obstacles_removed += 1
                    matrix[next_row][j] = "."  # Remove the obstacle

    return obstacles_removed


# Test cases
matrix1 = [
    ["*", "*", "*", "*"],
    ["#", "*", ".", "*"],
    [".", ".", "#", "."],
    [".", "#", ".", "#"],
]
print(find_min_obstacles(matrix1))  # Output: 4
