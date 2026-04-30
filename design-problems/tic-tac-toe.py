# https://leetcode.com/problems/design-tic-tac-toe/description/


class TicTacToe:
    def __init__(self, n):

        self.n = n
        self.diagonal = 0
        self.anti_diagonal = 0
        self.rows = [0] * n
        self.cols = [0] * n

    def move(self, row, col, player):

        move_val = 1 if player == 1 else -1   # don't overwrite player

        self.rows[row] += move_val
        self.cols[col] += move_val

        if row == col:
            self.diagonal += move_val

        if row + col == self.n - 1:
            self.anti_diagonal += move_val

        if (
            abs(self.rows[row]) == self.n or
            abs(self.cols[col]) == self.n or
            abs(self.diagonal) == self.n or
            abs(self.anti_diagonal) == self.n
        ):
            return player   # return original player (1 or 2)

        return 0 # no winner yet


obj = TicTacToe(3)
print(obj.move(0, 0, 1))  # Player 1 moves at (0, 0)
print(obj.move(0, 2, 2))  # Player 2 moves at (0, 2)
print(obj.move(2, 2, 1))  # Player 1 moves at (2, 2)
print(obj.move(1, 1, 2))  # Player 2 moves at (1, 1)
print(obj.move(2, 0, 1))  # Player 1 moves at (2, 0)
print(obj.move(1, 0, 2))  # Player 2 moves at (1, 0)
print(obj.move(2, 1, 1))  # Player 1 moves at (2, 1) - Player 1 wins



# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

class Solution:
    def tictactoe(self, moves):

        diagonal = 0
        row = [0] * 3
        cols = [0] * 3
        anti_diagonal = 0

        for i, (r, c) in enumerate(moves):

            player = 1 if i % 2 == 0 else -1 # even index for player 1, odd index for player 2

            row[r] += player
            cols[c] += player

            if r == c:
                diagonal += player

            if r + c == 2:
                anti_diagonal += player

            if (
                abs(row[r]) == 3 or
                abs(cols[c]) == 3 or
                abs(diagonal) == 3 or
                abs(anti_diagonal) == 3
            ):
                return "A" if player == 1 else "B"

        return "Draw" if len(moves) == 9 else "Pending"


print(Solution().tictactoe([[0,0],[1,1],[0,1],[1,2],[0,2]]))  # "A"
print(Solution().tictactoe([[0,0],[1,1],[2,2],[0,1],[1,0],[2,1],[0,2]]))  # "B"
