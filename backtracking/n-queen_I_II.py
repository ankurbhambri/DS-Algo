# https://leetcode.com/problems/n-queens/
# https://leetcode.com/problems/n-queens-ii/

'''

| Type              | Formula | Direction                 | Looks Like |
| ----------------- | ------- | ------------------------- | ---------- |
| **Column**        | `c`     | vertical                  |            |
| **Positive Diag** | `r + c` | top-left → bottom-right ↘ | `/`        |
| **Negative Diag** | `r - c` | top-right → bottom-left ↙ | `\`        |

'''

# TC: O(N!) — because you try placing queens row by row and prune using the sets.
# SC: O(N^2) - for the board, and O(N) for each of the sets (cols, pos_diag, neg_diag)

class Solution:
    def NQueens(self, n: int) -> int:

        res = []
        board = []

        # Sets to track used columns and diagonals
        cols = set()
        pos_diag = set()  # r + c
        neg_diag = set()  # r - c

        def backtrack(r):
            # If we've placed queens in all rows
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                # Place queen
                row = ["."] * n
                row[c] = "Q"
                board.append(row)
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                # Recurse to next row
                backtrack(r + 1)

                # Backtrack
                board.pop()
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

        backtrack(0)

        # Whole code is same for both N-Queens I and II, just the return the board in 1st problem and in 2nd return the count of solutions
        return res # len(res) in 2nd problem
