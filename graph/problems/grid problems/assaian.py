"""
Given a 2D matrix of size N x M. Where N and M can be at most 500. There will be an assassin (depicted as 'A') 
somehwere in the matrix, also there will be some obstacles represented by 'X'. Also there will be some guards.

Guards can appear the following way in the matrix: '<' represents a guard that is looking to the left, '>' 
represents a guard that is looking to the right, '^' looks up, and 'v' is looking down. 
Their line of sight extends as long as there is an obstacle, edge of the matrix or another guard.

Write a function that calculates whether the assassin can reach the bottom-right corner of the matrix. 
The assassin can not step in the line of sight of any guard.

Ex.:
For the input

. v .
. . .
A . .
Answer should be false.

For the input

A . . .
. < X X
. . . . 
Answer should be false.

For the input

. . . <
A . . ^
X . . .
Answer should be true.
"""


def assassin(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c):

        # If reached bottom-right corner
        if r == rows - 1 and c == cols - 1:
            return True

        matrix[r][c] = "#"  # Mark visited

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_r, new_c = r + dr, c + dc
            # Unvisited and no obstacle
            if is_valid(new_r, new_c) and matrix[new_r][new_c] == ".":
                if dfs(new_r, new_c):
                    return True
        return False

    def mark_guard_sight(r, c, direction):

        # if we find sight up side means all above line is blocked
        if direction == "^":
            r -= 1
            while is_valid(r, c) and matrix[r][c] == ".":
                matrix[r][c] = "X"
                r -= 1

        elif direction == "v":
            r += 1
            while is_valid(r, c) and matrix[r][c] == ".":
                matrix[r][c] = "X"
                r += 1

        elif direction == "<":
            c -= 1
            while is_valid(r, c) and matrix[r][c] == ".":
                matrix[r][c] = "X"
                c -= 1

        elif direction == ">":
            c += 1
            while is_valid(r, c) and matrix[r][c] == ".":
                matrix[r][c] = "X"
                c += 1

    # Step 1: Mark guards' lines of sight in the matrix
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] in "^v<>":
                mark_guard_sight(r, c, matrix[r][c])

    # Step 2: Find assassin and start DFS
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == "A":
                return dfs(r, c)

    return False  # No path found


# Example usage:
matrix1 = [[".", "v", "."], [".", ".", "."], ["A", ".", "."]]

matrix2 = [["A", ".", ".", "."], [".", "<", "X", "X"], [".", ".", ".", "."]]

matrix3 = [[".", ".", ".", "<"], ["A", ".", ".", "^"], ["X", ".", ".", "."]]

print(assassin(matrix1))  # Output: False
print(assassin(matrix2))  # Output: False
print(assassin(matrix3))  # Output: True


# Test Cases
matrix1 = [
    [".", "v", "."],
    [".", ".", "."],
    ["A", ".", "."],
]

matrix2 = [
    ["A", ".", ".", "."],
    [".", "<", "X", "X"],
    [".", ".", ".", "."],
]

matrix3 = [
    [".", ".", ".", "<"],
    ["A", ".", ".", "^"],
    ["X", ".", ".", "."],
]

matrix4 = [
    ["X", ".", ".", ".", ".", ".", ">"],
    [".", ".", "v", ".", ".", "X", "."],
    [".", ">", ".", ".", "X", ".", "."],
    ["A", ".", ".", ".", ".", ".", "."],
]

matrix5 = [
    [".", ".", ".", "X", "v"],
    ["A", "X", ".", ".", "^"],
    [".", "X", "X", ".", "."],
]
matrix6 = ["...", ">.A"]
matrix7 = ["A.v", "..."]
print(assassin(matrix1))  # Output: False
print(assassin(matrix2))  # Output: False
print(assassin(matrix3))  # Output: True
print(assassin(matrix4))  # Output: False
print(assassin(matrix5))  # Output: False
