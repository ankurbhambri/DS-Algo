"""
You are given a 2D array bubbles representing a game board where each cell contains a positive integer (indicating a bubble’s color).
You are also given a list of operations, where each operation is a pair [r, c] representing a user’s click on the cell at row r and column c. 

For each operation: 

1. If the clicked cell is not empty (non-zero), pop the bubble at [r][c] and any of its four diagonally adjacent neighbors that have the same color. 

2. After popping, apply gravity: in each column, all bubbles fall down to fill empty (zero) cells below them,
    and the top is filled with zeros as needed. 

Return the final state of the board after all operations are applied.
"""


def applyOperations(bubbles, operations):

    if not bubbles or not bubbles[0]:
        return bubbles

    rows = len(bubbles)
    cols = len(bubbles[0])

    for r, c in operations:
        color = bubbles[r][c]
        if color == 0:
            continue

        # 1. Popping the target and same-colored diagonal neighbors
        diagonals = [
            (r - 1, c - 1), (r - 1, c + 1),
            (r + 1, c - 1), (r + 1, c + 1)
        ]

        for dr, dc in diagonals:
            if 0 <= dr < rows and 0 <= dc < cols:
                if bubbles[dr][dc] == color:
                    bubbles[dr][dc] = 0

        # Pop the clicked cell itself
        bubbles[r][c] = 0

        # 2. Apply Gravity (Column by Column)
        for j in range(cols):
            # Pointer for the position where the next bubble should fall
            fill_ptr = rows - 1
            for i in range(rows - 1, -1, -1):
                if bubbles[i][j] != 0:
                    # Swap current bubble with the lowest empty slot
                    bubbles[fill_ptr][j] = bubbles[i][j]
                    if fill_ptr != i:
                        bubbles[i][j] = 0
                    fill_ptr -= 1

    return bubbles


# Example 1
board1 = [
    [1, 2, 1],
    [2, 1, 2],
    [1, 2, 1],
]
ops1 = [[1, 1]]
# Click (1,1) color=1 → pop (1,1) and diagonal matches: (0,0)=1, (0,2)=1, (2,0)=1, (2,2)=1
# Board after pop:
#  [0, 2, 0]
#  [2, 0, 2]
#  [0, 2, 0]
# After gravity:
#  [0, 0, 0]
#  [0, 2, 0]
#  [2, 2, 2]
print(applyOperations(board1, ops1))

# Example 2
board2 = [
    [3, 1, 2],
    [1, 3, 1],
    [2, 1, 3],
]
ops2 = [[0, 0], [2, 2]]
# Click (0,0) color=3, diag (1,1)=3 → pop both
# Board after pop: [[0,1,2],[1,0,1],[2,1,3]]
# Gravity: [[0,0,2],[1,1,1],[2,1,3]]
# Click (2,2) color=3, diag (1,1)=1 ≠ 3 → only pop (2,2)
# Board: [[0,0,2],[1,1,1],[2,1,0]]
# Gravity: [[0,0,0],[1,1,2],[2,1,1]]
print(applyOperations(board2, ops2))
